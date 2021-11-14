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
    
    def reduce_dup(linked_list):
        tmp = linked_list.head
        while tmp.next:
            data = tmp.data
            pointer = tmp
            while pointer.next:
                if pointer.next.data == data and pointer.next.next:
                    pointer.next = pointer.next.next
                elif pointer.data == data and not(pointer.next.next): 
                    # delete the last node in the linked list
                    pointer.next = None
                else:
                    pointer = pointer.next
            if tmp.next:
                tmp = tmp.next
        return linked_list
    
linked_list = LinkedList()
linked_list.insert(5)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)
linked_list.insert(6)
linked_list.insert(6)
linked_list.insert(7)

linked_list.reduce_dup().print_list()