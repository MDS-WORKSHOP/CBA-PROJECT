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
    try:
        loader = PyPDFLoader(file_path="./" + file_path)
        documents = loader.load()

        # Vérifiez si le chargement a réussi et que la liste n'est pas vide
        if not documents:
            raise ValueError("No documents loaded from file.")

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(documents)

        # Vérifiez si le fractionnement a réussi et que la liste n'est pas vide
        if not chunks:
            raise ValueError("No chunks created from documents.")

#         for doc in docs:
#             additional_metadata = filter_complex_metadata({"doc_id": doc_id, "schema_type": schema_type})
#             if doc.metadata:
#                 doc.metadata.update(additional_metadata)
#             else:
#                 doc.metadata = additional_metadata

        print("Adding document to Chroma DB", doc_id, schema_type, file_path)
        Chroma.from_documents(
            documents=chunks,
            persist_directory=os.getenv("CHROMA_DB_DIRECTORY", "chroma_db"),
            embedding=embedding_function
        )
    except Exception as e:
        print(f"Error in add_document_to_chroma: {str(e)}")
        raise


# Fonction pour supprimer un document de Chroma DB
def delete_document_from_chroma(doc_id):
    db = Chroma(
        persist_directory=os.getenv("CHROMA_DB_DIRECTORY", "chroma_db"),
    )

    db.delete(doc_id)

def get_chroma_db():
    return Chroma(
        persist_directory=os.getenv("CHROMA_DB_DIRECTORY", "chroma_db"),
        embedding_function=embedding_function
    )