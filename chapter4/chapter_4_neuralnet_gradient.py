import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7 #-INF(NaN)으로 가는 것을 방지하기 위해 작은 값 더함
    print(y)
    print(np.log(y+delta))
    print(t*np.log(y+delta))
    return -np.sum(t*np.log(y + delta))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp = np.sum(exp_a)
    return exp_a/sum_exp

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)
    
    def predict(self, x):
        return np.dot(x, self.W)
    
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        print('y: ', y)
        loss = cross_entropy_error(y, t)

        return loss


net = simpleNet()
print('initial weight: ', net.W)
x = np.array([0.6, 0.9])
p = net.predict(x)
print('p: ', p)
t = np.array([0, 0, 1])
print('loss: ', net.loss(x, t))