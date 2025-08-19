def findLeaders(arr):
    n = len(arr)
    leaders = []
    max_right = float('-inf')
   
    for i in range(n - 1, -1, -1):
        if arr[i] >= max_right:
            leaders.append(arr[i])
            max_right = arr[i]
    return leaders[::-1]

print(findLeaders([16, 17, 4, 3, 5, 2]))      
print(findLeaders([1, 2, 3, 4, 0]))           
print(findLeaders([7, 10, 4, 10, 6, 5, 2]))   
print(findLeaders([5]))
print(findLeaders([100, 50, 20, 10]))         
print(findLeaders(list(range(1, 1000001))))   
