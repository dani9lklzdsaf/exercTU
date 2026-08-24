from ListaEncadeada import ListaEncadeada

def mostraMenu():
	print("\n--- Lista Encadeada ---")
	print("1 - Verificar se a lista esta vazia")
	print("2 - Inserir no inicio")
	print("3 - Inserir no fim")
	print("4 - Inserir por chave")
	print("5 - Retirar do inicio")
	print("6 - Retirar do fim")
	print("7 - Retirar por chave")
	print("8 - Buscar por chave")
	print("9 - Mostrar lista")
	print("10 - Mostrar quantidade de nos")
	print("11 - Mostrar pre-ordem")
	print("12 - Mostrar pos-ordem")
	print("13 - Mostrar em ordem")
	print("0 - Sair")

def leChave():
	return int(input("Chave: "))

def leDados():
	chave = leChave()
	nome = input("Nome: ")
	return chave, nome

def mostraNo(no):
	if no is None:
		print("Nenhum no encontrado.")
	else:
		print(no.getValores())

def executaOpcao(lista, opcao):
	if opcao == "1":
		print("A lista esta vazia." if lista.listaVazia() else "A lista nao esta vazia.")
	elif opcao == "2":
		chave, nome = leDados()
		lista.insereNoInicio(chave, nome)
	elif opcao == "3":
		chave, nome = leDados()
		lista.insereNoFim(chave, nome)
	elif opcao == "4":
		chave, nome = leDados()
		lista.inserePorChave(chave, nome)
	elif opcao == "5":
		mostraNo(lista.retiraNoInicio())
	elif opcao == "6":
		mostraNo(lista.retiraNoFim())
	elif opcao == "7":
		mostraNo(lista.retiraPorChave(leChave()))
	elif opcao == "8":
		no, posicao = lista.buscaPorChave(leChave())
		mostraNo(no)
		print("Posicao:", posicao)
	elif opcao == "9":
		lista.mostraLista()
	elif opcao == "10":
		print("Quantidade de nos:", lista.quantidadeNos())
	elif opcao == "11":
		print(lista.preOrdem())
	elif opcao == "12":
		print(lista.posOrdem())
	elif opcao == "13":
		print(lista.emOrdem())
	else:
		print("Opcao invalida.")

def main():
	lista = ListaEncadeada()
	while True:
		mostraMenu()
		opcao = input("Escolha uma opcao: ")
		if opcao == "0":
			print("Programa encerrado.")
			break
		try:
			executaOpcao(lista, opcao)
		except ValueError:
			print("Informe uma chave numerica.")

if __name__ == "__main__":
	main()
