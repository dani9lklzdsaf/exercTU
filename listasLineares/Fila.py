class Fila:
  def __init__(self):
    self.__itens = []
  def filaVazia(self):
    return len(self.__itens) == 0
  def enqueue(self, item):
    self.__itens.append(item)
  def dequeue(self):
    if not self.filaVazia():
      return self.__itens.pop(0)
    else:
      raise IndexError("Tentando remover item de uma fila vazia.")