import math

def count_divisors(N):
    count = 0
    sqrtN = int(math.isqrt(N))  
    for i in range(1, sqrtN + 1):
        if N % i == 0:
            count += 1 
            if i != N // i:  
                count += 1
    return count

print(count_divisors(12))   
print(count_divisors(18))   
print(count_divisors(29))
print(count_divisors(100))
print(count_divisors(1))
print(count_divisors(997))  
print(count_divisors(36))  
