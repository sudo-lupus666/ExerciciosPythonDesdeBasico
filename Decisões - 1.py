#Faça um Programa que peça dois números e imprima o maior deles.

from decimal import *

def verifica_tamanho():

    print ("**Programa - retorna o maior**")
    print ("**Informe dois números. O programa retornará o maior**")

    numero1 = float(input("Informe o primeiro número: "))
    numero2 = float(input("Informe o segundo número: "))
    def retorna_maior():
        if numero1 > numero2:
            return round(numero1,)
        else: return round(numero2,)

    print (f"** O maior número é o {retorna_maior()}**")

verifica_tamanho()
