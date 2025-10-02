import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
grid=plt.GridSpec(2,2,width_ratios=[3,1], height_ratios=[1,3])

ax1 = fig.add_subplot(grid[0])
ax1.plot(np.random.rand(50))

ax2 = fig.add_subplot(grid[1])
ax2.plot(np.random.rand(50))

ax3 = fig.add_subplot(grid[2])
ax3.plot(np.random.rand(50))

ax4 = fig.add_subplot(grid[3])
ax4.plot(np.random.rand(50))




plt.show()