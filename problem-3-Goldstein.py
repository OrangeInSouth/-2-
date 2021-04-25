"""
This code aims at implementing Imprecise One-dimension Search:
    1. Goldstein
    2. Wolfe-Powell

Author: Yichong Huang (黄毅翀)
Student Code: 20S103272
"""

import torch

x = torch.tensor([-1., 1.])
d = torch.tensor([1., 1.])


def f(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2


def get_grad(x):
    x = x.detach()
    x.requires_grad = True
    y = f(x)
    y.backward()
    grad = x.grad.detach()
    return grad


def goldstein(x, d):
    p = 0.1
    zoom_in = 1.5
    zoom_out = 0.5
    step_size = 1
    phi_1 = f(x)
    phi_1_ = get_grad(x).dot(d)

    while f(x + step_size * phi_1_) > phi_1 + p * phi_1_ * step_size:
        step_size *= zoom_out
        print("updated step size:", step_size)

    while f(x + step_size * phi_1_) < phi_1 + (1 - p) * phi_1_ * step_size:
        step_size *= zoom_in
        print("updated step size:", step_size)
        while f(x + step_size * phi_1_) > phi_1 + p * phi_1_ * step_size:
            step_size *= zoom_out
            print("updated step size:", step_size)

    print("optimized step size:", step_size)

goldstein(x, d)