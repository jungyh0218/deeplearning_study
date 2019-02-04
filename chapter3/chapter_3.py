#chapter3 
#activation function
import numpy as np

def step_function(x):
    y = x > 0
    return y.astype(np.int)

print(step_function(np.array([-1, 2, -0.3, 0.9])))

def sigmoid(x):
    return 1/(1+np.exp(-x))

print(sigmoid(np.array([-1, 2, -0.3, 0.9])))

def relu(x):
    return np.maximum(0, x)

print(relu(np.array([0.7, -2.3, 3.2, 1.9, -6])))