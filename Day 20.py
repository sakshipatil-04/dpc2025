
def sort_stack(stack):

    if not stack:
        return
    top = stack.pop()
    sort_stack(stack)
    insert_sorted(stack, top)

def insert_sorted(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return

    top = stack.pop()
    insert_sorted(stack, element)
    stack.append(top)

if __name__ == "__main__":
    test_cases = [
        [3, 1, 4, 2],
        [7, 1, 5],
        [5],
        [-3, 14, 8, 2],
        [],
        [3, 3, 3]
    ]

    for i, stack in enumerate(test_cases, 1):
        print(f"Test Case {i} - Original Stack: {stack}")
        sort_stack(stack)
        print(f"Sorted Stack: {stack}\n")
