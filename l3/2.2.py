class Shape:
    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        self.length = int(input())  

    def area(self):
        return self.length * self.length  

square = Square(0)  
print(square.area())  
