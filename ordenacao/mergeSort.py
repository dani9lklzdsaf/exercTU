# A sua solução deve testar os módulos em separado, ou seja, cada função deve ser testada individualmente.

def mergeSort(x):
  return merge(x, 0, len(x))

def merge(x, inicio, fim):
  if fim - inicio > 1:
    meio = (inicio + fim) // 2
    merge(x, inicio, meio)
    merge(x, meio, fim)
    concatena(x, inicio, meio, fim)
  return x

def concatena(x, inicio, meio, fim):
  esquerda = x[inicio:meio]
  direita = x[meio:fim]
  i, j, k = 0, 0, inicio
  while i < len(esquerda) and j < len(direita):
    if esquerda[i] <= direita[j]:
      x[k] = esquerda[i]
      i += 1
    else:
      x[k] = direita[j]
      j += 1
    k += 1
  while i < len(esquerda):
    x[k] = esquerda[i]
    i += 1
    k += 1
  while j < len(direita):
    x[k] = direita[j]
    j += 1
    k += 1
  return x
