import numpy as np
from openai import OpenAI

client = OpenAI()

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def embed(text: str):
    return client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    ).data[0].embedding


def retrieve_best_kb_item(query_embedding, kb):
    best_item = None
    best_score = -1

    for item in kb:
        emb = embed(item["title"] + " " + item["content"])
        score = cosine_similarity(query_embedding, emb)

        if score > best_score:
            best_score = score
            best_item = item

    return best_item, round(best_score * 100, 2)
