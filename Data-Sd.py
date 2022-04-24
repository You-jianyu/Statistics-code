#计算样本的标准差、方差
from sympy import *

X = [13.64,13.72,13.6,13.34,13.28,13.34,13.7,13.81,13.62,13.93]
n = len(X)
X_Sum = 0
mean1 = 0
for i in range(n):
    X_Sum += X[i]
    mean1 +=X[i]
X_Ave = X_Sum/n
S = 0
for i in range(n):
    S += (X[i] - X_Ave)**2
S = S/(n-1)
print('样本方差：',S)
print('样本标准差：',sqrt(S))
print('样本均值',mean1)