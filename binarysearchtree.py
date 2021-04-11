class Node:
    def __init__(self, data):
        self.data: int = data
        self.right = None
        self.left = None
        self.counter = None


def insert(root=None, key=None):
    if root.data is None:
        root = Node(key)
    if root.data > key:
        if root.right is None:
            root.right = Node(key)
        if root.right:
            return insert(root=root.right, key=key)
    if root.data < key:
        if root.left is None:
            root.left = Node(key)
        if root.left:
            return insert(root=root.left, key=key)


def printTree(r : Node):
    if r.data:
        print(r.data, end='/n')
        if r.left:
            printTree(r.left)
        if r.right:
            printTree(r.right)
        if r.counter:
            print('( {} )'.format(r.counter))

k = Node(5)
insert(k, 15)
insert(k, 2)
insert(k,1)
printTree(k)
print(k.data, k.left.data, k.right.data)
