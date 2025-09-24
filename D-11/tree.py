class Node:
    def __init__(self, root):
        self.data = root
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')

def levelorder(root):
    q=[root]
    while len(q)!=0:
        root=q.pop(0)
        print(root.data,end=' ')
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)

def sum_of_nodes(root):
    if root == None:
        return 0
    return root.data + sum_of_nodes(root.left) + sum_of_nodes(root.right)

def sum_of_even_nodes(root):
    if root == None:
        return 0
    current = root.data if root.data % 2 == 0 else 0
    return current+sum_of_even_nodes(root.left)+sum_of_even_nodes(root.right)

def height(root):
    if root == None:
        return 0
    return 1+max(height(root.left), height(root.right))

def topview(root):
    print()
    q=[]
    d=dict()
    root.level=0
    q.append(root)
    while len(q)!=0:
        root=q.pop(0)
        if root.level not in d:
            d[root.level]=root.data
        if root.left is not None:
            q.append(root.left)
            root.left.level=root.level-1
        if root.right is not None:
            q.append(root.right)
            root.right.level=root.level+1
    for i in sorted(d):
        print(d[i],end=" ")

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(8)
root.right.left = Node(15)
root.right.right = Node(25)
root.left.left.left = Node(1)

print("Inorder: ", end='')
inorder(root)
print("\nPreorder: ", end='')
preorder(root)
print("\nPostorder: ", end='')
postorder(root)
print("\nLevelorder: ", end='')
levelorder(root)
total = sum_of_nodes(root)
print("\nsum: ",total)
print("even sum: ",sum_of_even_nodes(root))
print("height: ",height(root))
print("Topview: ",topview(root))
