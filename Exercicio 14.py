#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o 
# rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido 
# pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o 
# valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

def calcula_multa():

    print("**Esse é o seu software para calcular a multa sobre o excesso de pesca**")
    pesca_dia = int(input("Insira a quantidade em quilos de peixe que você pescou hoje: "))

    def verifica_multa():
        limite_diario = 50
        pesca_excedente = pesca_dia - limite_diario
        return pesca_excedente

    def calcula_multa():
        multa = verifica_multa() * 4
        return multa

    def informe_de_multa_para_o_Joao():
        if verifica_multa() > 1:
            print(f'Você pescou {verifica_multa()} quilos além do limite e deverá pagar uma multa de {calcula_multa()} reais.')
        else: 
            print ('Você pescou uma quantidade de peixes dentro do limite, portanto não precisará pagar multa hoje.')

    informe_de_multa_para_o_Joao()

calcula_multa()