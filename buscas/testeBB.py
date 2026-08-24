# Aqui um exemplo de teste manual da função buscaBinaria
# O seu exercício deve utilizar a biblioteca unittest para criar testes unitários

import buscaBinaria as bb
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v = int(input("Digite um valor para buscar: "))
r = bb.buscaBinaria(a, v)
if r != -1:
  print(f"Valor {v} encontrado na posição {r}.")
else:
  print(f"Valor {v} não encontrado.")
