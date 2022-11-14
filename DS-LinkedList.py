class LinkedList:
    
    class __Node:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next
        
        def getItem(self):
            return self.item
        
        def getNext(self):
            return self.next
        
        def setItem(self, item):
            self.item = item
            
        def setNext(self, next):
            self.next = next
            
    # Complexity = O(len(contents))
    def __init__(self, contents=[]):
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0
        
        for e in contents:
            self.append(e)
            
    # Complexity = O(n)
    def __getitem__(self, index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            
            return cursor.getItem()
        
        raise IndexError("LinkedList index out of range")
    
    # Complexity = O(n)
    def __setitem__(self, index, val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            
            cursor.setItem(val)
            return
        
        raise IndexError("LinkedList assignment index out of range.")
    
    # Complexity = O(n)
    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                            str(type(self)) + " + " + str(type(other)))
        
        result = LinkedList()
        
        cursor = self.first.getNext()
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
            
        cursor = other.first.getNext()
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
        
        return result
    
    # Complexity = O(1)
    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1
    
    # Complexity = O(n)
    def insert(self, index, item):
        cursor = self.first
        
        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()
            
            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)
    
    # Defining function to find predecessor
    def predecessor(self, item):
        cursor = self.first
        
        if cursor.getNext() == None:
            raise IndexError("Iterating on a null list.")
        
        while cursor.getNext() != None:
            if cursor.getNext().getItem() == item:
                return cursor
            cursor = cursor.getNext()
        return None

    # Complexity = O(n)
    def __delitem__(self, index):
        cursor = self.first.getNext()

        if cursor.getNext() == None:
            # This means we are deleting the only item in the list
            self.first.setNext(None)
            self.numItems -= 1
            return
        
        if index >= 0 and index < self.numItems:            
            for i in range(index-1):
                cursor = cursor.getNext()
            # At this point, cursor is at the predecessor
            temp = cursor.getNext()
            cursor.setNext(temp.getNext())    
            self.numItems -= 1
            return
        
        raise IndexError("LinkedList index out of range")    
    
    
    def __len__(self):
        return self.numItems
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        
        if self.numItems != other.numItems:
            return False
        
        for i in range(self.numItems):
            if self[i] != other[i]:
                return False
        
        return True
    
    def __contains__(self, item):
        cursor = self.first.getNext()
        while cursor.getNext() != None:
            if cursor.getItem() == item:
                return True
            cursor = cursor.getNext()
        
        return False
    
    def __iter__(self):
        for i in range(self.numItems):
            yield self[i]

def printLL(listObj = LinkedList()):
    if len(listObj) == 0:
        print("Empty List")
    else:
        lst = []
        for i in range(len(listObj)):
            lst.append(listObj[i])
        print(lst)

def main():
    example = LinkedList(list(range(10)))
    
    printLL(example)

    print(len(example)-1)
    del example[len(example)-1]
    printLL(example)

    print(len(example)-1)
    del example[len(example)-1]
    printLL(example)

    print(len(example)-1)
    del example[len(example)-1]
    printLL(example)

    print(len(example)-1)
    del example[len(example)-1]
    printLL(example)

    print(len(example)-1)
    del example[len(example)-1]
    printLL(example)

    print(len(example)-1)
    del example[len(example)-1]
    printLL(example)

    print(len(example)-1)
    del example[len(example)-1]
    printLL(example)

    print(len(example)-1)
    del example[len(example)-1]
    printLL(example)

    print(len(example)-1)
    del example[len(example)-1]
    printLL(example)

    print(len(example)-1)
    del example[len(example)-1]
    printLL(example)
    
    print(example.first.getItem())
    print(example.first.getNext())
    
if __name__ == "__main__":
    main()
