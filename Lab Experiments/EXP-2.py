import numpy as np

a = np.array([[2, 4], [6, 8]])
b = np.array([[1, 3], [5, 7]])

print("Matrix A")
print(a)

print("Matrix B")
print(b)

c = a + b
print("Addition")
print(c)

d = a - b
print("Subtraction")
print(d)

e = np.dot(a, b)
print("Multiplication")
print(e)

print("Transpose of A")
print(a.T)

print("Transpose of B")
print(b.T)

print("Inverse of A")
print(np.linalg.inv(a))

print("Inverse of B")
print(np.linalg.inv(b))
