def find_missing_number(arr):
    n = len(arr) + 1  
    total_sum = n * (n + 1) // 2  
    actual_sum = sum(arr)  
    return total_sum - actual_sum

print(find_missing_number([1, 2, 4, 5]))         
print(find_missing_number([2, 3, 4, 5]))          
print(find_missing_number([1, 2, 3, 4]))          
print(find_missing_number([1]))                  
print(find_missing_number(list(range(1, 1000000))))  
