def exercicio6():

    print("Programa que calcula a área do círculo")
    raio = int(input("Informe o raio do círculo: "))

    def calcula_raio():
        raioaoquadrado = raio * raio
        area = 3.14 * raioaoquadrado
        return area
    
    print(f'A área de um círculo de raio {raio} é igual a {calcula_raio()}')

exercicio6()