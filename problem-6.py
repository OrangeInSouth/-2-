"""
This code aims at implementing the BFGS algorithm

Author: Yichong Huang (黄毅翀)
Student Code: 20S103272
"""
import numpy as np
import numpy.linalg as lg

df = lambda x: np.array([[2 * x[0][0] - 4], [8 * x[1][0] - 8]])
x = np.array([[0], [0]])
B = np.eye(2)
epsilon = 1e-5
s = 1000
while np.average(np.abs(s)) > epsilon:
    x1 = x - lg.inv(B).dot(df(x))
    s = x1 - x
    y = df(x1) - df(x)
    B = B - (B.dot(s).dot(s.T).dot(B.T)) / ((s.T).dot(B).dot(s)) + y.dot(y.T) / ((y.T).dot(s))
    x = x1

print(x)

