# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:49:19 2020

@author: Dell
"""


import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data.csv")

ages=data['Age']
dev_salaries=data['All_Devs']
py_salaries=data['Python']
js_salaries=data['JavaScript']


plt.plot(ages, py_salaries, label='Python')
plt.plot(ages, js_salaries, label='JavaScript')

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()


"""2"""
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
