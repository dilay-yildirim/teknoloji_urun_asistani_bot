from google import genai
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # veya direkt API key
client = genai.Client(api_key=GEMINI_API_KEY)

# Mevcut modelleri listele
models = client.list_models()
for m in models:
    print(m.name, m.supported_generation_methods)
