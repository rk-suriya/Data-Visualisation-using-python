from matplotlib import pyplot as plt
from random_walk import RandomWalk


# Generate multiple random walks
while True:
    # Make a random walk with 150_000 points
    rw = RandomWalk(150_000)
    rw.fill_walk()

    plt.style.use('classic')
    # Set the size of the plotting window
    fig, ax = plt.subplots(figsize=(10, 10))
    # fig, ax = plt.subplots()
    # Style the plot
    # c argument is the color of the points

    point_numbers = range(rw.number_points)
    ax.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
    ax.set_aspect('equal')

    # Ploting the starting point and the ending point
    ax.scatter(0, 0, c='green', edgecolors='red', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='green', s=100)
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
