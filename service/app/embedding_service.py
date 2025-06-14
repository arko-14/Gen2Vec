import os
import pandas as pd
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
from langchain_google_vertexai.embeddings import VertexAIEmbeddings  

def embed_and_preview(csv_path: str, collection_name: str = "records"):
    df = pd.read_csv(csv_path)
    texts = df['text'].tolist()

    embedder = VertexAIEmbeddings(
        model_name="text-embedding-005",
        project=os.getenv('PROJECT_ID') or "gen-lang-client-0378774532"
    )
    vectors = embedder.embed_documents(texts)

    print("\n🔍 Sample Embeddings from your file:")
    for i in range(min(5, len(vectors))):
        print(f"\nText {i+1}: {texts[i]}")
        print(f"Embedding (len={len(vectors[i])}): {vectors[i][:8]} ...")

    os.makedirs("output", exist_ok=True)
    df_embed = pd.DataFrame(vectors)
    df_embed.insert(0, "text", texts)
    df_embed.to_csv("output/embeddings.csv", index=False)
    print("\n✅ Saved to output/embeddings.csv")

   
    client = QdrantClient(host="qdrant", port=6333)

    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=len(vectors[0]), distance=Distance.COSINE)
    )
    points = [
        {"id": int(df.loc[i, "id"]), "vector": vectors[i], "payload": {"text": texts[i]}}
        for i in range(len(vectors))
    ]
    client.upsert(collection_name=collection_name, points=points)
    print(f"\n✅ Upserted {len(points)} records to Qdrant.")

embed_and_preview("data/generated.csv")

