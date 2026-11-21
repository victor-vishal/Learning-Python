import numpy as np
import matplotlib.pyplot as plt
# pyplot is a module in matplotlib that provides a simple user friendly interface for plotting

# x = [2020, 2021, 2022, 2023, 2024, 2025]
# y = [60, 50, 35, 30, 70, 64]

# we use numpy arrays as it is more efficient
x = np.array([2020, 2021, 2022, 2023, 2024, 2025])
y = np.array([60, 50, 35, 30, 70, 64])

# we create a simple line plot using plot() functiion of pyplot module
plt.plot(x),y # Syntax: plt.plot(x-axis values, y-axis values)
# if only one parameter is passed, it is considererd as y axis and x axis is taken as the index of the y values

plt.show()