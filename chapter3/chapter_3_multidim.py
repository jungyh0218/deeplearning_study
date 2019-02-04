import numpy as np

A = np.array([1, 2, 3, 4])
print(np.ndim(A))
print(A.shape)

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([7, 8])
print(np.dot(A, B))

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])
A1 = np.dot(X, W1) + b1
print(A1)
def sigmoid(x):
    return 1/(1+np.exp(-x))
Z1 = sigmoid(A1)
print(Z1)
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
print(Z1.shape, W2.shape)
Z2 = sigmoid(np.dot(Z1, W2) + b2)
print(Z2)

def identity_function(x):
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])
print(Z2.shape, W3.shape)
Y = identity_function(np.dot(Z2, W3) + b3)
print(Y)

