# Implementing a Set using Hashing principles

import random

class HashSet:
    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self,other):
            return False

    def __add(item,items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] != None:
            if items[idx] == item:
                # item already in set
                return False

            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx

            idx = (idx + 1) % len(items)

        if loc < 0:
            loc = idx

        items[loc] = item  

        return True

    def __remove(item,items):
        idx = hash(item) % len(items)

        while items[idx] != None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                if items[nextIdx] == None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True

            idx = (idx + 1) % len(items)

        return False

    def __rehash(oldList, newList):
        for x in oldList:
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x,newList)

        return newList

    def __init__(self,contents=[]):
        self.items = [None] * 10
        self.numItems = 0

        for item in contents:
            self.add(item)

    def __str__(self):
        stringSet = '['
        for item in self:
            stringSet += str(item)
            stringSet += ', '
        stringSet = stringSet[:-2]
        stringSet += ']'
        return stringSet
    
    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]    

    # Following are the mutator set methods 
    def add(self, item):
        if HashSet.__add(item,self.items):
            self.numItems += 1             
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items,[None]*2*len(self.items))

    def remove(self, item):
        if HashSet.__remove(item,self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items,[None]*int(len(self.items)/2))
        else:
            raise KeyError("Item not in HashSet")

    def discard(self, item):
        try:
            self.remove(item)
        except:
            pass

    def pop(self):
        idx = random.randint(0, self.numItems-1)
        try:
            itemToPop = self.items[idx]
            self.remove(itemToPop)
        except:
            pass

    def clear(self):
        if len(self) == 0:
            return True
        else:
            while len(self) > 0:
                idx = len(self)-1
                item = self.items[idx]
                self.remove(item)
	
    def update(self, other):
        for item in other:
            self.add(item)

    def intersection_update(self, other):
        # This set will have all the elements in self but not in other
        # All the elements in self outside intersection
        notIntersection = self.difference(other)
        # Update the self to delete these elements
        self.difference_update(notIntersection)

    def difference_update(self, other):
        for item in other:
            self.discard(item)

    def symmetric_difference_update(self, other):
        # Should update the self with self.difference(other).union(other.difference(self))
        # Keeping an object with items in other without self
        otherDiff = other.difference(self)
        # Updating self without items commom with other
        self.difference_update(other)
        # Adding non-common items from other in self
        self.update(otherDiff)
        
    # Following are the accessor methods for the HashSet  
    def __len__(self):
        return self.numItems

    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return True

            idx = (idx + 1) % len(self.items)

        return False

    # One extra method for use with the HashMap class. This method is not needed in the 
    # HashSet implementation, but it is used by the HashMap implementation. 
    def __getitem__(self, item):
        idx = hash(item)%len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return self.items[idx]
            
            idx = (idx+1)%len(self.items)
        
        return None

    def not__contains__(self, item):
        pass

    def isdisjoint(self, other):
        pass


    def issubset(self, other):
        isSub = True
        
        for item in self:
            if item not in other:
                isSub = False
        
        return isSub


    def issuperset(self, other):
        if other.issubset(self):
            return True
        else:
            return False

    def union(self, other):
        pass

    def intersection(self, other):
        pass

    def difference(self, other):
        result = HashSet(self)
        result.difference_update(other)
        return result

    def symmetric_difference(self, other):
        pass

    def copy(self):
        other = HashSet([])
        for item in self:
            other.add(item)
        
        return other

    # Operator Definitions
    def __or__(self, other):
        pass

    def __and__(self,other):
        pass

    def __sub__(self,other):
        pass

    def __xor__(self,other):
        pass

    def __ior__(self,other):
        pass

    def __iand__(self,other):
        pass

    def __ixor(self,other):
        pass    

    def __le__(self,other):
        pass

    def __lt__(self,other):
        pass

    def __ge__(self,other):
        pass

    def __gt__(self,other):
        pass

    def __eq__(self,other):
        if type(self) != type(other):
            return False
        
        if len(self) != len(other):
            return False
        
        for item in self:
            if item not in other:
                return False
        
        return True


def main():
    s = HashSet(list(range(100)))

    t = HashSet(list(range(10,20)))

    u = HashSet(list(range(10,20)))

    if len(t) == len(u) and len(t) == 10:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")

    s.intersection_update(t)

    if len(s) == 10:
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")

    s = HashSet(list(range(100)))

    t.update(s)

    if len(s) == len(t):
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")

    t.clear()
    t.update(u)

    if len(t) == len(u):
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")

    s.difference_update(t)

    test5Passed = True
    test6Passed = True

    for x in range(1,10):
        if x in s:
            pass
        else:
            test5Passed = False
            print("Test 5 Failed on",x)

        if x not in s:
            test6Passed = False
            print("Test 6 Failed on",x)

    if test5Passed:
        print("Test 5 Passed")

    if test6Passed:
        print("Test 6 Passed")


    test7Passed = True
    test8Passed = True

    for x in range(20,100):
        if x in s:
            pass
        else:
            test7Passed = False
            print("Test 7 Failed on",x)

        if x not in s:
            test8Passed = False
            print("Test 8 Failed on",x)

    if test7Passed:
        print("Test 7 Passed")

    if test8Passed:
        print("Test 8 Passed")   

    x = HashSet(["a","b","c","d","e","f","g","h","i","j","k"])

    y = HashSet(["c","d","e","l","m","n"])

    z = x.difference(y)

    if len(z) == 8:
        print("Test 9 Passed")
    else:
        print("Test 9 Failed")

    test10Passed = True

    for item in z:
        if item not in ["a","b","f","g","h","i","j","k"]:
            test10Passed = False
            print("Test 10 Failed on", x)

    if test10Passed:
        print("Test 10 Passed")

    if z.issubset(x):
        print("Test 11 Passed")
    else:
        print("Test 11 Failed")

    if x.issuperset(z):
        print("Test 12 Passed")
    else:
        print("Test 12 Failed")

    if z == y:
        print("Test 13 Failed")
    else:
        print("Test 13 Passed")

    if z == z:
        print("Test 14 Passed")
    else:
        print("Test 14 Failed")

    r = z.copy()

    if r == z:
        print("Test 15 Passed")
    else:
        print("Test 15 Failed")

    for item in range(50):
        z.add(item)

    for item in range(50):
        z.discard(item)

    if r == z:
        print("Test 16 Passed")
    else:
        print("Test 16 Failed")    

    for item in range(50):
        z.add(item)

    for item in range(50):
        z.remove(item)  

    if r == z:
        print("Test 17 Passed")
    else:
        print("Test 17 Failed")  
        

if __name__ == "__main__":
    main()
