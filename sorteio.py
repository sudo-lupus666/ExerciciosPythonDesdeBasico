import random

def entrada():
lista = []
aluno = input('Entre com a lista de alunos que participarão da competição: .Quando terminar, digite "fim"')
while aluno != 'fim':
    lista.append(aluno)
return lista

deflista_de_participantes = entrada()

tamanho_lista = len(lista)

def sorteio():
    lista = [lista_de_alunos]
    randomico = random.randrange(1,tamanho_lista,1)
    sorteado = lista(randomico)
    lista.remove(sorteado)
    return sorteado

def mensagem_user:
    print (f"O aluno 1 é o(a) {sorteio()} 