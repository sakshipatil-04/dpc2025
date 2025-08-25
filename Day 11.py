from typing import List

def string_permutations(s: str) -> List[str]:
    result = []
    chars = sorted(list(s))
    used = [False] * len(chars)

    def backtrack(path):
        if len(path) == len(chars):
            result.append("".join(path))
            return
        for i in range(len(chars)):
            if used[i]:
                continue
            if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(chars[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result

if __name__ == "__main__":
    test_cases = [
        ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
        ("aab", ["aab", "aba", "baa"]),
        ("aaa", ["aaa"]),
        ("a", ["a"]),
    ]

    for s, expected in test_cases:
        output = string_permutations(s)
        print(f"Input: {s}")
        print(f"Output: {output}")
        print(f"Expected: {expected}")
        print(f"Pass: {sorted(output) == sorted(expected)}\n")

    s = "abcd"
    output = string_permutations(s)
    print(f"Input: {s}")
    print(f"Number of permutations: {len(output)} (Expected 24)")
    print(f"Sample output: {output[:6]} ... {output[-3:]}")
