import os
from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Configuration du modèle de génération d'embeddings
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Fonction pour initialiser Chroma DB
def get_chroma_db():
    return Chroma(
        persist_directory=os.getenv("CHROMA_DB_DIRECTORY", "chroma_db"),
        embedding_function=embedding_function
    )

# Fonction pour ajouter un document à Chroma DB
def add_document_to_chroma(doc_id, schema_type, file_path):
    db = get_chroma_db()
    loader = PyPDFLoader(file_path=file_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    db.add(
        documents=docs,
        metadatas=[{"doc_id": doc_id, "schema_type": schema_type}],
        ids=[doc_id]
    )
    db.persist()

# Fonction pour supprimer un document de Chroma DB
def delete_document_from_chroma(doc_id):
    db = get_chroma_db()
    db.delete(ids=[doc_id])
    db.persist()
