# Node Class
class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

# LinkedList Class
class LinkedList:
    def __init__(self , firstNode: Node):
        self.firstNode = firstNode

    # Function to read value of node
    def read(self , index):
        currentNode = self.firstNode
        currentIndex = 0
        while currentIndex < index:
            currentNode = currentNode.next
            currentIndex += 1
            if currentNode is None:
                return None
        return currentNode

    # Function to add element at certain index
    def addIndex(self , value , index):
        newNode = Node(value)
        if index == 0:
            newNode.next = self.firstNode
            self.firstNode = newNode
            return
        currentNode = self.firstNode
        currentIndex = 0
        while currentIndex < index - 1:
            currentNode = currentNode.next
            currentIndex += 1
            if currentNode is None:
                return
        newNode.next = currentNode.next
        currentNode.next = newNode

    # Function to delete element of certain index
    def delete(self , index):
        if index == 0:
            self.firstNode = self.firstNode.next
            return
        currentNode = self.firstNode
        currentIndex = 0
        while currentIndex < index - 1:
            currentNode = currentNode.next
            currentIndex += 1
            if currentNode is None:
                return
        currentNode.next = currentNode.next.next

# Counting Occurrence of element
def occurrence_count(linkedList: LinkedList , value):
    if linkedList.firstNode.next is None:
        if linkedList.firstNode.value == value:
            return 1
        else:
            return 0
    if linkedList.firstNode.value == value:
        return 1 + occurrence_count(LinkedList(linkedList.firstNode.next) , value)
    else:
        return 0 + occurrence_count(LinkedList(linkedList.firstNode.next) , value)

# Program Test
n1 = Node('1')
n2 = Node('2')
n3 = Node('3')
n4 = Node('4')

linkedList = LinkedList(n1)

n1.next = n2
n2.next = n3
n3.next = n4

linkedList.addIndex('5' , 2)
print("Node no.2 value = " + str(linkedList.read(2).value))
linkedList.delete(2)
print("Node no.2 new value = " + str(linkedList.read(2).value))
linkedList.addIndex('3' , 2)
linkedList.addIndex('1' , 2)
linkedList.addIndex('3' , 2)
print("Number of occurrence = " + str(occurrence_count(linkedList, '1')))