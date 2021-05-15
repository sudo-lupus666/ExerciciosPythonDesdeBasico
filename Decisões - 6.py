#Faça um Programa que leia três números e mostre o maior deles.
    
from decimal import *

def analisaNumero():

    print ("**Programa - lê 3 números e devolve o maior**")

    def entrada():
            numeros = []
            sequencia = 1
            while len(numeros) != 3:
                numero = float(input(f"Informe o número {sequencia}: "))
                numeros.append(numero)
                sequencia +=1         
            return numeros

    def verificaMaior():
        numeros = entrada()
        numeros_sortidos = sorted(numeros)
        listas = (numeros, numeros_sortidos)
        return listas
    
    def retorno_user():
        for lista1, lista2 in verificaMaior():
            print (lista1, lista2)
    
    retorno_user()

analisaNumero()