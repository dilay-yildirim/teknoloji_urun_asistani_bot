import os
from datasets import load_dataset
from dotenv import load_dotenv
from embeddings import Embedder
from vectorstore import create_or_get_collection
from tqdm.auto import tqdm

load_dotenv()
DATASET_NAME = os.getenv("HF_DATASET_NAME", "fthbrmnby/turkish_product_reviews")
SAMPLE_LIMIT = int(os.getenv("SAMPLE_LIMIT", "30000"))

def ingest():
    print(f"📦 Dataset yükleniyor: {DATASET_NAME}")
    ds = load_dataset(DATASET_NAME, split="train")

    if "sentence" in ds.column_names:
        texts = ds["sentence"]
    elif "text" in ds.column_names:
        texts = ds["text"]
    else:
        raise ValueError("Metin sütunu bulunamadı!")

    texts = texts[:SAMPLE_LIMIT]
    embedder = Embedder()
    collection = create_or_get_collection("reviews")

    print("🔢 Embedding'ler oluşturuluyor ve veritabanına ekleniyor...")
    batch_size = 256
    for i in tqdm(range(0, len(texts), batch_size)):
        batch = texts[i:i+batch_size]
        embs = embedder.embed_texts(batch)
        ids = [f"rev_{i+j}" for j in range(len(batch))]
        metas = [{"source": DATASET_NAME}] * len(batch)
        collection.add(ids=ids, documents=batch, metadatas=metas, embeddings=embs.tolist())

    print("✅ Ingestion tamamlandı!")

if __name__ == "__main__":
    ingest()
