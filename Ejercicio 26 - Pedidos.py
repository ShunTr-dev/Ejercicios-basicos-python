# -*- coding: utf-8 -*-

#--python 2.7.10

class produto:
	def __init__(self, nome, prezo):
			self.nome = nome
			self.prezo = prezo
			
lista_produtos = []
texto_opcions = ""

while not texto_opcions == "detener":
	texto_opcions = ""
	texto_opcions = raw_input("Que desea, introducir ou listar produtos? : ")
	
	if texto_opcions == "introducir":
		while True:
			nome_pro = ""
			nome_pro = raw_input("Introduza o nome do producto: ")
			if nome_pro == "stop":
				break
			precio_pro = raw_input("Introduza o prezo do produto: ")
			if precio_pro == "stop":
				break
			nome_pro = nome_pro.replace(" ", "")
			precio_pro = precio_pro.replace(" ","")
			n_produto = produto(nome_pro,precio_pro)
			if n_produto.nome != "" and n_produto.prezo != "":
				lista_produtos.append(n_produto)
				lista_produtos = sorted(lista_produtos, key=lambda produto: produto.nome)

	if texto_opcions == "listar":
			for i in lista_produtos:
				print(">>> " + i.nome + " : " + i.prezo + " euros")
			
		
		
