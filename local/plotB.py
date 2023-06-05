import matplotlib.pyplot as plt

def plotfigure(plot_fn, fig, background_col = 'xkcd:black', face_col = (0.06,0.06,0.06)):
    """
    Plot Figure using plt plot functions.

    Customize different background and face-colors of the plot.

    Parameters:
    plot_fn (func): The plot functions with necessary arguments as a lamdda function.
    fig : The Figure object by plt.figure()
    background_col: The background color of the plot. Supports matlplotlib colors
    face_col: The face color of the plot. Supports matlplotlib colors


    Returns:
    void 

    """
    fig.patch.set_facecolor(background_col)
    plot_fn()
    ax = plt.gca()
    ax.set_facecolor(face_col)
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.grid(alpha=0.1)
    ax.title.set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')


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

# Plot ROC curves
# plotfigure(lambda: plt.plot(fpr1, tpr1, linestyle='--',color='orange', label='Logistic Regression'), fig)
# plotfigure(lambda: plt.plot(fpr2, tpr2, linestyle='--',color='green', label='KNN'), fig)
# plotfigure(lambda: plt.plot(p_fpr, p_tpr, linestyle='-', color='blue'), fig)

# # Title
# plt.title('ROC curve')

# # X label
# plt.xlabel('False Positive Rate')

# # Y label
# plt.ylabel('True Positive rate')

# plt.legend(loc='best',labelcolor='white')
plt.savefig('ROC',dpi=300)

plt.show()
