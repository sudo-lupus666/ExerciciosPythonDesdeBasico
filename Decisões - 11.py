'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

import decimal

def calcula_salario():

    print("** Programa que calcula os novos salários dos funcionários das organizações Tabajara**")
    
    def entrada():
        salario_atual = input(float("Informe o salário atual do funcionário: "))
        return salario_atual

    def calcula_salario():
        salario = entrada()
        if salario <= 280: salario *= 1.20
        elif salario > 280 and salario < 700: salario *= 1.15
        elif salario >= 700 and salario < 1500: salario *= 1.10 
        else: salario *= 1.05
        return salario

    def mensagem():
        salario = entrada()
        if entrada() == "m": return f"Bom dia!"
        elif entrada() == "v": return f"Boa tarde!"
        elif entrada() == "n": return f"Boa noite!"
        else: return f"turno inválido, digite uma opção válida"

#    while entrada() != "m" or entrada() != "v" or entrada() != "n": entrada()
    print (mensagem())

turno_estudo()

