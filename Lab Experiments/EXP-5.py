from sklearn.metrics.pairwise import cosine_similarity

v1 = [[1, 2, 3, 4]]
v2 = [[2, 3, 4, 5]]

print("Vector 1")
print(v1)

print("Vector 2")
print(v2)

result = cosine_similarity(v1, v2)

print("Cosine Similarity")
print(result)

if result[0][0] > 0.8:
    print("The two documents are highly similar.")
else:
    print("The two documents are not similar.")
