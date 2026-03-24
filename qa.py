import os
import numpy as np
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def embed_texts(texts):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [np.array(e.embedding) for e in response.data]


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve_relevant_chunks(query, chunks, chunk_embeddings, top_k=3):
    query_embedding = embed_texts([query])[0]

    scores = []
    for i, emb in enumerate(chunk_embeddings):
        score = cosine_similarity(query_embedding, emb)
        scores.append((score, chunks[i]["text"], chunks[i]["page"]))

    scores.sort(reverse=True)

    return [
        {"text": chunk, "page": page}
        for _, chunk, page in scores[:top_k]
    ]


def answer_question(question, chunks, chunk_embeddings):
    relevant_chunks = retrieve_relevant_chunks(question, chunks, chunk_embeddings)

    context = "\n\n".join(
        [f"(Page {c['page']}) {c['text']}" for c in relevant_chunks]
    )

    prompt = f"""
You are answering questions about a research paper.

Use ONLY the context below.

Return your answer in this format:

### 🧠 Answer
Clear and concise explanation.

### 📌 Evidence
Provide a SHORT quote (max 1-2 sentences).

### 📄 Source
Page number.

Rules:
- Always cite the page number like: "Page X"
- Keep evidence short and relevant
- If the user asks for a simplified explanation (e.g., "like I'm 5"), adapt the tone accordingly while staying grounded in the text
- If unsure, say: "The paper does not clearly state this"

Question:
{question}

Context:
{context}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content