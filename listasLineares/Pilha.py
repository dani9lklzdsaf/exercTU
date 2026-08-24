class Pilha:
  def __init__(self):
    self.__itens = []
  def pilhaVazia(self):
    return len(self.__itens) == 0
  def push(self, item):
    self.__itens.append(item)
  def pop(self):
    if not self.pilhaVazia():
      return self.__itens.pop()
    else:
      raise IndexError("Tentando remover item de uma pilha vazia.")