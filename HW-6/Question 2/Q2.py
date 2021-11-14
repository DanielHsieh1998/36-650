import copy
class Queue:
    inner_list = []
    counter = 0
    
    def enqueue(self, value):
        self.inner_list.append(value)
        self.counter = self.counter + 1
        return
        
    def dequeue(self):
        if self.counter > 0:
            val = self.inner_list.pop(0)
            self.counter = self.counter - 1
            return val
        else:
            return

    def exist(self, element):
        tmp = copy.deepcopy(self)
        exist = False
        while tmp.counter > 0:
            new = tmp.dequeue()
            if new == element:
                exist = True
        if exist == False:
            print("Does not exist")
            return
        else:
            return exist
        
    def delete(self, element):
        boo = False
        for i in range(self.counter):
            tmp = self.dequeue()
            if tmp != element:
                self.enqueue(tmp)
            elif boo == False:
                boo = True
        return self
obj = Queue()
obj.enqueue(6)
obj.enqueue(7)
obj.enqueue(5)
obj.enqueue(5)
obj.enqueue(8)

print(obj.inner_list)

obj.delete(7)
print("delete an element in the middle")
print(obj.inner_list)

obj.delete(10)
print("delete an element not in the queue")
print(obj.inner_list)

obj.delete(6)
print("delete the first element")
print(obj.inner_list)

obj.delete(8)
print("delete the last element")
print(obj.inner_list)