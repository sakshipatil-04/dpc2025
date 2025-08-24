from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())

print("Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']")
print("Output:", groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print()

print("Input: ['']")
print("Output:", groupAnagrams([""]))
print()

print("Input: ['a']")
print("Output:", groupAnagrams(["a"]))
print()

print("Input: ['abc', 'bca', 'cab', 'xyz', 'zyx', 'yxz']")
print("Output:", groupAnagrams(["abc", "bca", "cab", "xyz", "zyx", "yxz"]))
print()

print("Input: ['abc', 'def', 'ghi']")
print("Output:", groupAnagrams(["abc", "def", "ghi"]))
