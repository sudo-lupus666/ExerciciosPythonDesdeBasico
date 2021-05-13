#Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

from decimal import *

def aprovadoReprovado():

    print ("**Programa - Verifica aprovação ou reprovação**")
    print ("**Informe as suas duas médias semestrais. O programa informará se você foi ou não aprovado**")

    media1 = float(input("Informe a média do primeiro semestre: "))
    media2 = float(input("Informe a média do segundo semestre: "))
#Deixei dois métodos de aprovação, só para fins de teste; para usar o primeiro é só descomentar e comentar o segundo.    
    '''
    def verificaAprovacao():
        mediafinal = (media1 + media2) / 2
        if mediafinal < 7: return f'Sua média foi {mediafinal}, portanto você foi reprovado'
        elif mediafinal == 10: return f' Sua média foi {mediafinal}. Você foi aprovado com louvor!' 
        else: return f'Sua média foi {mediafinal}. Você foi aprovado, parabéns!'
    '''
    def verificaAprovacao():
        mediafinal = (media1 + media2) / 2
        if mediafinal < 7: return f'Sua média foi {mediafinal}, portanto você foi reprovado'
        elif mediafinal >= 7 and mediafinal < 10: return f'Sua média foi {mediafinal}. Você foi aprovado, parabéns!'    
        else: return f' Sua média foi {mediafinal}. Você foi aprovado com louvor!'     

    print (verificaAprovacao())

aprovadoReprovado()