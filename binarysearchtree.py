class Node:
    def __init__(self, data):
        self.data: int = data
        self.right: Node = None
        self.left: Node = None
        self.counter = None


def insert(root=None, key=None):
    if root.data is None:
        root = Node(key)

    elif root.data < key:
        if root.right is None:
            root.right = Node(key)
        if root.right:
            return insert(root=root.right, key=key)
    elif root.data > key:
        if root.left is None:
            root.left = Node(key)
        if root.left:
            return insert(root=root.left, key=key)


def Inorder(r: Node):
    if r:
        Inorder(r.left)
        print(r.data)
        Inorder(r.right)


def preinorder(r: Node, pre: Node = None):
    while r.right:
        r = r.right
    return (r.data)


def deleteelement(r: Node, element):
    if r.left is None and r.right is None and r.data == element:
        r.data = None
        return Inorder(r)
    elif r.left and r.right is None and r.data == element:
        r.data = r.left.data
        r.left = None
    elif r.right and r.left is None and r.data == element:
        r.data = r.right.data
        r.right = None

    elif r.data is None:
        return print('No items in the tree')
    elif r.data and r.data != element:

        if element < r.data:
            return deleteelement(r.left, element)
        if element > r.data:
            return deleteelement(r.right, element)

    elif r.right and r.left and r.data == element:
        k = preinorder(r.left)
        r.data = k
        deleteelement(r.left, k)


r = Node(20)
insert(r, 8)
insert(r, 22)
insert(r, 24)
insert(r, 4)
insert(r, 12)
insert(r, 10)
insert(r, 14)
Inorder(r)
deleteelement(r, 20)
Inorder(r)
