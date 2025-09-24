class Node:
    def __init__(self, root):
        self.data = root
        self.left = None
        self.right = None

def sum_of_nodes(root):
    if root == None:
        return 0
    return root.data + sum_of_nodes(root.left) + sum_of_nodes(root.right)

def sum_of_even_nodes(root):
    if root == None:
        return 0
    current = root.data if root.data % 2 == 0 else 0
    return current+sum_of_even_nodes(root.left)+sum_of_even_nodes(root.right)

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(8)
root.right.left = Node(15)
root.right.right = Node(25)
root.left.left.left = Node(1)

total = sum_of_nodes(root)
print("sum: ",total)
print("even sum: ",sum_of_even_nodes(root))