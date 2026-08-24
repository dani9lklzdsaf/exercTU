def selectionSort(x):
  n = len(x)
  for i in range(n-1):
    for j in range(i+1, n):
      if x[i] > x[j]:
        x[i], x[j] = x[j], x[i]
  return x