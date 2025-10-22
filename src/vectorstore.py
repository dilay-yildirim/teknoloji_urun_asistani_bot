# src/vectorstore.py
import chromadb
import os

CHROMA_DIR = os.getenv("CHROMA_DB_DIR", "./data/chroma_db")

def get_client():
    # Yeni Chroma sürümü: PersistentClient kullanılıyor
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    return client

def create_or_get_collection(name="reviews"):
    client = get_client()
    try:
        col = client.get_collection(name)
    except Exception:
        col = client.create_collection(name)
    return col
