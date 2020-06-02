# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:34:11 2020

@author: Dell
"""


import pandas as pd
import matplotlib.pyplot as plt
import statistics

ages=[18,12,23,28,35,23,13]
bins=[10,20,30,40,50]

plt.hist(ages,bins=bins,edgecolor='black')


bins=[20,30,40]

plt.hist(ages,bins=bins,edgecolor='black')


"""2"""


data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age=statistics.median(ages)
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
