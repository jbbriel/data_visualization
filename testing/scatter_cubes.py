import matplotlib.pyplot as plt
# Define Data
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# Make plot.
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set chart title and label axes.
ax.set_title('Cubed Numbers', fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis=('both'), which='minor', labelsize=24)

plt.show()