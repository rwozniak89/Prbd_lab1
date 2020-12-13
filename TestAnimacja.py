# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:22:29 2019


"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x = np.linspace(0,np.pi, 100)

fig = plt.figure()

line,  = plt.plot(x, np.zeros_like(x))

plt.xlim([0, np.pi])
plt.ylim([-1, 1])

def update_plot(frame):
    a  = float(frame)/100
    line.set_ydata(np.sin(a*x))

anim = FuncAnimation(fig, update_plot, frames=300, interval=1, repeat=False)

plt.show()
