'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do 
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que 
o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao 
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme 
o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

import decimal

def folha_pagamento():

        print ("**Programa que realiza os cálculos referentes à folha de pagamento**")

        def entradas():
                hora_valor = float(input('informe o valor que você recebe por hora: '))
                quantidade_horas = int(input('Informe a quantidade de horas que você trabalha por mês: '))
                return hora_valor * quantidade_horas

        salario = entradas()

        def calculo_fgts():
                fgts = salario * 0.11
                return fgts

        fgts = calculo_fgts()        

        def calculo_IR():
                imposto_de_renda = 0
                if salario <= 900: imposto_de_renda = 0
                elif salario > 900 and salario <= 1500: imposto_de_renda = salario * 0.05
                elif salario > 1500 and salario <= 2500: imposto_de_renda = salario * 0.1
                elif imposto_de_renda: salario * 0.2
                return imposto_de_renda 

        IR = calculo_IR()

        def contribuicao_sindical():
                desconto = salario * 0.03
                return desconto

        sindicato = contribuicao_sindical()
        descontos = sindicato + IR   

        def calcula_salario():
                print (f'Prezado colaborador, o seu salário bruto é: R$ {salario}. '
                f'Do seu salário são descontados: 1 - O imposto de renda no valor de R$ {IR}.' 
                f'2 - A contribuição sindical, no valor de R$ {sindicato} e'
                f'3 - A contribuição para o FGTS, no valor de R$ {fgts}'
                f'O seu salário líquido é, portanto, R$ {salario - descontos}.')

        calcula_salario()

folha_pagamento()