import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

x_majortick = 0.2
x_minortick = 0.05
y_majortick = 0.2
y_minortick = 0.05

data = np.loadtxt('data.txt')
settings = np.loadtxt('settings.txt')

volts = data * settings[0]
time = np.arange(len(data)) * settings[1]

fig, ax = plt.subplots()

ax.plot(time, volts, color='pink', linestyle='-', marker='o', 
markersize=5, markerfacecolor='pink', label='Voltage')

ax.set_xlim(np.min(time), np.max(time))
ax.set_ylim(np.min(volts), np.max(volts))

ax.set_xlabel('Time (sec)')
ax.set_ylabel('Voltage (vol)')

ax.set_title('Voltage and Time of charging and uncharging capasitor')

ax.xaxis.set_major_locator(MultipleLocator(x_majortick))
ax.xaxis.set_minor_locator(MultipleLocator(x_minortick))
ax.yaxis.set_major_locator(MultipleLocator(y_majortick))
ax.yaxis.set_minor_locator(MultipleLocator(y_minortick))

ax.grid(True, linestyle='--', linewidth=0.5, color='gray')
ax.grid(True, which='minor', linestyle='--', linewidth=0.5, color='gray')

ax.legend()

plt.savefig('graph.svg')

plt.show()

