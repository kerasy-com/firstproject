class Rectangle:
    increase_amount = 1.1

    def __init__(self, _width, _height):
        #가로, 세로 길이 객체 속성에 저장
        self.width = _width
        self.height = _height

    def print_info(self): #가로 세로 출력
        print("Width: " + str(self.width) + "\nHeight: " + str(self.height))

    def calcArea(self): #넓이 구하기
        print("The area is: " + str(self.width * self.height))
 
    def width_increase(self): #width를 increase_amount배만큼 증가시킴
        self.width *= self.increase_amount

rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)

#rect1
rect1.print_info() #가로 세로 길이 출력
rect2.print_info()

#원래 넓이 출력
rect1.calcArea()
rect2.calcArea()

# width를 'increase_amount'배만큼 증가시킴
rect1.width_increase()
rect2.width_increase()

#바뀐 넓이 출력
rect1.calcArea()
rect2.calcArea()