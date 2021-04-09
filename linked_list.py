# Problem On how to delete 4th node from the end of a linked list
# with the finding the length of the Linked list and looping fot that many times before deleting the element


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


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
        while (current):
            print(current.data, current.next)
            current = current.next

    def lenth(self):
        counter = 0
        current = self.head
        while current.next:
            counter += 1
            current = current.next
        return counter

    def delete(self, index):
        i = index
        current = self.head
        for j in range(index):
            previous = current
            current = current.next
        print(previous.data)
        previous.next = current.next
        current = None
        LinkedList.printll(self)


def insertfromloop(i, name):
    for j in range(i + 1):
        name.insert(j)


def deletenthfromtheend(name, element):
    if element < 0:
        index = name.lenth() + element + 1
        return LinkedList.delete(name, index=index)
    else:
        index = name.lenth() - element
        return LinkedList.delete(name, index=index)


name = input('enter the name of the linked list  --')
name = LinkedList()
insertfromloop(int(input('Number of elements in loop  -- ')), name)
deletenthfromtheend(name, int(input('enter the element to delete  -- ')))
