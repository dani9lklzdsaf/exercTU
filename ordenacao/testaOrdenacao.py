import bubbleSort as bs
import selectionSort as ss
import insertionSort as ins
import heapSort as hs
import mergeSort as ms
a = [4, 3, 2, 1, 9, 7, 5, 8, 6]
print("Bubble Sort...:", bs.bubbleSort(a))

a = [4, 3, 2, 1, 9, 7, 5, 8, 6]
print("Selection Sort:", ss.selectionSort(a))

a = [4, 3, 2, 1, 9, 7, 5, 8, 6]
print("Insertion Sort:", ins.insertionSort(a))

a = [4, 3, 2, 1, 9, 7, 5, 8, 6]
print("Heap Sort:", hs.heapSort(a))

a = [4, 3, 2, 1, 9, 7, 5, 8, 6]
print("Merge Sort:", ms.mergeSort(a))

