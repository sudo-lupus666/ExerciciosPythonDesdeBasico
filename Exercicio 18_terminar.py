#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

from decimal import *

def verifica_tamanho():

    print ("**Programa para os Naruteiros de Plantão**")
    print ("**Informe o tamanho do episódio de anime e a velocidade da sua internet**")
    print ("*Esse programa determinará quanto tempo você deverá esperar até poder assistir o episódio")

    tamanho_arq = float(input("**Informe o tamanho do arquivo: **"))
    velocidade_net = float(input("**Informe a velocidade da sua internet: "))

    def calcula_tempo():
        tamanho_bits = tamanho_arq * 8
        tempo_total = tamanho_bits / velocidade_net
        tempo_segundos = tempo_total / 60 
        tempo_minutos = tempo_segundos / 60
        return round(tempo_minutos,3)

    print (f"O download desse arquivo será terminado em {calcula_tempo()} minutos")

verifica_tamanho()
