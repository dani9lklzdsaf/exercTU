def insertionSort(x):
  n = len(x)
  for i in range(1, n):
    key = x[i]
    j = i - 1
    while j >= 0 and key < x[j]:
      x[j + 1] = x[j]
      j = j - 1
    x[j + 1] = key
  return x