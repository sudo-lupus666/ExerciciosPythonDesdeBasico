#Faça um Programa que peça um
#valor e mostre na tela se o valor é positivo ou negativo.

from decimal import *

def verifica_sinal(): 

    print ("**Programa que verifica se um número é positivo ou negativo**")

    numero1 = float(input("Informe um número: "))
    
    def verifica_positivoNegativo():
        parametro = 0 
        if numero1 < parametro: return True 
        else: return False

    def resposta():
        if verifica_positivoNegativo(): print (f'O número {round(numero1,1)} é um número negativo.')
        else: print (f'O número {round(numero1,1)} é um número positivo.')
    
    resposta()
verifica_sinal()