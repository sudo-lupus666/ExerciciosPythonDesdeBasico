#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58


from decimal import *

def pesoIdeal():

    print ("**Programa para informar o seu peso ideal**")

    altura = (input("Informe a sua altura: "))

    def calcula_peso_ideal():
        peso_ideal = altura * 72,7 - 58
        return peso_ideal

    print (f'Considerando a altura de {altura} metros, o seu peso ideal é {calcula_peso_ideal()}')

pesoIdeal()