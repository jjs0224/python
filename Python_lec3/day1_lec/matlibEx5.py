import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('sample.txt')
print(data)

# plt.plot(data[:,0], data[:,1])
# plt.show()

for column in data.T:
    plt.plot(data[:,0], column)
plt.show()
