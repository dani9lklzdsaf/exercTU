def buscaBinaria(x, v):
  li, ls = 0, len(x) - 1
  while li <= ls:
    m = (li + ls) // 2
    if v == x[m]:
      return m
    elif v < x[m]:
      ls = m - 1
    else:
      li = m + 1
  return -1