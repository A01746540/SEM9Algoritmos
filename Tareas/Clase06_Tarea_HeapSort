import math
def BuildMaxHeap(A):
    for i in range (math.floor(len(A)/2), -1, -1):
        MaxHeapify(A,i)
def MaxHeapify(A, i):
    Asize = len(A)-1
    l = (i*2)+1
    r = (i*2)+2
    if(l<=Asize) and (A[l] > A[i]):
        largest = l
    else:
        largest = i
    if(r<=Asize) and (A[r] > A[largest]):
        largest = r
    if(largest != i):
        n = A[i]
        A[i] = A[largest]
        A[largest] = n
        print(A)
        MaxHeapify(A, largest)
def HeapSort(A):
    NewA = []
    BuildMaxHeap(A)
    Asize = len(A) - 1
    for i in range (Asize, -1, -1):
        Asize = len(A) - 1
        n = A[0]
        A[0] = A[Asize]
        A[Asize] = n
        NewA.append(A[Asize])
        A = A[0:Asize]
        print(A)
        BuildMaxHeap(A)
    print(list(reversed(NewA)))
A = [4, 10, 3, 5, 1]
HeapSort(A)