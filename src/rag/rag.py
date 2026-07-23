import json
import numpy as np
import faiss
import PyPDF2
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer, CrossEncoder
from groq import Groq
from config import GOLD_PATH


groq_client = Groq(api_key="YOUR_GROQ_API_KEY")

def call_llm(prompt):
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content

#  نماذج RAG
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

#  قراءة بيانات Gold
records = []
with open(GOLD_PATH, "r", encoding="utf-8") as f:
    for line in f:
        records.append(json.loads(line))

gold_texts = [
    f"Patient {r['Patient_Name']} has condition {r['Condition']} "
    f"and billing {r['Billing_Amount']} at hospital {r['Hospital']}."
    for r in records
]

#  قراءة PDF 
pdf_path = "C:\Users\arwa_\OneDrive\Desktop\Hospital_Project\data\rag_docs\CDC diabetes.pdf"
pdf_reader = PyPDF2.PdfReader(pdf_path)

pdf_text = ""
for page in pdf_reader.pages:
    pdf_text += page.extract_text()

#  Chunking
def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

pdf_chunks = chunk_text(pdf_text)

#  دمج كل النصوص
all_docs = gold_texts + pdf_chunks

#  Embeddings + FAISS
embeddings = embed_model.encode(all_docs)
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

#  BM25
tokenized_docs = [doc.split() for doc in all_docs]
bm25 = BM25Okapi(tokenized_docs)


#  RRF (Hybrid Search)

def rrf_fusion(dense_indices, bm25_indices, k=60):
    scores = {}
    for rank, idx in enumerate(dense_indices):
        scores[idx] = scores.get(idx, 0) + 1 / (k + rank)
    for rank, idx in enumerate(bm25_indices):
        scores[idx] = scores.get(idx, 0) + 1 / (k + rank)
    return sorted(scores.keys(), key=lambda x: scores[x], reverse=True)

#  دالة البحث RAG
def rag_search(query, top_k=5):
    # Dense search
    q_emb = embed_model.encode([query])
    distances, indices = index.search(q_emb, k=top_k)
    dense_indices = indices[0].tolist()

    # BM25 search
    bm25_scores = bm25.get_scores(query.split())
    bm25_indices = np.argsort(bm25_scores)[::-1][:top_k].tolist()

    # Hybrid search
    fused = rrf_fusion(dense_indices, bm25_indices)

    # Reranking
    candidates = [all_docs[i] for i in fused]
    pairs = [[query, c] for c in candidates]
    ce_scores = cross_encoder.predict(pairs)

    reranked = [
        doc for _, doc in sorted(
            zip(ce_scores, candidates),
            key=lambda x: x[0],
            reverse=True
        )
    ]

    return reranked[:3]  # أفضل 3 سياقات


def answer_with_llm(query):
    contexts = rag_search(query)
    context_block = "\n\n---\n\n".join(contexts)

    prompt = f"""
You are a helpful medical assistant specialized in diabetes.

Use ONLY the context below to answer the question.
Do not make up information.

Context:
{context_block}

Question:
{query}

Answer:
"""

    answer = call_llm(prompt)
    return answer, contexts


if __name__ == "__main__":
    q = "What are early symptoms of diabetes?"
    ans, ctx = answer_with_llm(q)

    print("Answer:\n", ans)
    print("\nCitations:\n")
    for c in ctx:
        print("-", c[:200], "...")