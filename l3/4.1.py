import math

class Point:
    def __init__(self):
        self.x = float(input())  # Вводим координату x
        self.y = float(input())  # Вводим координату y

    def show(self):
        print(f"Point is at ({self.x}, {self.y})")  # Выводим координаты

    def move(self):
        self.x += float(input())  # Смещаем точку по оси x
        self.y += float(input())  # Смещаем точку по оси y

    def dist(self, other):
        # Вычисляем расстояние между двумя точками
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Создаем две точки
point1 = Point()
point2 = Point()

# Выводим координаты первой точки
point1.show()

# Перемещаем первую точку
point1.move()
point1.show()

# Вычисляем расстояние между двумя точками
print(f"The distance between point1 and point2 is: {point1.dist(point2)}")
