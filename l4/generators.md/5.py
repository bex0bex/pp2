class By3_4:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:  
            if self.current % 3 == 0 and self.current % 4 == 0:
                result = self.current 
                self.current += 1 
                return str(result)  
            self.current += 1  
        
        raise StopIteration  

n = int(input("Enter a number: "))

by34 = By3_4(n)

print(" ".join(by34))