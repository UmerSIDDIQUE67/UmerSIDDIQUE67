
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.value, end=" ")
    inorder_traversal(root.right)
def preorder_traversal(root):
    if root is None:
        return
    print(root.value, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value, end=" ")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("Inorder traversal:")
inorder_traversal(root)  
print("Preorder traversal:")
preorder_traversal(root) 
print("Postorder traversal:")
postorder_traversal(root)  
