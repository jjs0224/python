import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

customer = ['김길동','홍길동','최길동','이길동','오길동']
customer_index = range(len(customer))
y_data = [120, 90, 200, 110, 230]

fig = plt.figure(figsize=(6,4))
ax1 = fig.add_subplot(111)
ax1.bar(customer_index, y_data, color='darkblue')
plt.xticks(customer_index, customer)
plt.xlabel('고객 이름')
plt.ylabel('수요')
plt.show()

# women_pop = [5, 30, 45, 22]
# man_pop = [-5, -25, -50, -20]
# x = range(4)
# plt.barh(x, women_pop, color='0.25')
# plt.barh(x, man_pop, color='0.75')
# plt.show()




