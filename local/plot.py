import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['axes.edgecolor'] = '#ffffff'

fig = plt.figure()
fig.set_facecolor('xkcd:black')

plt.rcParams['axes.facecolor'] = 'black'

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
