import random
import timing

# Complexity = O(n)
def partition(seq, start, stop):
    pivotIndex = start
    pivot = seq[pivotIndex]
    i = start+1
    j = stop-1
    
    while i <= j:
        while i <= j and not pivot < seq[i]:
            i +=1
        while i <= j and pivot < seq[j]:
            j -=1
        
        if i < j:
            tmp = seq[i]
            seq[i] = seq[j]
            seq[j] = tmp
            i +=1
            j -=1
    
    seq[pivotIndex] = seq[j]
    seq[j] = pivot
    
    return j

# Complexity = O(n.logn)
def quickSortRecursively(seq, start, stop):
    if start >= stop-1:
        return
    # Complexity = O(n)
    pivotIndex = partition(seq, start, stop)
    
    quickSortRecursively(seq, start, pivotIndex)
    quickSortRecursively(seq, pivotIndex+1, stop)

# Complexity = O(n.logn)
def quickSort(seq):
    # Complexity = O(n)
    for i in range(len(seq)):
        j = random.randint(0, len(seq)-1)
        tmp = seq[i]
        seq[i] = seq[j]
        seq[j] = tmp
    # Complexity = O(n.logn)
    quickSortRecursively(seq, 0, len(seq))
    

x = [5, 8, 2, 6, 9, 1, 0, 7]
quickSort(x)
print(x)