# Problem On how to delete 4th node from the end of a linked list
""" With bigbrain using two pointer where first will go up to last and the second one follows the tails of the first
    pointer with the distance of the index so that when the first will hit the last element and seond will reach to the
    desired index  """

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newnode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
        else:
            self.head = newnode

    def printll(self):
        current = self.head
        while current.next:
            print(current.data)
            current = current.next


def insertfromloop(i, name):
    for j in range(i + 1):
        name.insert(j)


def deletefromLinkedlist(name, index):
    if index >= 0:
        current = name.head
        pre = None
        for i in range(index - 1):
            pre = current
            current = current.next
        pre.next = current.next
        current = None
        LinkedList.printll(name)
    if index < 0:
        counter = 0
        current = name.head
        pointer = name.head
        prv_pointer = None

        while current:
            current = current.next
            if -counter < index:
                prv_pointer = pointer
                pointer = pointer.next
            counter += 1
        print('{} is deleted up on ur request'.format(pointer.data))
        prv_pointer.next = pointer.next
        LinkedList.printll(name)

name = input('enter the name of the linked list  --')
name = LinkedList()
insertfromloop(int(input('Number of elements in loop  -- ')), name)
name.printll()
deletefromLinkedlist(name, int(input('enter the index to delete ---  ')))
