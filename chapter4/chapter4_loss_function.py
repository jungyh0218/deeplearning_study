import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

t = np.array([0,0,1,0,0,0,0,0,0,0])
#y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
y = np.array([0.1, 0.05, 0.6, 0.0, 0.05])

#print(mean_squared_error(y, t))

def cross_entropy_error(y, t):
    delta = 1e-7 #-INF(NaN)으로 가는 것을 방지하기 위해 작은 값 더함
    return -np.sum(t*np.log(y + delta))

#print(cross_entropy_error(y, t))

def cross_entropy_error_label(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    batch_size = 5
    print('batch_size=', batch_size)
    print(y[np.arange(batch_size)])
    return 1#-np.sum(np.log(y[np.arange(batch_size), t]+1e-7))/batch_size

print(cross_entropy_error_label(y, np.array([2,7,0,9,4])))