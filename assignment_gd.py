# -*- coding: utf-8 -*-
"""assignment GD.ipynb
"""

import numpy as np
from numpy.linalg import norm

def gradient_descent(fderiv, initial_start, step_size=0.001, precision=0.00001, max_iter=1000):
    cur_start = np.array(initial_start, dtype=float)
    last_start = cur_start + 100 * precision
    start_list = [cur_start]

    iter_count = 0
    while norm(cur_start - last_start) > precision and iter_count < max_iter:
        last_start = cur_start.copy()
        gradient = fderiv(cur_start)
        cur_start -= step_size * gradient
        start_list.append(cur_start)
        iter_count += 1

    return cur_start

def trial1():
    def fderiv(state):
        x, y = state[0], state[1]
        return np.array([6 * (x + 2), 2 * (y - 1)])

    initial_state = np.array([-5.0, 2.5])
    minimum = gradient_descent(fderiv, initial_state)
    print(f'Trial 1 - Minimum found at state = {minimum}')

def trial2():
    def fderiv(state):
        x, y = state[0], state[1]
        return np.array([4 * (x - y), 4 * (y ** 3 - x)])

    initial_state = np.array([2.5, 1.9])
    minimum = gradient_descent(fderiv, initial_state)
    print(f'Trial 2 - Minimum found at state = {minimum}')

if __name__ == '__main__':
    trial1()
    trial2()

import numpy as np
from numpy.linalg import norm

def gradient_descent(fderiv, inital_start, step_size = 0.001, precision = 0.00001, max_iter = 1000):
    cur_start = np.array(inital_start)
    last_start = cur_start + 100 * precision    # something different
    start_list = [cur_start]

    iter = 0
    while norm(cur_start - last_start) > precision and iter < max_iter:
        print(cur_start)
        last_start = cur_start.copy()     # must copy

        gradient = fderiv(cur_start)
        cur_start -= gradient * step_size   # move in opposite direction

        start_list.append(cur_start)
        iter += 1

    return cur_start


def trial1():
    def f(x, y):
        return 3 * (x + 2) ** 2 + (y - 1) ** 2       # 3(x + 2)² + (y - 1)²

    def fderiv_dx(x, y):
        return 6 * (x + 2)

    def fderiv_dy(x, y):
        return 2 * (y - 1)

    def fderiv(state):
        x, y = state[0], state[1]
        return np.array([fderiv_dx(x, y), fderiv_dy(x, y)])

    func_name = 'Gradient Descent on 2x² - 4x y + y⁴ + 2'

    inital_x, inital_y = -5.0, 2.5
    state = np.array([inital_x, inital_y])
    mn = gradient_descent(fderiv, state)
    print(f'The minimum found at state = {mn}')
    # The minimum z exists at (x,y) = [-2.00730307  1.20259678]


def trial2():
    def f(x, y):
        return 2 * x ** 2 + 4 * x * y + y ** 4 + 2       # 2x² - 4x y + y⁴ + 2

    def fderiv_dx(x, y):
        return 4 * (x-y)

    def fderiv_dy(x, y):
        return 4 * (y **3 - x)

    def fderiv(state):
        x, y = state[0], state[1]
        return np.array([fderiv_dx(x, y), fderiv_dy(x, y)])

    func_name = 'Gradient Descent on 2x² - 4x y + y⁴ + 2'

    inital_x, inital_y = 2.5, 1.9
    state = np.array([inital_x, inital_y])
    mn = gradient_descent(fderiv, state)
    print(f'The minimum found at state = {mn}')
    # The minimum z exists at (x,y) = [1.11270719 1.04406617]

if __name__ == '__main__':
    #trial1()
    trial2()

import numpy as np
from numpy.linalg import norm

# Instead of trying to import, directly define the gradient_descent function here
def gradient_descent(fderiv, initial_start, step_size=0.001, precision=0.00001, max_iter=1000):
    cur_start = np.array(initial_start, dtype=float)
    last_start = cur_start + 100 * precision
    start_list = [cur_start]

    iter_count = 0
    while norm(cur_start - last_start) > precision and iter_count < max_iter:
        last_start = cur_start.copy()
        gradient = fderiv(cur_start)
        cur_start -= step_size * gradient
        start_list.append(cur_start)
        iter_count += 1

    return cur_start


if __name__ == '__main__':

    def fun(x, y, z):
        return np.sin(x) + np.cos(y) + np.sin(z)

    def fderiv_dx(x):
        return np.cos(x)

    def fderiv_dy(y):
        return -np.sin(y)

    def fderiv_dz(z):
        return np.cos(z)

    def fderiv(state):
        derv = [fderiv_dx, fderiv_dy, fderiv_dz]
        gradients = []
        for dfunc, var in zip(derv, state):
            gradients.append(dfunc(var))
        return np.array(gradients)

    inital_x, inital_y, intial_z = 1, 2, 3.5
    state = np.array([inital_x, inital_y, intial_z])
    mn = gradient_descent(fderiv, state)
    mn_output = fun(mn[0], mn[1], mn[2])

    print(f'Initial start at {state} ends at point: {mn} with minimum value {mn_output}')
    # Initial start at [1.  2.  3.5] ends at point: [0.22457445 2.67782963 4.21311734] with minimum value -1.5496155799445872
    # Initial start at [ -7.5 -15.9 -12.1] ends at point: [ -7.72263523 -15.77876279 -13.06066696] with minimum value -2.463293552679835
