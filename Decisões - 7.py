#Faça um Programa que leia três números e mostre o maior e o menor deles.

from decimal import *

def analisaNumero():

    print ("**Programa - lê 3 números e devolve o maior e o menor**")

    def entrada():
        numeros = []
        sequencia = 1
        while len(numeros) != 3:
            numero = float(input(f"Informe o número {sequencia}: "))
            numeros.append(numero)
            sequencia +=1            
        return numeros
        
    def verifica_maior():
        lista = sorted(entrada())
        return lista

    def retorno_user():
        lista = sorted(verifica_maior())
        print (f'O maior número é o {lista[2]} e o menor número é o {lista[0]}.')
    
    retorno_user()

analisaNumero()