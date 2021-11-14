import copy
class Node:
  # constructor
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):  
        self.head = None

    # Print the linked list
    def print_list(self):
        if self.head == None:
            #raise ValueError("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    # Delete a node in a linked list
    def delete(self, data):
        if not self.head:
            return

        temp = self.head

        # Check if head node is to be deleted
        if self.head.data == data:
            #print("Deleted node is " + str(self.head.data))
            self.head = self.head.next
            return

        while temp.next:
            if temp.next.data == data:
                #print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
        return

    def sort(self):
        l = self.size()
        l_list = LinkedList()
        for i in range(l):
            min = self.head.data
            temp = self.head
            while temp.next:
                if temp.next.data < min:
                    min = temp.next.data
                temp = temp.next
            l_list.insert(min)
            self.delete(min)
        return l_list

linked_list = LinkedList()
linked_list.insert(43)
linked_list.insert(1)
linked_list.insert(23)
linked_list.insert(34)
linked_list.insert(98)
linked_list.insert(2)
linked_list.insert(6)
linked_list.insert(12)

linked_list.print_list()
linked_list.sort().print_list()