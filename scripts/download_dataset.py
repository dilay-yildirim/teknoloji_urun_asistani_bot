from datasets import load_dataset
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
dataset_name = os.getenv("HF_DATASET_NAME", "fthbrmnby/turkish_product_reviews")

def main():
    ds = load_dataset(dataset_name, split="train")
    print(f"Dataset loaded: {dataset_name} - {len(ds)} rows")
    df = ds.to_pandas()
    sample = df.sample(frac=0.1, random_state=42)
    os.makedirs("data", exist_ok=True)
    sample.to_csv("data/reviews_sample.csv", index=False)
    print("✅ Saved data/reviews_sample.csv")

if __name__ == "__main__":
    main()
