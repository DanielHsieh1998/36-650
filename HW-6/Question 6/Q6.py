class Node:
  # constructor
    def __init__(self, data = None, previous=None): 
        self.data = data
        self.previous = previous

# A Reversed Linked List class with a single tail node
class ReversedLinkedList:
    def __init__(self, element = None):  
        self.tail = element
    
    def print_list(self):
        if self.tail == None:
            #raise ValueError("List is empty")
            return
        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")

    def insert(self,element):
        new = Node(element)
        if self.tail == None:
            self.tail = new
        else:
            tmp = self.tail
            self.tail = new
            new.previous = tmp
        return self

    def delete(self, data):
        if not self.tail:
            return

        temp = self.tail

        if self.tail.data == data:
            self.tail = self.tail.previous
            return

        while temp.previous:
            if temp.previous.data == data:
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")
        return
        
    def search(self,element):
        if self.tail == None:
            return False
        else: 
            tail = self.tail
            while tail.previous:
                if tail.data == element:
                    return True
                else:
                    tail = tail.previous
            if tail.data == element:
                return True
            else:
                return False

RLL = ReversedLinkedList()
RLL.insert(17)
RLL.insert(12)
print("test of insert")
print(RLL.tail.data)
print(RLL.tail.previous.data)

print("test of search")
print(RLL.search(12))
print(RLL.search(17))

print("test of delete")
RLL.delete(12)
print(RLL.tail.data)
RLL.delete(10)
RLL.delete(17)
print(RLL.tail)
RLL.delete(1)

print("\n")

first_node = Node(11)
linked_list = ReversedLinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)

print("The Linked List is (after insertion):")
linked_list.print_list()

linked_list.delete(6)

print("The Linked List is (after deleteing 6):")
linked_list.print_list()

print("Does 5 exist in the Linked List?")
print(linked_list.search(5))

print("Does 17 exist in the Linked List?")
print(linked_list.search(17))