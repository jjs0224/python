def order_summary(**kwargs):
    print('order summary')
    total = 0
    for item, qty in kwargs.items():
        print(f'{item}: {qty} 개')
        total += qty
    print(f'총 주문 수량: {total}개')
    print()

order_summary(apple=3, banana=2, orange=4)
order_summary(notebook=1, pen=10, eraser=5, book=2)

#according to index, key and value is added to the dictionary