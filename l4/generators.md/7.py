class Squares:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.current = a  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current > self.b:
            raise StopIteration  
        else:
            square = self.current ** 2  
            self.current += 1  
            return square 

a = int(input("Enter start number (a): "))
b = int(input("Enter end number (b): "))

squares_gen = Squares(a, b)

for square in squares_gen:
    print(square, end=" ")