# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:43:10 2017

@author: cemalper
"""

import csv
import matplotlib.pyplot as plt
with open("workout_updates.csv",'rb') as csvfile:
    data = csv.reader(csvfile, delimiter = ';')
    data_list = [rows for rows in data]
    data_list = data_list[1:]
    secs = [float(data_list_elem[3]) for data_list_elem in data_list]
    hr = [float(data_list_elem[8]) if data_list_elem[8]!='' else 0 for data_list_elem in data_list]
    plt.figure()
    plt.plot(secs,hr)
    plt.show()