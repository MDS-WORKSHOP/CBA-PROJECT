import os
from langchain.prompts import PromptTemplate
# from langchain.llms import ChatGroq
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_chroma import Chroma
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain.schema import Document
from langgraph.graph import END, StateGraph
from .llms import get_embedding_openai, get_openai_llm
from .chroma_utils import get_chroma_db

embedding_function = get_embedding_openai()


# Définir les templates de prompt
retrieval_prompt_template = PromptTemplate(
    template="""system You are a grader assessing relevance 
    of a retrieved document to a user question. If the document contains keywords related to the user question, 
    grade it as relevant. It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question. \n
    Provide the binary score as a JSON with a single key 'score' and no premable or explanation.
     user
    Here is the retrieved document: \n\n {document} \n\n
    Here is the user question: {question} \n assistant
    """,
    input_variables=["question", "document"],
)

answer_prompt_template = PromptTemplate(
    template="""system You are an assistant for question-answering tasks. 
    Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. 
    Use three sentences maximum and keep the answer concise user
    Question: {question} 
    Context: {context} 
    Answer: assistant""",
    input_variables=["question", "context"],
)

hallucination_prompt_template = PromptTemplate(
    template="""system You are a grader assessing whether 
    an answer is grounded in / supported by a set of facts. Give a binary 'yes' or 'no' score to indicate 
    whether the answer is grounded in / supported by a set of facts. Provide the binary score as a JSON with a 
    single key 'score' and no preamble or explanation. user
    Here are the facts:
    \n ------- \n
    {documents} 
    \n ------- \n
    Here is the answer: {generation}  assistant""",
    input_variables=["generation", "documents"],
)

usefulness_prompt_template = PromptTemplate(
    template="""system You are a grader assessing whether an 
    answer is useful to resolve a question. Give a binary score 'yes' or 'no' to indicate whether the answer is 
    useful to resolve a question. Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.
    user Here is the answer:
    \n ------- \n
    {generation} 
    \n ------- \n
    Here is the question: {question} assistant""",
    input_variables=["generation", "question"],
)

# Define the state graph
def create_state_graph(gpt_4: True):
    llm = get_openai_llm()
    db = get_chroma_db()
    retriever = db.as_retriever()

    retrieval_grader = retrieval_prompt_template | llm | JsonOutputParser()
    rag_chain = answer_prompt_template | llm | StrOutputParser()
    hallucination_grader = hallucination_prompt_template | llm | JsonOutputParser()
    usefulness_grader = usefulness_prompt_template | llm | JsonOutputParser()

    # Define the nodes
    def retrieve(state):
        question = state["question"]
        documents = retriever.invoke(question)
        return {"documents": documents, "question": question}

    def generate(state):
        question = state["question"]
        documents = state["documents"]
        generation = rag_chain.invoke({"context": documents, "question": question})
        return {"documents": documents, "question": question, "generation": generation}

    def grade_documents(state):
        question = state["question"]
        documents = state["documents"]
        filtered_docs = []
        web_search = "No"
        for d in documents:
            score = retrieval_grader.invoke({"question": question, "document": d.page_content})
            if score["score"].lower() == "yes":
                filtered_docs.append(d)
            else:
                web_search = "Yes"
        return {"documents": filtered_docs, "question": question, "web_search": web_search}

    def grade_generation(state):
        documents = state["documents"]
        generation = state["generation"]

        hallucination_score = hallucination_grader.invoke({"documents": documents, "generation": generation})
        usefulness_score = usefulness_grader.invoke({"question": state["question"], "generation": generation})

        return {
            "documents": documents,
            "generation": generation,
            "hallucination_score": hallucination_score,
            "usefulness_score": usefulness_score
        }

    # Create the state graph
    workflow = StateGraph()

    workflow.add_node("retrieve", retrieve)
    workflow.add_node("generate", generate)
    workflow.add_node("grade_documents", grade_documents)
    workflow.add_node("grade_generation", grade_generation)

    # Define the edges
    workflow.add_edge("retrieve", "grade_documents")
    workflow.add_edge("grade_documents", "generate", condition=lambda state: state["web_search"] == "No")
    workflow.add_edge("generate", "grade_generation")
    workflow.add_edge("grade_generation", END)
    app = workflow.compile()
    return app