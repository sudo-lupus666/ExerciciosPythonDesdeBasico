#Faça um Programa que peça a temperatura em 
#graus Celsius, transforme e mostre em graus Fahrenheit.

def conversor_Celsius_p_Fahrenheit():
    print ("**Bem-vindo ao conversor de Celsius para Fahrenheit**")
    temp_celsius = int(input("Insira a temperatura que você deseja converter de Celsius para Fahrenheit: "))

    def conversor():
        temp_fahrenheit = (((temp_celsius / 5)*9) + 32)
        return temp_fahrenheit
    
    temp_fahrenheit = conversor()
    
    print (f'{temp_celsius} graus célsius são equivalentes a {temp_fahrenheit} graus Fahrenheit')

conversor_Celsius_p_Fahrenheit()