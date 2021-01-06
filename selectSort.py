# Complexity = O(n)
def select(seq, start):
    minIndex = start
    
    for j in range(start+1, len(seq)):
        if seq[minIndex] > seq[j]:
            minIndex = j
    
    return minIndex

# Complexity = O(n^2)
def selSort(seq):
    for i in range(len(seq)):
        minIndex = select(seq,i)
        tmp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = tmp
        
# Basically, for each item, finds the smallest element in the remaining list right of it,
# and then swaps it.