import matplotlib.pyplot as plt

ax1 = plt.gca()
ax2 = ax1.twinx()

line1 = ax1.plot([10, 5, 3, 12, 7], 'r--', label='y1')
print(line1) #[<matplotlib.lines.Line2D object at 0x0000028E282EAB90>]
ax1.set_ylabel('y1')

line2 = ax2.plot([100, 200, 220, 170, 120], 'b:', label='y2')
ax2.set_ylabel('y2')
lns = line1 + line2
print(lns) #[<matplotlib.lines.Line2D object at 0x000001AB2598AC20>,
            # <matplotlib.lines.Line2D object at 0x000001AB2598AF80>]
print(line1[0].get_label()) #y1
labels = [l.get_label() for l in lns]
print(labels) #['y1', 'y2']
#plt.legend(lns, labels, loc='best')
plt.legend(lns, ['y1 graph', 'y2 graph'], loc='best')
plt.show()
