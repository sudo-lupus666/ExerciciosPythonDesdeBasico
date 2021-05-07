'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
 área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
 que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
 de latas de tinta a serem compradas e o preço total.'''

from decimal import *

 def calculo_da_qtdd_tinta():

        print('Esse software determina quantas latas de tinta você precisará usar para pintar a sua parede e qual será o custo final**')

        tamanho_parede = input('Informe qual é a area da parede a ser pintada, em m2: ')

        def qtdd_tinta():
            qttd_tinta = tamanho_parede / 3
            return qttd_tinta

        def qtdd_latas():
            qtdd_latas = qtdd_tinta() / 18
            return qtdd_latas

        def orcamento():
            custo = qtdd_latas() * 80

        def teste():
            print (f'tamanho parede: {tamanho parede()}, qtdd tinta: {qtdd_tinta()}, qtdd latas: {qtdd latas()}, orcamento {orcament()}')

        teste()
        
     calculo_da_qtdd_tinta()