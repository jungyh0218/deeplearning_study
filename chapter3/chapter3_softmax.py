import numpy as np

def softmax_old(a):
    exp_a = np.exp(a)
    sum_exp = np.sum(exp_a)
    return exp_a / sum_exp

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp = np.sum(exp_a)
    return exp_a / sum_exp

a = np.array([1010, 1000, 990])
print(softmax_old(a))
print(softmax(a))
