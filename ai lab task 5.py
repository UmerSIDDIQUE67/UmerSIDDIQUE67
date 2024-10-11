class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def dfs_stack(root):
    if root is None:
        return
    stack = []
    stack.append(root)
    while stack:
        current_node = stack.pop()
        print(current_node.value, end=" ")
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("DFS traversal with stack:")
dfs_stack(root)
