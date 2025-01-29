import plotly.express as px
from die import Die

die_1 = Die()
die_2 = Die(10)

# Roll the dice and store the results in a list
results = []

for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Frequencies
frequencies = []

max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results + 1)  # [2.....16]

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)  # dtick means distance between ticks
fig.show()

# Save the results to a file
filename = 'dice_visual_d6d10.html'
fig.write_html(filename)
print(f"Results saved to {filename}.")

# save as a png
filename = 'dice_visual_d6d10.png'
fig.write_image(filename)
