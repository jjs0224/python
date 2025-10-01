import matplotlib.pyplot as plt
import numpy as np


plt.subplot(221)
plt.title('axes1')
plt.plot(np.random.randn(50))

plt.subplot(222)
plt.title('axes2')
plt.plot(np.random.randn(50))

plt.subplot(223)
plt.title('axes3')
plt.plot(np.random.randn(50))

plt.subplot(224) #(2,2,4) ,생략가능
plt.title('axes4')
plt.plot(np.random.randn(50))

plt.suptitle('2 x 2 graph plot practice',
             fontsize=16)
plt.tight_layout()
plt.show()