#perceptron codes without using numpy library

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w1
    if tmp < theta:
        return 0
    else:
        return 1

print('AND')
print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))

def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.3
    tmp = x1*w1 + x2*w1
    if tmp < theta:
        return 0
    else:
        return 1

print('OR')
print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))