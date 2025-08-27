def longestPalindrome(s: str) -> str:
    if not s or len(s) == 1:
        return s
    
    start, max_len = 0, 1
    
    def expandAroundCenter(left: int, right: int) -> None:
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
    
    for i in range(len(s)):
        expandAroundCenter(i, i)     
        expandAroundCenter(i, i + 1) 
    
    return s[start:start + max_len]

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))   
print(longestPalindrome("a"))      
print(longestPalindrome("aaaa"))
print(longestPalindrome("abc"))    
