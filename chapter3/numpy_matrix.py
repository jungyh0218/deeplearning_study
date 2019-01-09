#Multiple dimension arrays and their calculations
#Using numpy

import numpy as np
import activate_function as activate

A = np.array([1, 2, 3, 4])
print(A)

print(np.ndim(A)) #1차원 배열, 4개 원소
print(A.shape)
print(A.shape[0])

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(np.ndim(B)) #2차원 배열
print(B.shape) #3행 2열

#행렬 합
X = np.array([[1, 0, 3], [4, 3, 2], [4, 2, 0]])
Y = np.array([[5, 3, 2], [2, 8, 1], [1, 6, 2]])
print(X+Y)


#행렬 곱
print(X, Y)
print(np.dot(X, Y))

#신경망 쌓기
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])

print(X.shape)
print(W1.shape)
print(b.shape)

A1 = np.dot(X, W1) + b
Z1 = activate.sigmoid(A1)

print(A1)
print(Z1) # output
