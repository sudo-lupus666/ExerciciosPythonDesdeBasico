#Faça um programa que pergunte o preço de três produtos e informe qual 
#produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

from decimal import *

def analisaPreco():

    print ("**Programa - lê 3 preços e devolve o menor**")

    def entradas():
        precos = []
        produto_numero = 0
        while produto_numero != 3:
            preco = float(input("Insira o preço do produto: "))
            precos.append(preco)
            produto_numero += 1
        return precos

    def retornaPreco():
        return f' Você deve comprar o produto de preço R$ {(sorted(entradas())[0])}'

    print (retornaPreco())

analisaPreco()