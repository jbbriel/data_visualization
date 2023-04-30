from die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die(6)


results = [die_1.roll() + die_2.roll() for roll_num in range(10000)]


# Analyze the results
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_results+1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results
x_values = list(range(1, max_results+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of rolling two D6 Die 10000 times',
                      xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')