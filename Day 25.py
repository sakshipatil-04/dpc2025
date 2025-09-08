from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (helper(node.left, low, node.val) and
                    helper(node.right, node.val, high))
        return helper(root)

def build_tree(values):
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

solution = Solution()

root1 = build_tree([2, 1, 3])
print(solution.isValidBST(root1))

root2 = build_tree([5, 1, 4, None, None, 3, 6])
print(solution.isValidBST(root2))  

root3 = build_tree([10, 5, 15, None, None, 6, 20])
print(solution.isValidBST(root3))
