import os
from langchain_chroma import Chroma
# from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from .utils import filter_complex_metadata
from .llms import get_embedding_openai

# Configuration du modèle de génération d'embeddings
# embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
embedding_function = get_embedding_openai()

# Fonction pour ajouter un document à Chroma DB
def add_document_to_chroma(doc_id, schema_type, file_path):

    loader = PyPDFLoader(file_path="./" + file_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    for doc in docs:
        additional_metadata = filter_complex_metadata({"doc_id": doc_id, "schema_type": schema_type})
        if doc.metadata:
            doc.metadata.update(additional_metadata)
        else:
            doc.metadata = additional_metadata

    Chroma.from_documents(
        documents=docs,
        ids=[doc_id],
        persist_directory=os.getenv("CHROMA_DB_DIRECTORY", "chroma_db"),
        embedding=embedding_function
    )


# Fonction pour supprimer un document de Chroma DB
def delete_document_from_chroma(doc_id):
    db = Chroma(
        persist_directory=os.getenv("CHROMA_DB_DIRECTORY", "chroma_db"),
    )

    db.delete(doc_id)