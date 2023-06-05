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



def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print(f'# This is a polynomial of order {o}.')
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y

x = np.linspace(0, 9, 10)
coeffs = [1, 2, 3, 4, 5]
plt.plot(x, PolyCoefficients(x, coeffs), color='xkcd:white')

plt.show()