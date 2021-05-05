#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

def converte_temp():

    print ("**Bem-vindo ao seu software de conversão de temperaturas**")
    temp_fahrenheit = int(input("Insira a temperatura em Fahrenheit: "))

    def conversor_temp():
        calculo_1 = (temp_fahrenheit - 32)/9
        temperatura_em_Celcios = calculo_1 * 5
        return temperatura_em_Celcios

    temp_celcius = conversor_temp()

    print (f'{temp_fahrenheit} graus Fahrenheit equivalem a {temp_celcius} graus Celcius')

converte_temp()    

#Melhorar esse código, retrabalhando as casas decimais da resposta.