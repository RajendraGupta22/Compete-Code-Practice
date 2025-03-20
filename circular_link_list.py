
"""
    author  : Rajendra Gupta
    alias   : Raj
    data    : 20 March 2025
    Desc    : circular link list implementation  
    visualiztaion link : https://www.cs.usfca.edu/~galles/visualization/QueueLL.html
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            # list empty first entry
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head

    def display(self):
        if self.head is None:
            print("List empty")
            return
        current = self.head
        while True:
            print(current.data,end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("back to head .")

    def length(self):
        if self.head is None:
            return 0
        current = self.head
        count = 0
        while True:
            count+=1
            current= current.next
            if current==self.head:
                break
        return count
    
    def delete_by_index(self,index):
        if self.head is None:
            print("Empty list")
            raise IndexError(f"index out of bound, empty list")
        if index < 0:
            raise ValueError("Negative index not allowed")
        current = self.head
        previous = None
        count = 0
        while True:
            if count == index:
                if previous is not None:
                    # Bypassing the node to be deleted
                    previous.next = current.next
                    # If the node to be deleted is the tail, update the tail reference
                    if current == self.tail:
                        self.tail = previous
                else:
                    # node to be delted is head
                    if self.head == self.tail:
                        # only one node in list
                        self.head = None
                        self.tail = None
                    else:
                        # head node
                        self.head = self.head.next # current hed set to next head
                        self.tail.next = self.head # pointer of tail to head change to new head
                return
            count += 1
            previous = current
            current = current.next
            if current == self.head:
                break
        raise IndexError(f"index {index} out of bound")
        
    def delete_by_val(self, data):
        if self.head is None:
            raise ValueError("The list is empty.")
        current = self.head
        previous = None
        while True:
            if current.data == data:
                if previous is not None:
                    # Bypassing the node to be deleted
                    previous.next = current.next
                    # If the node to be deleted is the tail, update the tail reference
                    if current == self.tail:
                        self.tail = previous
                else:
                    # If the node to be deleted is the head
                    if self.head == self.tail:
                        # Only one node in the list
                        self.head = None
                        self.tail = None
                    else:
                        # Update head and maintain the circular link
                        self.head = self.head.next
                        self.tail.next = self.head
                return
            previous = current
            current = current.next
            if current == self.head:
                break
        # Raise an exception if the element is not found
        raise ValueError(f"Node with data {data} not found.")
    
    def get(self,index):
        if index < 0:
            raise ValueError(f"Negative index not allowed")
        if self.head is None:
            raise IndexError(f"index out of bound, empty list")
        current = self.head
        count = 0
        while True:
            if count == index:
                return current.data
            current = current.next
            count += 1
            if current == self.head:
                break
        raise IndexError(f"index : {index} out of bound error")
    
    def __iter__(self):
       if self.head is None:
           return # no data in list , stop iteration
       current = self.head
       while True:
            yield current.data
            current = current.next
            if current == self.head:
                break 
            
if __name__ == '__main__':
    z =  CircularLinkList()
    z.append(1)
    z.append(2)
    z.append(3)
    
    print("length : ",z.length())
    print("display : ")
    z.display()
    print("get 0 index data : ",z.get(0))
    for x in z:
        print("iter ", x)
    z.delete_by_index(1)
    z.display()

    z.delete_by_val(3)
    z.display()
