def countSubstringsWithKDistinct(s: str, k: int) -> int:

    def atMostK(k: int) -> int:
        count = {}
        left = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            res += (right - left + 1)
        return res
    
    if k > len(s):
        return 0

    return atMostK(k) - atMostK(k - 1)


print(countSubstringsWithKDistinct("pqpqs", 2))
print(countSubstringsWithKDistinct("aabacbebebe", 3))
print(countSubstringsWithKDistinct("a", 1))
print(countSubstringsWithKDistinct("abc", 3))
print(countSubstringsWithKDistinct("abc", 2))

print(countSubstringsWithKDistinct("aaaa", 1))        
print(countSubstringsWithKDistinct("abc", 4))
