import random

'''def entrada():
    lista = []
    print ('Entre com a lista de alunos que participarão da competição')
    alunos = input('Insira a lista de alunos: ')
    for nome in alunos:
        lista.append(nome)
    return lista'''

def entrada():
    lista = []
    print ('Entre com a lista de alunos que participarão da competição. Quando terminar, digite "fim"')
    aluno = input('Insira o nome do primeiro aluno: ')
    while aluno != 'fim':
        lista.append(aluno)
        aluno = input ('Insira o nome do próximo aluno: ')
    return lista 

lista_de_participantes = entrada()
tamanho_lista = len(lista_de_participantes) -1

def sorteio1():
    tamanho_lista = len(lista_de_participantes)
    randomico = random.randrange(0,tamanho_lista,1)
    sorteado1 = lista_de_participantes[randomico]
    lista_de_participantes.remove(sorteado1)
    return sorteado1

tamanho_lista = len(lista_de_participantes)

def sorteio2():
    tamanho_lista = len(lista_de_participantes)
    randomico = random.randrange(0,tamanho_lista,1)
    sorteado2 = lista_de_participantes[randomico -1]
    lista_de_participantes.remove(sorteado2)
    return sorteado2

sorteado1 = sorteio1()
sorteado2 = sorteio2()    

def mensagem_user():
    return f'O aluno 1 é o(a) {sorteado1}. O participante 2 é o(a) {sorteado2}'

print (mensagem_user())