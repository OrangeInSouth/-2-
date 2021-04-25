"""
This code aims to resolve one-dimension optimization problem
using different kinds of algorithm:
    1. Golden Section
    2. Fibonacci
    3. Dichotomy
    4. Dichotomous

Author: Yichong Huang (黄毅翀)
Student Code: 20S103272
"""
import math
import torch

def target(x):
    problem_a = 2 * x**2 - x - 1
    problem_b = 3 * x**2 - 21.6 * x - 1
    return problem_b


threshold = 0.06
init_span = [-1., 1.]

def gold_section():
    """
     Golden Section Algorithm
    """
    print("Golden Section Algorithm")

    gold_point = (math.sqrt(5) - 1) / 2

    def get_sub_golden_span(left, right):
        """
        calculate sub-span by gold split point
        """
        new_left = left + (1 - gold_point) * (right - left)
        new_right = left + gold_point * (right - left)
        return new_left, new_right

    a = init_span[0]
    b = init_span[1]
    c, d = get_sub_golden_span(a, b)

    k = 0
    mat = "| %3s | %10s | %10s | %10s | %10s |"
    print(mat % ("k", "a", "c", "d", "b"))

    while b - a > threshold:
        print(mat % (k, round(a, 6), round(c, 6), round(d, 6), round(b, 6)))

        y_c = target(c)
        y_d = target(d)

        if y_c > y_d:
            a = c
            c = d
            d = a + gold_point * (b - a)
        elif y_c < y_d:
            b = d
            d = c
            c = a + (1 - gold_point) * (b - a)
        else:
            a = c
            b = d
            c, d = get_sub_golden_span(a, b)

        k += 1

    print("resolution:", (a + b)/2)


def fibonacci():
    """
    fibonacci algorithm
    """
    a = init_span[0]
    b = init_span[1]
    const = 0.01

    # calculate fibonacci list: [F_0, F_1, ..., F_{N+1}]
    F = [1, 1]
    while 1 / F[-1] > threshold:
        F.append(F[-2] + F[-1])
    N = len(F) - 2
    c = a + (b - a) * (F[-3]/F[-1] - const)
    d = a + (b - a) * (F[-2]/F[-1] - const)

    mat = "| %3s | %10s | %10s | %10s | %10s |"
    print(mat % ("k", "a", "c", "d", "b"))

    for k in range(1, N+1):
        print(mat % (k, round(a, 6), round(c, 6), round(d, 6), round(b, 6)))

        if target(c) > target(d):
            a = c
            c = d
            d = a + (b - a) * (F[N-k]/F[N-k+1] + const)
        else:
            b = d
            d = c
            c = a + (b - a) * (F[N-k-1]/F[N-k+1] - const)

    print("resolution:", (a+b)/2)



def dichotomy():
    """
    dichotomy algorithm
    """
    a = torch.tensor([init_span[0]])
    b = torch.tensor([init_span[1]])

    k = 0
    mat = "| %3s | %10s | %10s | %10s | %10s |"
    print(mat % ("k", "a", "midpoint", "b", "grad"))
    while b - a > threshold:
        midpoint = (a + b) / 2
        midpoint.requires_grad=True
        y = target(midpoint)
        y.backward()
        grad = midpoint.grad

        print(mat % (k, round(a.item(), 6), round(midpoint.item(), 6), round(b.item(), 6), round(grad.item(), 6)))

        if grad > 0:
            b = midpoint.detach()
        elif grad < 0:
            a = midpoint.detach()
        else:
            break
        k += 1

    print("resolution:", ((a + b) / 2).item())

def dichotomous():
    """
     Dichotomous
    """
    print("Dichotomous")

    sigma=threshold/2

    a = init_span[0]
    b = init_span[1]
    c = (a + b) / 2 - sigma / 2
    d = (a + b) / 2 + sigma / 2

    k = 0
    mat = "| %3s | %10s | %10s | %10s | %10s |"
    print(mat % ("k", "a", "c", "d", "b"))

    while b - a > threshold:
        print(mat % (k, round(a, 6), round(c, 6), round(d, 6), round(b, 6)))

        y_c = target(c)
        y_d = target(d)

        if y_c >= y_d:
            a = c
        else:
            b = d

        c = (a + b) / 2 - sigma / 2
        d = (a + b) / 2 + sigma / 2

        k += 1

    print("resolution:", (a + b)/2)

# gold_section()
# dichotomy()
# fibonacci()
dichotomous()