# 🤖 Teknoloji Ürün Asistanı (RAG Chatbot)

PROJENİN AMACI
Bu projenin amacı, teknoloji ürünlerine ait kullanıcı yorumlarını analiz ederek  
ürün hakkında **doğal dilde, Türkçe ve anlamlı yanıtlar üretebilen** bir asistan geliştirmektir.  
Sistem, kullanıcıdan gelen soruyu anlamlandırıp, gerçek yorumlar içinden en alakalı bilgileri bulur  
ve bunlara dayanarak **öneri ve özet** sunar.

---

VERİ SETİ
Proje, **Hugging Face** üzerinden alınan `fthbrmnby/turkish_product_reviews` veri setini kullanır.  
Bu veri seti, çeşitli e-ticaret platformlarından toplanmış Türkçe kullanıcı yorumlarını içerir.  
Yorumlar; ürün kalitesi, teslimat süresi, fiyat performansı, pil ömrü gibi birçok özelliğe dair  
doğrudan kullanıcı geri bildirimlerini barındırır.

Veri kümesinin temel amacı, Türkçe metinlerde duygu ve değerlendirme analizine olanak sağlamaktır.  
Projemiz bu yorumları kullanarak semantik arama ve doğal yanıt üretimi yapmaktadır.

---

KULLANILAN YÖNTEMLER
- **RAG (Retrieval-Augmented Generation)** mimarisi:  
  Kullanıcı sorgusu, önceden indekslenmiş yorumlardan en alakalı olanları getirir (retrieval),  
  ardından **Gemini API** kullanılarak anlamlı bir yanıt üretilir (generation).

- **Vektör Veritabanı (ChromaDB):**  
  Ürün yorumları embedding vektörlerine dönüştürülerek saklanır.  
  Arama işlemleri benzerlik skoruna göre yapılır.

- **Embedding Modeli:**  
  `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`  
  → Çok dilli destekli, Türkçe metinler için optimize edilmiş.

- **LLM (Gemini 2.5 Flash):**  
  Google’ın büyük dil modeli, Türkçe doğal dil üretiminde kullanıldı.

- **Streamlit:**  
  Kullanıcıların doğrudan web tarayıcısı üzerinden etkileşim kurabildiği sade arayüz.

---

ELDE EDİLEN SONUÇLAR
- Chatbot, ürün hakkındaki yorumlardan **konuya uygun, özet ve Türkçe yanıtlar** üretebilmektedir.  
- Kullanıcı testlerinde, özellikle “pil ömrü”, “teslimat hızı”, “kalite” gibi temalarda  
  doğru yorumları çekip anlamlı açıklamalar sunmuştur.  
- Sistem, farklı sorgulara karşı **dinamik ve güvenilir** cevaplar üretmektedir.  
- Sonuç: RAG mimarisi + Gemini API birleşimi, Türkçe veri setleriyle başarılı bir performans göstermiştir.  

---


Chatbot uygulamasına buradan erişebilirsiniz 👇  
https://teknolojiurunasistanibot-i52mwd6rzlduxnnwa6zbd9.streamlit.app/

---
DİLAY YILDIRIM 
GAIH GenAI Bootcamp — Final Projesi
