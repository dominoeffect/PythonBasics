import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from pandas import Series,DataFrame



x = np.linspace(0,2*np.pi,100) # 设置横轴变量，从0到2*pi，均分为100份

y = np.sin(x) # 因变量取值

plt.plot(x,y,'b*',label='aaa') # 'b*'表示蓝色*状线，label是指定义图例

plt.plot(x*2,y,'r--',label='bbb') # 'r--'表示红色虚线，

plt.xlabel('this is x') # 设置横轴标签

plt.ylabel('this is y') # 设置纵轴标签

plt.title('this is title') # 设置标题

plt.legend() # 显示上面定义的图例

plt.show() # 展示图像


plt.subplot(2,1,1) # 子图，（2,1,1）代表，创建2*1的画布，并且定位于画布1 ；等效于plt.subplot(211)，即去掉逗号

a = plt.subplots() # 返回两个对象 figure ax

figure,ax = plt.subplots()

ax.plot([1,2,3,4,5])

plt.show() # 显示图像

# subplots可以传入参数，几行几列

figure,ax = plt.subplots(2,2)

# figure 显示画布，分成2*2的

ax[0][0].plot(x,y)

ax[0][1].plot(x*2,y*2) # 可以分别绘图





