#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde 
# os valores para cima, isto é, considere latas cheias.

from decimal import *

def calculo_da_qtdd_tinta():

    print('Esse software determina quantas latas de tinta você precisará usar para pintar a sua parede e qual será o custo final**')

    tamanho_parede = int(input('Informe qual é a area da parede a ser pintada, em m2: '))

    def qtdd_tinta():
        qttd_tinta = round(tamanho_parede / 3, 1)
        return qttd_tinta

    def qtdd_latas():
        qtdd_latas = round(qtdd_tinta() / 18 + 1)
        return qtdd_latas

    def plural_latas():
        if qtdd_latas() > 1:
            return 'latas'
        else: return 'lata'

    def plural_galoes():
        if qtdd_galoes() > 1:
            return 'galões'
        else: return 'galão'        

    def qtdd_galoes():
        qtdd_galoes = round(qtdd_tinta() / 3.6 + 0.5)
        return qtdd_galoes

    def orcamento():
        custo = qtdd_latas() * 80
        return custo

    def retorno_user():
        print (f'A sua parede de tamanho {tamanho_parede}m2 necessitará de {qtdd_tinta()} litros de tinta. Você precisa, portanto, adquirir {qtdd_latas()} {plural_latas()} de tinta ou, se preferir, {qtdd_galoes()}{plural_galoes()}. Você irá gastar R$ {orcamento()} reais, em nossa loja')

    retorno_user()
        
calculo_da_qtdd_tinta()