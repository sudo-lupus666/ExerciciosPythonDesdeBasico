#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def calcula_quadrado():
    lado = int(input("Informe o lado do quadrado cuja área você deseja: "))

    def calcula_area():
        area = lado * lado
        return area
    area = calcula_area()

    def calcula_area_vezes_2():
        area_dobro = area * 2
        return area_dobro

    print (f'A area do quadrado de lado {lado} é {calcula_area()} e a área em dobro é {calcula_area_vezes_2()}')

calcula_quadrado()