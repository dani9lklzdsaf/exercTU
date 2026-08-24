# Aqui um exemplo de teste manual da função buscaSequencial
# O seu exercício deve utilizar a biblioteca unittest para criar testes unitários

import buscaSequencial as bs
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v = int(input("Digite um valor para buscar: "))
r = bs.buscaSequencial(a, v)
if r != -1:
  print(f"Valor {v} encontrado na posição {r}.")
else:
  print(f"Valor {v} não encontrado.")
