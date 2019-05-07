#클래스 내부/외부 변수 선언의 차이
product_name = 'Cellphone: '

#클래스 정의
class Factory():
    def hello(self):
        print("Hello! ", end = '')

class Smartphone_factory(Factory):
    #내부변수 초기선언
    product_name = 'Smartphone: '
    price = 100

    #메소드 선언
    def __init__(self, brand):
        self.brand = brand
    
    def print_full_name(self, version):
        print(self.product_name + self.brand + version)
    
    def like_myself(self):
        print('Yes!' + self.brand)
    
    def price_increase(self):
        Smartphone_factory.price += 100
        self.price += 50
    
    def price_decrease(self):
        self.price -= 30
        return self.price
    
    def print_price(self):
        print(self.price)

#새로운 인스턴스 선언
apple = Smartphone_factory('iPhone')
samsung = Smartphone_factory('Galaxy')

#메소드 호출의 두 가지 방법: 클래스를 통한 호출과 인스턴스를 통한 호출
#인스턴스를 통해 호출하면 self 자리에 무조건 자기 자신을 넣는다!
Smartphone_factory.print_full_name(apple, 'XR')
apple.print_full_name('XS_MAX')

Smartphone_factory.print_full_name(samsung, 'S10')
samsung.print_full_name('S10+')

#self는 항상 메소드에 인자로 주어진다. 첫 인자를 다른 엉뚱한 것으로 줘도 다 self처럼 작동하지만, 
#self를 인자로 주는 것을 관례로 한다.
apple.like_myself()

#클래스 내에서 클래스를 불러서 그 클래스에 해당하는 변수 전체를 조작할 수 있다. 
#self는 인스턴스 하나만 조작한다.
apple.price_increase()
samsung.price_decrease()
apple.price_increase()
samsung.price_decrease()

apple.print_price()
samsung.print_price()
print(Smartphone_factory.price)
