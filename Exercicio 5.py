#Exercicio 5

def exercicio5():
    print("Programa conversor de metros para centímetros")
    medida = int(input("Digite a medida em metros que você deseja converter: "))
    
    def medidaCentimetros():
        conversao = (medida * 100)
        return conversao 

    print (f'{medida} metros são {medidaCentimetros()} em centímetros')
    
exercicio5()