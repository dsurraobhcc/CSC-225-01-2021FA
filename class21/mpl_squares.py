"""
Source: https://github.com/ehmatthes/pcc_2e
"""
import matplotlib.pyplot as plt

x_values = list(range(-6, 6))

fig, ax = plt.subplots()
ax.plot(x_values, [i**2 for i in x_values])
ax.plot(x_values, [i**3 for i in x_values])

ax.set_xlabel("Value")
ax.set_ylabel("Square/Cube of Value")
ax.set_title("Squares and Cubes")

plt.style.use('seaborn')

plt.show()
