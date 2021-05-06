#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

def calcula_salario():

    print ('**Esse é um software que calcula o seu salário**')

    valor_hora = int(input("Informe o quanto você ganha por hora: "))
    horas_trabalhadas = int(input("Informe qunantas horas você trabalha por mês: "))

    def calculo_do_salario():
        salario = valor_hora * horas_trabalhadas
        return salario

    print (f'Você ganha {calculo_do_salario()} reais por mês')

calcula_salario()
