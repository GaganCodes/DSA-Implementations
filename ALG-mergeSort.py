# Complexity = O(n)
# Both lists are already sorted, so just need to run through the length of the list
def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid
    
    # Merge the two lists while each has more elements
    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
        else:
            lst.append(seq[j])
            j += 1
    
    # Copy in the rest of the start to mid sequence
    # This is when we have exhausted the prev while loop, and there are still elements
    # left in start to mid section, here 'i' will continue from prev while loop
    # This will happen when we have exhausted all the 'j' elements, and 'i' has elements left
    while i < mid:
        lst.append(seq[i])
        i += 1
    
    # This is correct, because we merged the original sequence in lst, and then we are
    # replacing the sequence with the sorted list
    for i in range(len(lst)):
        seq[start+i] = lst[i]

# Complexity = O(n.logn)
# O(n) from merge, and O(logn) for dividing the list recursively
def mergeSortRecursively(seq, start, stop):
    if start >= stop-1:
        return
    
    mid = (start+stop)//2
 
    mergeSortRecursively(seq, start, mid)
    mergeSortRecursively(seq, mid, stop)
    merge(seq, start, mid, stop)

def mergeSort(seq):
    mergeSortRecursively(seq, 0, len(seq))
    

# mergeSort([2, 3, 14, 54, 63, 78, 40, 100, 1, 5, 25, 10])
