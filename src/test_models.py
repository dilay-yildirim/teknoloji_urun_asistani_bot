# src/test_models.py
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY .env dosyasında tanımlı değil!")

# API anahtarını yapılandır
genai.configure(api_key=api_key)

print("🔍 Desteklenen Gemini modelleri listeleniyor...\n")

supported_models = []
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        supported_models.append(m.name)
        print("✅", m.name)

if not supported_models:
    print("\n⚠️ Uygun model bulunamadı! API anahtarını kontrol et.")
else:
    # Otomatik olarak uygun model seç
    preferred_model = None
    for candidate in ["models/gemini-1.5-flash", "models/gemini-1.5-pro"]:
        if candidate in supported_models:
            preferred_model = candidate
            break

    if preferred_model:
        print(f"\n💡 Kullanılabilecek model: {preferred_model}")
        # .env dosyasına yaz (geçici)
        with open(".env", "r") as f:
            lines = f.readlines()

        updated = False
        with open(".env", "w") as f:
            for line in lines:
                if line.startswith("GEMINI_MODEL="):
                    f.write(f"GEMINI_MODEL={preferred_model.split('/')[-1]}\n")
                    updated = True
                else:
                    f.write(line)
            if not updated:
                f.write(f"\nGEMINI_MODEL={preferred_model.split('/')[-1]}\n")

        print("✅ .env dosyası otomatik güncellendi.")
    else:
        print("\n⚠️ 'gemini-1.5-flash' veya 'gemini-1.5-pro' modelleri bulunamadı.")
