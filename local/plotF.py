import matplotlib.pyplot as plt
import numpy as np
from typing import Sequence, Union

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





Number = Union[int, float, complex]

def polyval(coefficients: Sequence[Number], x: Sequence[Number]) -> np.ndarray:
    # expand dimensions to allow broadcasting (constant time + inexpensive)
    # axis=-1 allows for arbitrarily shaped x
    x = np.expand_dims(x, axis=-1)
    powers = x ** np.arange(len(coefficients))
    return powers @ coefficients

def polyplot(coefficients: Sequence[Number], x: Sequence[Number]) -> None:
    y = polyval(coefficients, x)
    plt.plot(x, y)

polyplot(np.array([0, 0, -1]), np.linspace(-10, 10, 210))

plt.show()