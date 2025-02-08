import math  

class Point:
    def __init__(self):
        
        self.x = float(input("enter the x-coordinate: "))  
        
        self.y = float(input("enter the y-coordinate: ")) 

    def show(self):
        print(f"point is at ({self.x}, {self.y})")

    def move(self):
        self.x += float(input("enter the shift for x: "))  
        
        self.y += float(input("enter the shift for y: "))  

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

point1 = Point()

point2 = Point()

point1.show()

point1.move()

point1.show()

distance = point1.dist(point2)  
print(f"the distance between point1 and point2 is: {distance}")

