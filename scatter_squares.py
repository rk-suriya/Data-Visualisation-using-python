import matplotlib.pyplot as plt


values = range(1, 1001)
squares = [i**2 for i in values]

# Using Built-in Styles
# Check available styles
# To check use the following command in the terminal
# plt.style.available

# fig - figure instance
# ax - axes instance

fig, ax = plt.subplots()
# ax.scatter using scatter plot
# ax.scatter(x, y, s=100) s is the size of the dots
# for single point
# ax.scatter(3, 9, s=100)
# for multiple points
# custom color
# ax.scatter(values, squares, s=100, color=(0, 0.8, 0))
# color map - cmap parameter is used to set the color map of the plot
ax.scatter(values, squares, s=10, c=squares, cmap=plt.cm.Reds)
# set_title parameters are [title, fontsize]
ax.set_title("SQUARES", fontsize=20)
ax.set_xlabel("Values", fontsize=16)
ax.set_ylabel("Squares Values", fontsize=16)
# ax.axis to set the range of the axis
# parameters are [xmin, xmax, ymin, ymax]
ax.axis([0, 1100, 0, 1_100_000])
# tick labels
ax.ticklabel_format(style='plain')
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
