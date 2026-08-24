def buscaSequencial(x, v):
  for i in range(len(x)):
    if v == x[i]:
      return i
  return -1
