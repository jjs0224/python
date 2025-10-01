import matplotlib.pyplot as plt

# plt.plot([10,20,30,40], [4,2,99,12],
#          color='orange', lw=5, ls='--', marker='o', ms=12, mec='green', mew=5, mfc='red')
# plt.show()

#선그래프 할때만 사용가능
#color = 선색깔, lw = Line Width,  marker = o 모양, ms = Marker Size,
# mec = Marker Edge Color, mew = Marker Edge Width, mfc = Marker Face Color

plt.plot([10,20,30,40], [4,2,99,12],
         color='k', lw=5, ls='--', marker='^', ms=12, mec='blue', mew=5, mfc='yellow')
plt.show()

x = range(5)
y = [2,5,7,8,1]
plt.plot(x, y, 'o-')
x2 = [2]
y2 = [7]
plt.plot(x2,  y2, 'rs')
plt.show()
































