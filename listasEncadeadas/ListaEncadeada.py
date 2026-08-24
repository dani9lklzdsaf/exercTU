from Elemento import Elemento
from No import No
class ListaEncadeada:
  def __init__(self):
    self.__cabeca = No()
  def listaVazia(self):
    return self.__cabeca.getProximo() == None
  def criaNo(self, chave, nome):
    no = No(Elemento(chave, nome))
    return no
  def inserNoInicioNo(self, no):
    no.setProximo(self.__cabeca.getProximo())
    self.__cabeca.setProximo(no)
  def insereNoInicio(self, chave, nome):
    no = self.criaNo(chave, nome)
    self.inserNoInicioNo(no)
  def retiraNoInicio(self):
    ret = None
    if not self.listaVazia():
      ret = self.__cabeca.getProximo()
      self.__cabeca.setProximo(ret.getProximo())
    return ret
  def inserNofimNo(self, no):
    anterior = self.__cabeca
    proximo  = self.__cabeca.getProximo() 
    while proximo != None:
      anterior = proximo
      proximo  = proximo.getProximo()
    anterior.setProximo(no)
  def insereNoFim(self, chave, nome):
    no = self.criaNo(chave, nome)
    self.inserNofimNo(no)
  def retiraNoFim(self):
    ret = None
    if not self.listaVazia():
      anterior = self.__cabeca
      proximo  = self.__cabeca.getProximo()
      while proximo.getProximo() != None:
        anterior = proximo
        proximo  = proximo.getProximo()
      ret = proximo
      anterior.setProximo(None)
    return ret
  def inserePorChaveNo(self, no):
    anterior = self.__cabeca
    proximo  = self.__cabeca.getProximo()
    while proximo != None and proximo.getElemento().getChave() < no.getElemento().getChave():
      anterior = proximo
      proximo  = proximo.getProximo()
    no.setProximo(proximo)
    anterior.setProximo(no)
  def inserePorChave(self, chave, nome):
    no = self.criaNo(chave, nome)
    self.inserePorChaveNo(no) 
  def retiraPorChave(self, chave):
    ret = None
    if not self.listaVazia():
      anterior = self.__cabeca
      proximo  = self.__cabeca.getProximo()
      while proximo != None and proximo.getElemento().getChave() != chave:
        anterior = proximo
        proximo  = proximo.getProximo()
      if proximo != None and proximo.getElemento().getChave() == chave:
        ret = proximo
        anterior.setProximo(proximo.getProximo())
    return ret
  def mostraLista(self):
    proximo = self.__cabeca.getProximo()
    while proximo != None:
      print(proximo.getValores())
      proximo = proximo.getProximo() 
  def quantidadeNos(self):
    count = 0
    proximo = self.__cabeca.getProximo()
    while proximo != None:
      count = count + 1
      proximo = proximo.getProximo()
    return count
  def buscaPorChave(self, chave):
    ret = None
    pos = -1
    proximo  = self.__cabeca.getProximo()
    while proximo != None and proximo.getElemento().getChave() != chave:
      proximo  = proximo.getProximo()
      pos = pos + 1
    if proximo != None and proximo.getElemento().getChave() == chave:
      ret = proximo
    else:
      pos = -1
    return (ret, pos)
  def preOrdem(self):
    ret = []
    proximo  = self.__cabeca.getProximo()
    while proximo != None:
      ret.append(proximo.getValores())
      proximo  = proximo.getProximo()
    return ret
  def posOrdem(self):
    ret = []
    proximo  = self.__cabeca.getProximo()
    while proximo != None:
      ret.insert(0, proximo.getValores())
      proximo  = proximo.getProximo()
    return ret  
  def emOrdem(self):
    ret = []
    proximo  = self.__cabeca.getProximo()
    while proximo != None:
      ret.append(proximo.getValores())
      proximo  = proximo.getProximo()
    ret.sort(key=lambda x: x[0])
    return ret