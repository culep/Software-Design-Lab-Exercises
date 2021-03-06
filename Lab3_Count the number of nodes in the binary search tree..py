#Counting the Number of Nodes in the Binary Tree

class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# to get the left height of the node
def left_height(node):
    height = 0
    while (node):
        height += 1
        node = node.left

    return height


# to get the right height of the node
def right_height(node):
    height = 0
    while (node):
        height += 1
        node = node.right

    return height

#to get the count of nodes
def totalN(root):
    # Base case
    if (root == None):
        return 0

    left_h = left_height(root)
    right_h = right_height(root)

    if (left_h == right_h):
        return (1 << left_h) - 1

    return 1 + totalN(root.left) + totalN(root.right)


#nodes
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(9)
root.right.right = node(8)
root.left.left.left = node(6)
root.left.left.right = node(7)
root.left.right.left = node(10)

print ("\nThe total node is: ")
print (totalN(root))