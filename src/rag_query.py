import os
from dotenv import load_dotenv
from vectorstore import create_or_get_collection
from embeddings import Embedder
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

assert GEMINI_API_KEY, "⚠️ Lütfen GEMINI_API_KEY'i .env dosyasına ekle!"

genai.configure(api_key=GEMINI_API_KEY)

class ProductAssistant:
    def __init__(self, k=5):
        self.col = create_or_get_collection("reviews")
        self.embedder = Embedder()
        self.k = k

    def retrieve(self, query):
        q_emb = self.embedder.embed_texts([query])[0].tolist()
        res = self.col.query(
            query_embeddings=[q_emb],
            n_results=self.k,
            include=["documents", "metadatas"]
        )
        hits = []
        for docs, metas in zip(res["documents"], res["metadatas"]):
            for doc, meta in zip(docs, metas):
                hits.append({"doc": doc, "meta": meta})
        return hits

    def generate_answer(self, user_query, hits):
        context = "\n\n---\n".join([f"Yorum: {h['doc']}" for h in hits])
        prompt = f"""
Sen bir teknoloji ürün asistanısın. Aşağıdaki kullanıcı yorumlarına dayanarak Türkçe bir yanıt oluştur.
Soru: {user_query}

Yorumlar:
{context}

Kısa, samimi ve öneri içeren bir cevap oluştur:
"""
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text

    def ask(self, query):
        hits = self.retrieve(query)
        answer = self.generate_answer(query, hits)
        return {"answer": answer, "hits": hits}

if __name__ == "__main__":
    assistant = ProductAssistant()
    q = "Kargo hızı ve pil ömrü hakkında ne düşünülüyor?"
    print(assistant.ask(q)["answer"])
