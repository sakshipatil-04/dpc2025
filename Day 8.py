def reverseWords(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

print(reverseWords("the sky is blue"))       
print(reverseWords("  hello world  "))       
print(reverseWords("a good   example"))
print(reverseWords("    "))                  
print(reverseWords("word"))
