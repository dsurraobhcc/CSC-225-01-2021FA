"""
Source: https://github.com/ehmatthes/pcc_2e
"""

from matplotlib import scale
import matplotlib.pyplot as plt

x_values = range(25)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(
    x_values,   # positional arguments
    y_values, 
    s=y_values,
    c=y_values, # keyword arguments
)

plt.show()