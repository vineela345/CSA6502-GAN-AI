from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Python is a programming language.",
    "Machine learning is a branch of artificial intelligence.",
    "Deep learning uses neural networks.",
    "Football is a popular sport."
]

query = "What is artificial intelligence?"

document_embeddings = model.encode(documents)
query_embedding = model.encode([query])

scores = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

print("Query:", query)
print("\nSimilarity Scores:\n")

for i, score in enumerate(scores):
    print(documents[i])
    print("Score:", round(score, 4))
    print()

best_index = scores.argmax()

print("Most Similar Document:")
print(documents[best_index])
