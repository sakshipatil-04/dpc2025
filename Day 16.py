import math

def find_lcm(n, m):
    return (n * m) // math.gcd(n, m)

print(find_lcm(4, 6))
print(find_lcm(5, 10))
print(find_lcm(7, 3))          
print(find_lcm(1, 987654321))  
print(find_lcm(123456, 789012))
