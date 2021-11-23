"""
Source: https://github.com/ehmatthes/pcc_2e
"""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
ax.scatter(rw.x_values, rw.y_values,
    c=range(len(rw.x_values)),
    cmap=plt.cm.Blues,
    edgecolors='none',
    s=15
)

plt.show()

