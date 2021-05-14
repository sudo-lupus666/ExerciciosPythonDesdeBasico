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
        return numeros, numeros_sortidos
    
    def retorno_user():
        for item1, item2 in verificaMaior():
            print (item1, item2[0])
    
    retorno_user()

analisaNumero()