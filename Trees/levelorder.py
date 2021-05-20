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


def bfs(r:Node):
    q = []
    q.append(r)
    while (len(q)>0):
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        print(node.data)

r = Node(20)
insert(r, 8)
insert(r, 22)
insert(r, 24)
insert(r, 4)
insert(r, 12)
insert(r, 10)
insert(r, 14)
bfs(r)