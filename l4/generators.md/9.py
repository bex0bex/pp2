class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current < 0:
            raise StopIteration 
        else:
            num = self.current 
            self.current -= 1  
            return num  

n = int(input("Enter a number: "))

countdown_gen = Countdown(n)

for num in countdown_gen:
    print(num, end=" ")
