def longestCommonPrefix(strs):
    if not strs:  
        return ""
    prefix = strs[0]

    for word in strs[1:]:
        while word[:len(prefix)] != prefix:
            prefix = prefix[:-1]  
            if not prefix:
                return ""  

    return prefix

print("Input: ['flower', 'flow', 'flight']")
print("Output:", longestCommonPrefix(["flower", "flow", "flight"]))
print()

print("Input: ['dog', 'racecar', 'car']")
print("Output:", longestCommonPrefix(["dog", "racecar", "car"]))  
print()

print("Input: ['apple', 'ape', 'april']")
print("Output:", longestCommonPrefix(["apple", "ape", "april"]))
print()

print("Input: ['']")
print("Output:", longestCommonPrefix([""]))  
print()

print("Input: ['alone']")
print("Output:", longestCommonPrefix(["alone"]))
