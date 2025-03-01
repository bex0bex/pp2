class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0  # Start from 0

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current > self.n:
            raise StopIteration  
        else:
            even_number = self.current
            self.current += 2  
            return str(even_number) 

n = int(input("Enter a number: "))

even_gen = EvenNumbers(n)

print(",".join(even_gen))