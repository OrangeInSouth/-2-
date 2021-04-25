"""
This code aims to resolve a 2-dimension optimization problem:
        min f(x) = x_1 - x_2 + 2 * (x_1)^2 + 2 * x_1 * x_2 + (x_2)^2
    initial x = (0, 0)
    threshold = 10^(-6)

Author: Yichong Huang (黄毅翀)
Student Code: 20S103272
"""
import torch

# target function
def loss(x):
    return x[0] - x[1] + 2 * x[0] ** 2 + 2 * x[0] * x[1] + x[1] ** 2


# get grad
def get_grad(x):
    x = x.detach()
    x.requires_grad = True
    y = loss(x)
    y.backward()
    grad = x.grad
    x.grad = None
    return grad

# get optimized step size
# 这一步暂时没想到通用的写法
def get_optimized_step_size(x, d):
    optimized_ste_size = (d[0] + d[1]) * (1 - 2 * x[0] - 2 * x[1]) - 2 * d[0] * (x[0] + 1)
    optimized_ste_size /= (d[0] + d[1])**2 + 2 * d[0]**2
    return optimized_ste_size


initial_point = torch.tensor([0., 0.], requires_grad=True)
x = [initial_point]
k = 0
grad = [get_grad(x[0])]
d = [grad[0] * (-1)]
threshold = 10 ** (-6)
beta = [None]
step_size = [get_optimized_step_size(x[0], d[0])]

# format the output
output_format = "| %3s | %25s | %25s | %25s | %10s | %8s |"
print(output_format % ("k", "x", "grad", "d", chr(946), chr(955)))

while (grad[-1] * grad[-1]).sum().sqrt() > threshold:
    print(output_format % (k+1,
                           [round(i, 6) for i in x[-1].tolist()],
                           [round(i, 6) for i in grad[-1].tolist()],
                           [round(i, 6) for i in d[-1].tolist()],
                           round(beta[-1].item(), 6) if beta[-1] is not None else "",
                           round(step_size[-1].item(), 6)))

    k += 1

    new_x = x[-1] + step_size[-1] * d[-1]
    x.append(new_x)

    new_grad = get_grad(new_x)
    grad.append(new_grad)

    new_beta = (grad[-1] * grad[-1]).sum() / (grad[-2] * grad[-2]).sum()
    beta.append(new_beta)

    new_d = grad[-1]*(-1) + new_beta * d[-1]
    d.append(new_d)

    new_step_size = get_optimized_step_size(new_x, new_d)
    step_size.append(new_step_size)