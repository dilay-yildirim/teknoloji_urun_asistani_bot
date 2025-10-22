# src/streamlit_app.py
import streamlit as st
from rag_query import ProductAssistant

st.set_page_config(page_title="Türkçe Ürün Asistanı", layout="centered")
st.title("🇹🇷 Türkçe Ürün Asistanı (RAG Chatbot)")

assistant = ProductAssistant(k=5)

query = st.text_input("Ürün hakkında ne merak ediyorsun?")

if st.button("Cevapla") and query.strip():
    with st.spinner("Cevap oluşturuluyor..."):
        try:
            # Asistan yanıtı
            res = assistant.ask(query)

            st.subheader("💬 Asistanın Yanıtı")
            st.write(res["answer"])

            st.subheader("📚 Kullanılan Yorumlar")
            for i, h in enumerate(res["hits"][:5]):
                st.markdown(f"**Yorum {i+1}:** {h['doc'][:400]}...")
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
