# -*- coding: utf-8 -*-

#--python 2.7.10

class produto:
	def __init__(self, nome, prezo):
			self.nome = nome
			self.prezo = prezo
			
lista_produtos = [produto("leite", 5),produto("galleta", 1), produto("chocolate", 20), produto("laranxa", 2)]
texto_opcions = ""

while not texto_opcions == "detener":
	texto_opcions = ""
	texto_opcions = raw_input("Que desea, introducir, listar ou borrar produtos? : ")
	
	if texto_opcions == "introducir":
		while True:
			nome_pro = ""
			nome_pro = raw_input("Introduza o nome do producto: ")
			if nome_pro == "stop" or nome_pro.replace(" ","") == "":
				break
			precio_pro = raw_input("Introduza o prezo do produto: ")
			if precio_pro == "stop" or precio_pro.replace(" ","") == "":
				break
			nome_pro = nome_pro.replace(" ", "")
			precio_pro = precio_pro.replace(" ","")
			try:
				n_produto = produto(nome_pro,int(precio_pro))
				produto_valido = True
			except:
				n_produto = produto(nome_pro,precio_pro)
				produto_valido = False
				print(">> Inserte un numero de prezo!")
			for i in lista_produtos:
				if nome_pro == i.nome:
					print(">> Xa existe este produto!")
					produto_valido = False
					break
			if produto_valido:
				lista_produtos.append(n_produto)
				
	if texto_opcions == "listar":
		lista_produtos = sorted(lista_produtos, key=lambda produto: produto.nome)
		for i in lista_produtos:
			print(">>> " + i.nome + " : " + str(i.prezo) + " euros")
				
	if texto_opcions == "borrar":
		texto_borrado = ""
		texto_borrado = raw_input("Introduce o nome do produto a borrar: ")
		num_lista = 0
		for i in lista_produtos:
			if i.nome == texto_borrado:
				del lista_produtos[num_lista]
				print(">>> Produto borrado!")
				break
			num_lista += 1
			if num_lista == len(lista_produtos):
				print(">>> Non se encontraron produtos con ese nome")