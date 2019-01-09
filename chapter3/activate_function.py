import numpy as np

def step_function(x):
    y = x > 0
    return y.astype(np.int)


def sigmoid(x):
    return 1/(1+np.exp(-x))


def relu(x):
    return np.maximum(0, x)

arr = np.array([-0.4, -0.3, 0.2, 2.3])
print(step_function(arr))
print(sigmoid(arr))
print(relu(arr))