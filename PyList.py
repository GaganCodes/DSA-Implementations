class PyList:
    # Initializing with size 10 and no contents, user may change as needed
    # Complexity of __init__ = O(1) for no value, O(n) if contents is non-empty sequence
    def __init__(self, contents = [], size=10):
        self.items = [None]*size
        self.numItems = 0
        self.size = size
        
        for e in contents:
            self.append(e)
            
    # Complexity of __getitem__ = O(1) because we are just accessing the index
    def __getitem__(self, index):
        if index >= 0 and index < self.numItems:
            return self.items[index]
        
        raise IndexError("PyList index out of range")
    
    # Complexity of __setitem__ = O(1) because getting and assigning both are O(1)
    def __setitem__(self, index, val):
        if index >= 0 and index < self.numItems:
            self.items[index] = val
            return
        
        raise IndexError("PyList assignment index out of range")
    
    # Complexity of __add__ = O(n1+n2)
    def __add__(self, other):
        result = PyList(size=self.numItems+other.numItems)
        
        for i in range(self.numItems):
            result.append(self.items[i])
        
        for i in range(other.numItems):
            result.append(other.items[i])
        
        return result
    
    # Complexity of __makeroom = O(n)
    def __makeroom(self):
        newLen = (self.size//4) + self.size + 1         # Increasing size by 1/4
        newLst = [None]*newLen
        
        for i in range(self.numItems):
            newLst[i] = self.items[i]
        
        self.items = newLst
        self.size = newLen
    
    # Complexity of append = O(1) amortized
    def append(self, item):
        if self.numItems == self.size:
            self.__makeroom()
        
        self.items[self.numItems] = item
        self.numItems += 1
    
    # Complexity of insert = O(n)
    def insert(self, i, e):
        # i is the index of the element to be inserted, e is the element
        if self.numItems == self.size:
            self.__makeroom()
            
        if i < self.numItems:
            for j in range(self.numItems-1, i-1, -1):
                self.items[j+1] = self.items[j]
            
            self.items[i] = e
            self.numItems += 1
        else:
            self.append(e)
    
    # Complexity of __delitem__ = O(n)
    def __delitem__(self, index):
        for i in range(index, self.numItems-1):
            self.items[i] = self.items[i+1]
        
        self.numItems -= 1
    
    # Complexity of __eq__ = O(n)
    def __eq__(self, other):
        if type(other) != type(self):
            return False
        
        if self.numItems != other.numItems:
            return False
        
        for i in range(self.numItems):
            if self.items[i] != other.items[i]:
                return False
        
        return True
    
    # Complexity of __iter__ = O(n)
    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]
    
    # Complexity of __len__ = O(1), O(n) if we are not keeping track with self.numItems
    def __len__(self):
        return self.numItems
    
    # Complexity of __contains__ = O(n)
    def __contains__(self, item):
        for i in range(self.numItems):
            if self.items[i] == item:
                return True
        
        return False
    
    # Complexity of __str__ = O(n)
    def __str__(self):
        s = "["
        for i in range(self.numItems):
            s = s + repr(self.items[i])
            if i < self.numItems-1:
                s = s + ", "
        
        s = s + "]"
        return s
    
    # Complexity of __repr__ = O(n)
    def __repr__(self):
        s = "PyList(["
        for i in range(self.numItems):
            s = s + repr(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
            
        s = s + "])"
        return s