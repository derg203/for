numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 0
for i in range (2,len(numbers)+1) :
    is_prime = 0
    for j in  range(2 ,i+1) :
        if i % j ==0 :
            is_prime =is_prime + 1
            if j == i:
                 if is_prime > 1 :
                     not_primes.append(i)
                 else:primes.append(i)
        else:
            continue
print('простые числа:', primes)
print('не простые числа:', not_primes)

