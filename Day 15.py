
def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])

        max_len = max(max_len, right - left + 1)

    return max_len

if __name__ == "__main__":

    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "abcdefgh",
        "a"
    ]

    for s in test_cases:
        print(f"Input: {s}")
        print(f"Output: {length_of_longest_substring(s)}")
        print("-" * 30)
