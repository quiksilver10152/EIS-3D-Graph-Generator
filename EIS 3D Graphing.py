# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 13:02:48 2024

@author: quiks
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection# New import
from matplotlib import animation
import matplotlib.ticker as mticker
import time
import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d
import pandas as pd
import math

def init():
    return fig,

def animate(i):
    ax.view_init(elev=30., azim=i*2)
    return fig,

def log_tick_formatter(val, pos=None):
    return (10**val)
nameList = ['Trial 1' , 'Trial 2', 'Trial 3', 'Trial 4', 'Trial 5']
#nameList = ['JADES', 'Sunflower', 'Pegasus', 'Aquila', 'Orion', 'Butterfly', 'Omega', 'Wishing Well', 'Beehive',
#            'Eye of God', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'JADES']
colorList = ['red', 'orange', 'green', 'blue', 'darkviolet']
#colorList = ['red', 'tomato', 'orangered', 'orange', 'gold', 'yellow', 'greenyellow', 'springgreen', 'aqua',
#             'darkturquoise', 'skyblue', 'cornflowerblue', 'blue', 'slateblue', 'blueviolet', 'darkviolet', 'fuchsia', 'mediumvioletred', 'red']
filePath = r"C:\Users\quiks\Downloads\EIS.xlsx"
eisData = pd.read_excel(filePath)
eis = eisData.to_numpy()

fig, ax = plt.subplots()
fig = plt.figure(figsize=(8, 6), dpi=80)
y = np.array(eis[1:,0], dtype=np.float64)
null = [0]*len(y)
nyq = [100000]*len(y)
h = 0.0
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('Z real')
ax.set_ylabel('LOG Frequency [Hz]')
ax.set_zlabel('Z imaginary')
ax.set_zlim(6000, -500000)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(log_tick_formatter))

for i in range(5):
    v = []
    color = colorList[math.ceil(i)] 
    name = nameList[math.ceil(i)]
    x = np.array(eis[1:,2*i + 1], dtype=np.float64)    
    z = np.array(eis[1:,2*i + 2], dtype=np.float64)
    for k in range(0, len(x) - 1):
        xs = [x[k], x[k+1], x[k+1], x[k]]
        ys = [np.log10(y[k]), np.log10(y[k+1]), np.log10(y[k+1]), np.log10(y[k])]
        zs = [z[k], z[k+1], h, h]
        v.append(list(zip(xs, ys, zs))) 
    poly3dCollection = Poly3DCollection(v, facecolors=color, alpha=0.5)
    lineCollection = Line3DCollection(v, colors=color, label=name,  linewidths=0.5, alpha=1)
    ax.add_collection3d(poly3dCollection)
    ax.add_collection3d(lineCollection)
         
    ax.plot(null, np.log10(y), z, color=color, linewidth=0.5)
    ax.plot(x, np.log10(nyq), z, color=color, linewidth=0.5)
    ax.plot(x, np.log10(y), null, color=color, linewidth=0.5)
    ax.plot(x, np.log10(y), z, color=color, linewidth=0.5)
    ax.legend()    
# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=36*5, interval=140, blit=True)
plt.show()

# Save
anim.save('animation.gif', writer='imagemagick', fps=8)