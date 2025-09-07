class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right

def run_test(tree_list, p_val, q_val):
    root = build_tree(tree_list)
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    lca = lowestCommonAncestor(root, p, q)
    print(f"LCA of {p_val} and {q_val} is: {lca.val}")

run_test([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4)  
run_test([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1)   
run_test([1, 2], 1, 2)                                  
