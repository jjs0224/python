class Product():

    products = []

    def __init__(self):
        self
        
    def set_product(self):
        idata = input('상품을 입력하세요').split()
        while True:
            if idata[0]== 'exit':
                break
            else:   
                self.name = idata[0]
                self.price = int(idata[1])
                self.qty = int(idata[2])
    
                Product.products.append([self.name, self.price, self.qty])
                print(f'{self.name} {self.qty} 장바구니에 추가 완료!')
            idata = input('상품을 입력하세요').split()

class Cart():
    
    def calc_product(self):
        total = 0
        for x, y, z in Product.products:
            print(f'-{x} x {z} = {y*z}원')
            total += y*z
        print(f'총액: {total} 원')

p1 = Product()
p1.set_product()
c1 = Cart()
c1.calc_product()
