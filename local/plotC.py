import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

background_col = 'xkcd:black'
face_col = (0,0,0) #(0.06,0.06,0.06)

fig.patch.set_facecolor(background_col)
# plot_fn()
ax = plt.gca()
ax.set_facecolor(face_col)
ax.spines['bottom'].set_color('white')
# ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
# ax.spines['right'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
# ax.grid(alpha=0.1)
ax.title.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')



x = np.linspace(-np.pi, np.pi, 201)

plt.plot(x, np.sin(x), color='xkcd:white')

plt.show()