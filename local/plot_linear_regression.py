import matplotlib.pyplot as plt
import numpy
from typing import Sequence, Union
from scipy import stats

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


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y, color='xkcd:white')
plt.plot(x, mymodel)
plt.show()