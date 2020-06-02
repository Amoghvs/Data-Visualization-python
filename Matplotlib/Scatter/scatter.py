# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:49:05 2020

@author: Dell
"""



import pandas as pd
from matplotlib import pyplot as plt

"""1"""


x=[1,2,4,5,6,7,8,4,2,5,3,2]
y=[2,6,2,5,2,1,5,7,4,2,4,6]


plt.scatter(x,y,s=50,c='green',marker='X',edgecolor='black',linewidth=1,alpha=0.75)


"""2"""
plt.style.use('seaborn')

data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio, cmap='summer',
            edgecolor='black', linewidth=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
