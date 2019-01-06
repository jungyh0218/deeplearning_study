#NAND or NOR로 모든 가능한 논리 회로를 구성할 수 있습니다.
#실제로 상업적 용도의 flash memory 를 nand/nor 회로로만 구성합니다.
#NOR 에 비해 적은 회로로도 구성할 수 있어서 몇 가지 단점에도 불구하고 nand flash memory가 주류

import numpy as np

#nand 회로
def NAND(x1, x2):
    x = np.array([x1, x2])
    weight = np.array([-0.5, -0.5])
    bias = 0.7
    tmp = np.sum(x*weight) + bias
    if tmp <= 0:
        return 0
    else:
        return 1


#NAND로 or 회로 구성
def OR_NAND(x1, x2):
    s1 = NAND(x1, x1)
    s2 = NAND(x2, x2)
    y = NAND(s1, s2)
    return y
print("NAND to OR")
print(OR_NAND(0, 0))
print(OR_NAND(0, 1))
print(OR_NAND(1, 0))
print(OR_NAND(1, 1))


#nand로 and 회로 구성
def AND_NAND(x1, x2):
    s1 = NAND(x1, x2)
    y = NAND(s1, s1)
    return y

print("NAND to AND")
print(AND_NAND(0, 0))
print(AND_NAND(0, 1))
print(AND_NAND(1, 0))
print(AND_NAND(1, 1))


#nand로 not 회로 구성
def NOT_NAND(x):
    return NAND(x, x)

print("NAND to NOT")
print(NOT_NAND(0))
print(NOT_NAND(1))