
numbers = [10, 15, 3, 7, 23, 50, 11, 13, 4, 18]


prime_numbers = []

for num in numbers:
    if num < 2:
        continue
    
    
    is_prime = True
    
    
    for i in range(2, num):
        if num % i == 0:  
            is_prime = False
            break  
    
    if is_prime:
        prime_numbers.append(num)

print(prime_numbers)

