#Faça um Programa que leia três números e mostre-os em ordem decrescente.

from decimal import *

def analisa_numeros():

    print ("**Programa - lê 3 preços e devolve em ordem decrescente**")

    def entradas():
        numeros = []
        qtdd_numero = 0
        while qtdd_numero != 3:
            numero = float(input("Insira um número: "))
            numeros.append(numero)
            qtdd_numero += 1
        return sorted(numeros, reverse=True)

    def retorna_numeros():
        return f' Os números são {entradas()}'

    print (retorna_numeros())

analisa_numeros()