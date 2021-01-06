class Heap:
    # Construction a minimum Heap
    def __init__(self, items = []):
        self.items = []
        self.numItems = 0
        for item in items:
            self.insert(item)
    
    def parentIndex(self, index):
        # Root
        if index == 0:
            return None
        else:
            return (index-1)//2
    
    def leftChildIndex(self, index):
        return 2*index + 1
    
    def rightChildIndex(self, index):
        return 2*index + 2
    
    def insert(self, item):
        self.items.append(item)
        self.numItems += 1
        self.bubbleUp(len(self.items)-1)
    
    def bubbleUp(self, index):
        # Find the parent index
        parentIndex = self.parentIndex(index)
        # If at root, no execution needed
        if parentIndex == None:
            return
        elif self.items[parentIndex] > self.items[index]:
            temp = self.items[index]
            self.items[index] = self.items[parentIndex]
            self.items[parentIndex] = temp
            self.bubbleUp(parentIndex)
    
    def bubbleDown(self, index):
        childIndex = self.leftChildIndex(index)
        minIndex = index
        
        for i in range(2):
            # To make sure we're not beyond the end
            if childIndex + i <= self.numItems-1:
                # We are essentially checking left and right child
                if self.items[minIndex] > self.items[childIndex+i]:
                    minIndex = childIndex+i
        # Checking if minIndex is one of the children            
        if minIndex != index:
            temp = self.items[index]
            self.items[index] = self.items[minIndex]
            self.items[minIndex] = temp
            self.bubbleDown(minIndex)
    
    def extractMin(self):
        minimum = None
        
        if self.numItems == 0:
            print("Empty heap, nothing to extract.")
        else:
            minimum = self.items[0]
            self.items[0] = self.items[-1]
            del self.items[-1]
            self.numItems -= 1
            self.bubbleDown(0)
        
        return minimum
    
    def __len__(self):
        return self.numItems

def heapSort(inputList = []):
    sortedList = []
    heap = Heap(inputList)
    for i in range(len(heap)):
        sortedList.append(heap.extractMin())
    
    return sortedList
            
def main():
    
    exList = [40, 12, 45, 32, 33, 1, 1, 0, 22, 9, 8, 2, 1, 3, 6, 23, 19, 26, 40, 38]
    
    sortedHeap = heapSort(exList)
    
    print(sortedHeap)
    
    print('Works')
    
if __name__ == "__main__":
    main()