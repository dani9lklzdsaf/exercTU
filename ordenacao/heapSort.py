# A sua solução deve testar os módulos em separado, ou seja, cada função deve ser testada individualmente.
# A heapify gera um heap, ou seja, o vetor é reorganizado como uma árvore binária,
# onde cada nó é maior que seus filhos. 
# A função heapSort utiliza a função heapify para ordenar o vetor.

def geraHeap(x, n, i):
  largest = i  # Inicializa o maior como raiz
  l = 2 * i + 1  # filho esquerdo
  r = 2 * i + 2  # filho direito

  # Verifica se o filho esquerdo é maior que a raiz
  if l < n and x[l] > x[largest]:
    largest = l

  # Verifica se o filho direito é maior que o maior até agora
  if r < n and x[r] > x[largest]:
    largest = r

  # Se o maior não for a raiz, troca e continua heapificando
  if largest != i:
    x[i], x[largest] = x[largest], x[i]  # Troca
    geraHeap(x, n, largest)

def heapSort(x):
  n = len(x)

  # Construir o heap máximo
  for i in range(n // 2 - 1, -1, -1):
    geraHeap(x, n, i)

  # Extrair elementos do heap
  for i in range(n - 1, 0, -1):
    x[i], x[0] = x[0], x[i]  # Trocar
    geraHeap(x, i, 0)

  return x