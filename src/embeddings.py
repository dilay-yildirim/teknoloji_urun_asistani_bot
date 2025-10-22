from sentence_transformers import SentenceTransformer
import os

MODEL_NAME = os.getenv("SENTENCE_TRANSFORMER_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

class Embedder:
    def __init__(self, model_name=MODEL_NAME):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts):
        return self.model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
