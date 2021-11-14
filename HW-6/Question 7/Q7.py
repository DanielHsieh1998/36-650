class Node:
    def __init__(self, data = None, small = None, big = None, toobig = None, parent = None):
        self.small = small #small child (less value)
        self.big = big #big child (bigger than parent, smaller than parent + 10)
        self.toobig = toobig # too big child (bigger than parent + 10)
        self.parent = parent
        self.data = data

    def insert(self,data):
        if self.data: 
            if self.data > data:
                if self.small is None: self.small = Node(data = data); self.small.parent = self
                else: self.small.insert(data)
            elif self.data <= data and self.data + 10 > data:
                if self.big is None: self.big = Node(data = data); self.big.parent = self
                else: self.big.insert(data)
            elif self.data + 10 <= data:
                if self.toobig is None: self.toobig = Node(data = data); self.toobig.parent = self
                else: self.toobig.insert(data)
        else: self.data = data

    def traversal(self):
        if self.small:
            self.small.traversal()
        print(self.data)
        if self.big:
            self.big.traversal()
        if self.toobig:
            self.toobig.traversal()
    
    def delete(self, data):
        node = self.findNode(data)
        if node.parent is None: # root
            l = node.subNodes()
            root = l.pop(0)
            self.data = root
            self.small = None; self.big = None; self.toobig = None
            self.insert_list(l)
            return
        l = node.subNodes()
        parent = node.parent
        if node == parent.small: parent.small = None
        elif node == parent.big: parent.big = None
        elif node == parent.toobig: parent.toobig = None
        parent.insert_list(l)
        
    def subNodes(self):
        l1 = []; l2 = []; l3 = []
        if self == None: return
        if self.small: l1 = self.small.traversal_list(l1)
        if self.big: l2 = self.big.traversal_list(l2)
        if self.toobig: l3 = self.toobig.traversal_list(l3)
        l = l1 + l2 + l3
        return l

    def insert_list(self, l):
        for i in l:
            self.insert(i)

    def findNode(self, data):
        if not self:
            return None
        if data == self.data:
            return self
        elif data < self.data and self.small: 
            node = self.small.findNode(data)
        elif data > self.data  and data < self.data + 10 and self.big:
            node = self.big.findNode(data)
        elif data >= self.data + 10 and self.toobig:
            node = self.toobig.findNode(data)
        else: return None

        return node

    def traversal_list(self,l):
        if self.small:
            self.small.traversal_list(l)
        l.append(self.data)
        if self.big:
            self.big.traversal_list(l)
        if self.toobig:
            self.toobig.traversal_list(l)
        return l
root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)
root.delete(45)
root.delete(20)
root.traversal()