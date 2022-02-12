# # Heap indexes (assuming start with index 0) :-
# # parent index = i - 1 / 2
# # left   index = 2i + 1
# # right  index = 2i + 2

# Index of Parent
def parent(list , i):
    p = (i - 1) / 2
    if(p <= len(list)):
        return p
    else:
        None

# Index of Left element
def left(list , i):
    l = (2 * i) + 1
    if(l <= len(list)):
        return l
    else:
        None

# Index of Right element
def right(list , i):
    r = (2 * i) + 2
    if(r <= len(list)):
        return r
    else:
        None

# Max-Heapify method
def maxHeapify(list , i):
    l = left(list , i)
    r = right(list , i)
    if not l or not r:
        return
    if(l <= len(list) and list[l] > list[i]):
        largest = l
    else:
        largest = i
    if(r <= len(list) and list[r] > list[largest]):
        largest = r
    if(largest != i):
        list[i] , list[largest] = list[largest] , list[i]
        maxHeapify(list , largest)

# Build Max-Heap
def maxHeap(list):
    for i in range(len(list) // 2 , -1 , -1):
        maxHeapify(list , i)

# Program Test
elements = list(map(int, input().split()))
maxHeap(elements)
print(*elements)