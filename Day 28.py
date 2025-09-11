from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right) if root else True

test_cases = [
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False),
    ([1], True),
    ([], True),
    ([1, 2, 2, 3, None, None, 3], False)
]

sol = Solution()
for i, (tree_list, expected) in enumerate(test_cases, 1):
    tree = buildTree(tree_list)
    result = sol.isSymmetric(tree)
    print(f"Test Case {i}: Input = {tree_list} → Output = {result} | Expected = {expected} | {'✅' if result == expected else '❌'}")
