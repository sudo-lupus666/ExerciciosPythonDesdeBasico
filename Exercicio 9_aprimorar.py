#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

def converte_temp():

    print ("**Bem-vindo ao seu software de conversão de temperaturas**")
    temp_fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))

    def conversor_temp():
        calculo_1 = (temp_fahrenheit - 32)/9
        temperatura_em_Celcios = calculo_1 * 5
        return round(temperatura_em_Celcios, 0)

    print (f'{temp_fahrenheit} graus Fahrenheit equivalem a {conversor_temp()} graus Celcius')

converte_temp()    

#Melhorar esse código, convertendo vírgulas para pontos