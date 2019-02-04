import numpy as np

def numerical_diff(f, x):
    h = 1e-4 #0.0001
    return (f(x+h) - f(x-h))/(2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))

def function_tmp1(x0):
    return x0**2 + 4.0**2.0




print(numerical_diff(function_tmp1, 3.0))

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    
    for idx in range(0, x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val+h
        fxh1 = f(x)
        x[idx] = tmp_val-h
        fxh2 = f(x)

        grad[idx] = (fxh1-fxh2)/(2*h)
        x[idx] = tmp_val
    return grad

def function_2(x):
    return x[0]**2 + x[1]**2

print(numerical_gradient(function_2, np.array([3.0, 4.0])))