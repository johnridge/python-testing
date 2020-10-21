import math
import numpy as np
import scipy
from scipy import stats as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#from celluloid import Camera
import argparse

fig, axes = plt.subplots(2)
ax1 = axes[0]
ax2 = axes[1]
def sinc(x):
    return math.sin(np.pi * x) / (np.pi * x)
def rect(x):
    if abs(x) > 0.5:
        return 0
    if abs(x) == 0.5:
        return 0.5
    if abs(x) < 0.5:
        return 1
x_range = np.linspace(-100, 100, 50000)
a = [sinc(x) for x in x_range]
a = [complex(x) for x in a]
ax1.plot(x_range, [x.real for x in a], color = 'tab:red', label = 'Re')
ax1.plot(x_range, [x.imag for x in a], color = 'tab:blue', label = 'Im')
pulse = np.fft.ifft(a)
ax2.plot(x_range, [x.real for x in pulse], color = 'tab:red', label = 'Re')
ax2.plot(x_range, [x.imag for x in pulse], color = 'tab:blue', label = 'Im')
ax1.grid(axis='both', alpha=0.75, zorder = 0)
ax2.set(xlabel = '$\omega$')
ax2.set(ylabel = '$\hat{{f}}(\omega)$')
ax1.legend(loc = 'upper right')
ax2.grid(axis='both', alpha=0.75, zorder = 0)
ax1.set(xlabel = '$t$')
ax1.set(ylabel = '$f(t)$')
ax2.legend(loc = 'upper right')
plt.show()