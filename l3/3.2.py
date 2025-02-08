class Shape:
    def area(self):
        return 0  

class Rectangle(Shape):
    def __init__(self):
        self.length = int(input())  
        self.width = int(input())  

    def area(self):
        return self.length * self.width  


rectangle = Rectangle()
print(rectangle.area())  
