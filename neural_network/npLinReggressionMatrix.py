# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:12:07 2020

@author: gmpoc
Найдите оптимальные коэффициенты для построения линейной регрессии.

На вход вашему решению будет подано название csv-файла, из которого нужно
считать данные. Пример можно посмотреть
https://stepic.org/media/attachments/lesson/16462/boston_houses.csv

"""

import numpy as np
import urllib

fname = input("Please enter url to download or leave empty to open local:\n")
try:
    csvfile = None
    if fname:
        urlfile = urllib.request.urlopen(fname)
        csvfile = open('boston_houses.csv', 'w+t', encoding='UTF-8')
        csvfile.write(urlfile.read().decode('utf-8'))
    else:
        csvfile = open('boston_houses.csv', 'r+t', encoding='UTF-8')
    csvfile.seek(0)
    data = np.loadtxt(csvfile, delimiter=',', skiprows=1)  # load data
    X = data[:, 1:]
    Y = data[:, :1]
    X = np.hstack((np.ones((data.shape[0], 1)), X))
    b = np.linalg.inv(X.T@X)@X.T@Y
    print(*b.flatten())
except FileNotFoundError as ferr:
    print(ferr)
finally:
    if csvfile:
        csvfile.close()
