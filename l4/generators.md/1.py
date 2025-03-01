import math 

class MyNum:
    def __iter__(self):
        self.a = 1
        return self
    
    def get(self):
        self.N = int(input())

    def __next__(self):
        if self.a <= self.N:
            x = pow(self.a, 2)
            self.a += 1
            return x
        else:
            raise StopIteration
        
my_num = MyNum()
my_num.get()

for i in my_num:
    print(i)
