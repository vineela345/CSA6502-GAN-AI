import faiss
from sentence_transformers import SentenceTransformer

documents = [
    ("AI Document", "Artificial intelligence enables machines to perform intelligent tasks."),
    ("Machine Learning Document", "Machine learning allows computers to learn from data."),
    ("Deep Learning Document", "Deep learning uses neural networks with multiple layers."),
    ("NLP Document", "Natural language processing helps computers understand human language."),
    ("Robotics Document", "Robotics combines artificial intelligence with machines to perform tasks.")
]

texts = [item[1] for item in documents]
names = [item[0] for item in documents]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(texts).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

print("Multiple Document AI Assistant")
print("Type exit to stop.")

while True:

    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    query_embedding = model.encode(
        [question]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        2
    )

    print("\nTop Results:")

    for rank, i in enumerate(indices[0], 1):

        print("\nResult", rank)
        print("Source:", names[i])
        print("Answer:", texts[i])
