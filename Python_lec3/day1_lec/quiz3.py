import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 256)
y1 = x**2
y2 = x**3

plt.plot(x, y1, 'b-', label='$y=x^2$')
plt.plot(x, y2, 'r-', label='$y=x^3$')



plt.grid(True)
plt.annotate('Parabola Min',
             xytext=(0.5, 5),
             xy=(0,0),
             arrowprops={'facecolor':'b'})
plt.annotate('Cubic Inflection',
             xytext=(-2,-10),
             xy=(0,0),
             arrowprops={'facecolor':'r'})
plt.legend(loc=0)

plt.text(-2, 15, 'Quadratic vs Cubic', fontsize=12, color='green')
plt.show()

