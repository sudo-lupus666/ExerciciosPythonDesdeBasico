def exercicio1():
    print ("helllo, world")

def exercicio2():

    print ("Escreva um número")
    numero = input("Digite um número: ")
    print (f'O número digitado foi {numero}.')

def exercicio3():

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    soma = numero1 + numero2
    print (f'A soma desses números é: {soma}')

def exercicio4():

    print("Programa de calculo de média final")

    media1 = int(input("Digite a média do primeiro bimestre: "))
    media2 = int(input("Digite a média do segundo bimestre: "))
    media3 = int(input("Digite a média do terceiro bimestre: "))
    media4 = int(input("Digite a média do quarto bimestre: "))

    def media_dos_bimestres():
        totalPontos = media1 + media2 + media3 + media4
        mediaFinal = totalPontos / 4
        return mediaFinal
    
    print (f'A média final é {media_dos_bimestres()}')

exercicio4()
    