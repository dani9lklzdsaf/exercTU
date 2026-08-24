from Elemento import Elemento
class No:
  def __init__(self, elemento = Elemento(), proximo = None):
    self.__elemento = elemento
    self.__proximo = proximo
  def getElemento(self):
    return self.__elemento
  def setElemento(self, elemento):
    self.__elemento = elemento
  def getProximo(self):
    return self.__proximo
  def setProximo(self, proximo):
    self.__proximo = proximo
  def criarElemento(self, chave, nome):
    self.__elemento = Elemento(chave, nome)
  def criaNo(self, chave, nome):
    self.criarElemento(chave, nome)
    self.__proximo = None
  def getValores(self):
    return self.__elemento.getValores()
  