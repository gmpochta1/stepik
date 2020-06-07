# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:07:14 2020

@author: gmpoc
У нас есть набор данных: знания о длине тормозного пути и скорости для
трёх автомобилей. Напишите через запятую оценки коэффициентов линейной
регрессии D на V, т.е. β^0 \hat{\beta}_0 β^​0​, β^1 \hat{\beta}_1 β^​1​
для модели D=β0+β1V+ε D=\beta_0+\beta_1 V+\varepsilon D=β0​+β1​V+ε
с точностью до трёх знаков после точки.
"""

import numpy as np

ylist = [10, 7, 12]
xlist = [60, 50, 75]
X = np.array([[1, x] for x in xlist])
Y = np.array([[y] for y in ylist])
print(X)
print(Y)
b = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
print(*map(lambda x: round(x[0], 3), b))
