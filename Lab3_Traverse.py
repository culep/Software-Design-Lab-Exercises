class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# to do inorder tree traversal
def Inorder(root):
    if root:
        Inorder(root.right)
        print(root.val),
        Inorder(root.left)


# to do postorder tree traversal
def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.val),


# to do preorder tree traversal
def Preorder(root):
    if root:
        print(root.val),
        Preorder(root.left)
        Preorder(root.right)



root = Node(0)
root.right = Node(3)
root.left = Node(7)
root.right.left = Node(13)
root.left.right = Node(16)
print ("\nThe Preorder traversal of binary tree is")
Preorder(root)

print ("\nThe Inorder traversal of binary tree is")
Inorder(root)

print ("\nPostorder traversal of binary tree is")
Postorder(root)