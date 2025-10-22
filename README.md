# 🤖 TEKNOLOJİ ÜRÜN ASİSTANI CHATBOT

PROJE AMACI
Bu proje, kullanıcıların teknoloji ürünleri hakkında bilgi almasını kolaylaştırmak amacıyla geliştirilmiş bir yapay zekâ destekli ürün asistanıdır.  
Asistan, ürün yorumlarını analiz ederek kullanıcıya tavsiye, yorum özeti ve satın alma yönlendirmesi sunar.  
Model, gerçek kullanıcı yorumlarını anlamlandırarak doğal diyaloglarla yanıt verir.

---

## 📦 Veri Seti Hakkında
Proje, Hugging Face üzerinden alınan aşağıdaki veri kümesini kullanmaktadır:

Veri seti: [`fthbrmnby/turkish_product_reviews`](https://huggingface.co/datasets/fthbrmnby/turkish_product_reviews)  
- Türkçe teknoloji ürün yorumlarını içerir.  
- Her kayıt: ürün kategorisi, başlık, yorum ve puan alanlarını barındırır.  
- Eğitim aşamasında `SAMPLE_LIMIT=15000` kayıt ile test edilmiştir.

---

## 🧠 Kullanılan Yöntemler ve Teknolojiler

| Teknoloji | Açıklama |
|------------|-----------|
| **Python** | Projenin ana dili |
| **Streamlit** | Web arayüzü geliştirme framework’ü |
| **Hugging Face Datasets** | Yorum verilerini sağlama |
| **Sentence-Transformers (MiniLM-L12-v2)** | Metin embedding (anlam vektörleştirme) |
| **ChromaDB** | Vektör veritabanı — yorumların anlam bazlı aranması |
| **Google Gemini API (gemini-2.5-flash)** | Cevap üretimi ve doğal dil işleme |
| **dotenv & Secrets** | Anahtar yönetimi (GEMINI_API_KEY ve HUGGINGFACE_TOKEN) |

---

## ⚙️ Proje Yapısı
📦 teknoloji_urun_asistani_bot
├── 📁 data/ → ChromaDB vektör verileri
├── 📁 scripts/ → Veri çekme & embedding oluşturma
├── 📁 src/
│ ├── ingest.py → Hugging Face’ten veri çekip ChromaDB’ye ekler
│ ├── rag_query.py → Arama + Cevap üretimi (RAG pipeline)
│ └── streamlit_app.py → Ana web arayüzü (Streamlit)
├── .env (gizli) → API anahtarları (lokalde)
├── requirements.txt → Gerekli Python kütüphaneleri
└── README.md → Proje açıklaması (bu dosya)


---

## 🚀 Elde Edilen Sonuçlar
- Chatbot, teknoloji ürünlerine ait kullanıcı yorumlarını analiz ederek anlamlı, bağlama uygun yanıtlar üretebilmektedir.  
- Hugging Face verisinden gelen yorumlar sayesinde model, Türkçe dilinde oldukça akıcı çalışmaktadır.  
- Kullanıcı sorularına göre:  
  - Ürün memnuniyetini özetleyebilir,  
  - Olumlu/olumsuz yönleri çıkarabilir,  
  - Benzer ürün tavsiyeleri sunabilir.

---

## 🔧 Nasıl Çalıştırılır (Yerel Ortamda)

```bash
# 1. Ortamı klonla
git clone https://github.com/dilay-yildirim/teknoloji_urun_asistani_bot.git
cd teknoloji_urun_asistani_bot

# 2. Sanal ortam oluştur
python -m venv .venv
.venv\Scripts\activate     # (Windows)
# veya
source .venv/bin/activate  # (Mac/Linux)

# 3. Gereksinimleri yükle
pip install -r requirements.txt

# 4. .env dosyasına anahtarları ekle
GEMINI_API_KEY="YOUR_GEMINI_KEY"
HUGGINGFACE_TOKEN="YOUR_HF_TOKEN"

# 5. Uygulamayı başlat
streamlit run src/streamlit_app.py

---

## UYGULUAMA LİNKİ : [Canlı Uygulamayı Aç](https://teknolojiurunasistanibot-i52mwd6rzlduxnnwa6zbd9.streamlit.app/)



---
DİLAY YILDIRIM 
GAIH GenAI Bootcamp — Final Projesi EKİM 2025
