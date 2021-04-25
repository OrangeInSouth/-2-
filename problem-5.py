"""
This code aims at implementing DFP algorithm to search the optimal resolution.

Author: Yichong Huang (黄毅翀)
Student Code: 20S103272
"""

import numpy as np
import numpy.linalg as lg

df = lambda x: np.array([[20 * x[0][0]], [2 * x[1][0]]])
x = np.array([[0.1], [1]])
H = np.eye(2)
epsilon = 1e-5
s = 1000

while np.average(np.abs(s)) > epsilon:
    x1 = x - lg.inv(H).dot(df(x))
    s = x1 - x
    y = df(x1) - df(x)
    tmp = y - H.dot(s)
    H = H + tmp.dot(tmp.T) / ((tmp.T).dot(s))
    x = x1

print(x)

