#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido

from decimal import *

def calcula_salario():

    print ('**Esse é um software que calcula o seu salário**')

    salario_hora = int(input("Informe o quanto você ganha por hora: "))
    horas_trabalhadas = int(input("Informe qunantas horas você trabalha por mês: "))

    def calculo_do_salario():
        salario = salario_hora * horas_trabalhadas
        return salario

    def desconto_imposto_de_renda():
        descontoImpostodeRenda =  calculo_do_salario() * 0.11
        return descontoImpostodeRenda       

    def desconto_INSS():
        descontoInss = calculo_do_salario() * 0.08
        return descontoInss
                        
    def desconto_Sindicato():
        descontoSindicato = calculo_do_salario() * 0.05
        return descontoSindicato

    def salario_liquido():
        salarioLiquido = calculo_do_salario() - desconto_imposto_de_renda() - desconto_INSS()      
        return salarioLiquido

    def informe_rendimentos_usuario():
        print (f"Seu salário bruto é: R$ {calculo_do_salario()}, o desconto do imposto de renda é R${desconto_imposto_de_renda()}, o desconto do INSS é R$ {desconto_INSS()}, o desconto do sindicato é R$ {desconto_Sindicato()}. O seu salário líquido é:{salario_liquido()}")
        
    informe_rendimentos_usuario()

calcula_salario()