"""
This code aims at implementing the RSMprop algorithm

Author: Yichong Huang (黄毅翀)
Student Code: 20S103272
"""

import numpy as np


def f(x):
    return 2 * x ** 2 - x - 1


def h(x):
    return 4 * x - 1


x = 0  # 初始点（初始横坐标）
step = 0.1  # （步长）

f_change = 1
f_current = f(x)
count = 0  #
n_t = 0
epsi = 1e-10
gamma = 0.5
i = 0

while f_change > 1e-5:
    n_t = gamma * n_t + (1 - gamma) * h(x) ** 2
    x = x - step / ((n_t + epsi) ** 0.5) * h(x)
    f_new = f(x)
    f_change = np.abs(f_new - f_current)
    f_current = f_new
    count += 1
print('Iteration times：%d' % count, '\n''optimal resolution=', x, '\n''optimal value=', f_current)
