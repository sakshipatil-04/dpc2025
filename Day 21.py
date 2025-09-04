def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)

def test_reverse_stack():
    test_cases = [
        {"input": [3, 2, 1], "expected": [1, 2, 3]},
        {"input": [5], "expected": [5]},
        {"input": [-5, -10, -15], "expected": [-15, -10, -5]},
        {"input": [], "expected": []},
        {"input": [3, 3, 3], "expected": [3, 3, 3]},
    ]

    for i, case in enumerate(test_cases, 1):
        stack = case["input"].copy()
        reverse_stack(stack)
        result = stack
        assert result == case["expected"], f"❌ Test {i} failed: got {result}, expected {case['expected']}"
        print(f"✅ Test {i} passed: {result}")

if __name__ == "__main__":
    test_reverse_stack()
