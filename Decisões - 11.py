#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
#contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
#baseado no salário atual:
#alários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

from decimal import *

def calcula_salario():

    print("** Programa que calcula os novos salários dos funcionários das organizações Tabajara**")
    
    def entrada():
        salario_atual = float(input("Informe o salário atual do funcionário: "))
        return salario_atual

    def calcula_aumento():
        salario = entrada()
        if salario <= 280: aumento = salario * 0.20
        elif salario > 280 and salario < 700: aumento = salario * 0.15
        elif salario >= 700 and salario < 1500:  aumento = salario * 0.10 
        else:  aumento = salario * 0.05
        return aumento

    def porcentagem_aumento():
        salario = entrada()
        if salario <= 280: mensagem_aumento = '20%'
        elif salario > 280 and salario < 700: mensagem_aumento = '15%'
        elif salario >= 700 and salario < 1500: mensagem_aumento = '10%'
        else: mensagem_aumento = '05%'
        return mensagem_aumento

    def mensagem():
        return (
            f'Prezado funcionário, o seu salário '
            f'anterior era de R$ {entrada()}, o seu aumento foi de R$ {calcula_aumento()} e '
            f'a porcentagem do seu aumento foi de {porcentagem_aumento()}. O seu novo salário é '
            f' {entrada() + calcula_aumento()}'
        )

    print (mensagem())

calcula_salario()
