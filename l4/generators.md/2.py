def square_generator(N):
    for i in range(N + 1):
        yield i ** 2  

N = int(input("Enter a number: "))
for square in square_generator(N):
    print(square, end=" ")