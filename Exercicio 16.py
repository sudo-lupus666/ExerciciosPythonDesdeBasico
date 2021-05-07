'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
 área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
 que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
 de latas de tinta a serem compradas e o preço total.'''

from decimal import *

def calculo_da_qtdd_tinta():

    print('Esse software determina quantas latas de tinta você precisará usar para pintar a sua parede e qual será o custo final**')

    tamanho_parede = int(input('Informe qual é a area da parede a ser pintada, em m2: '))

    def qtdd_tinta():
        qttd_tinta = round(tamanho_parede / 3, 1)
        return qttd_tinta

    def qtdd_latas():
        qtdd_latas = int(qtdd_tinta() / 18 + 1)
        return qtdd_latas

    def orcamento():
        custo = qtdd_latas() * 80
        return custo

    def teste():
        print (f'A sua parede de tamanho {tamanho_parede}m2 necessitará de {qtdd_tinta()} litros de tinta. Você precisa, portanto, adquirir {qtdd_latas()} lata(s) de tinta. Você irá gastar R$ {orcamento()} reais, em nossa loja')

    teste()
        
calculo_da_qtdd_tinta()