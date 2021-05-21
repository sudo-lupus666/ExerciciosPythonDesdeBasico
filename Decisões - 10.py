#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou 
# V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", 
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def turno_estudo():

    print("** Programa que verifica em qual turno você estuda e te retorna uma mensagem para melhorar o seu dia**")
    
    def entrada():
        turno = input("Informe em qual horário você estuda. Digite M para matutino, V para vespertino ou n para noturno: ").lower()
        return turno

    def mensagem():
        if entrada() == "m": return f"Bom dia!"
        elif entrada() == "v": return f"Boa tarde!"
        elif entrada() == "n": return f"Boa noite!"
        else: return f"turno inválido, digite uma opção válida"

#    while entrada() != "m" or entrada() != "v" or entrada() != "n": entrada()
    print (mensagem())

turno_estudo()