# src/rag_query.py
import os
from dotenv import load_dotenv
from vectorstore import create_or_get_collection
from embeddings import Embedder
from google import generativeai as genai

load_dotenv()

# API ve model ayarları
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.1-chat")  # desteklenen bir model girin

assert GEMINI_API_KEY, "⚠️ Lütfen GEMINI_API_KEY'i .env dosyasına ekle!"

# GenAI client oluştur
client = genai.Client(api_key=GEMINI_API_KEY)


class ProductAssistant:
    def __init__(self, k=5):
        self.col = create_or_get_collection("reviews")
        self.embedder = Embedder()
        self.k = k

    def retrieve(self, query):
        """Kullanıcı sorusuna en uygun yorumları getir"""
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
        """RAG ile yanıt üret"""
        context = "\n\n---\n".join([f"Yorum: {h['doc']}" for h in hits])
        prompt = f"""
Sen bir ürün asistanısın. Aşağıdaki kullanıcı yorumlarına dayanarak kullanıcının sorusuna Türkçe yanıt ver.
Soru: {user_query}

Bağlam (yorumlar):
{context}

Kısa, samimi ve öneri içeren bir yanıt oluştur:
"""
        # Chat başlat
        chat = client.chats.create(model=MODEL_NAME)

        # Mesaj gönder
        chat.send_message(prompt)

        # Yanıtı al
        response = chat.get_message()
        return response.content.strip()

    def ask(self, query):
        hits = self.retrieve(query)
        answer = self.generate_answer(query, hits)
        return {"answer": answer, "hits": hits}


# Test
if __name__ == "__main__":
    assistant = ProductAssistant()
    q = "Kargo hızı ve paketleme kalitesi hakkında ne düşünüyorsun?"
    print(assistant.ask(q)["answer"])
