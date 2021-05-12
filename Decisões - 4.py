#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def verifica_vogalConsoante(): 

    print ("**Programa que verifica se uma letra pertence à família das vogais ou das consoantes**")
    letra = (input("Por favor, informe a letra que você deseja que seja verificada: ")).lower()

    def validador():
        dicionario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
        'j','k','l','m','n','o','p','q','r','s','t', 'u', 'v', 'w', 'x', 'y', 'z']
        if letra in dicionario: return True
        else: return False

    def vogalOuConsoante():
        vogais = ['a', 'e', 'i', 'o', 'u']
        if validador(): 
            if letra in vogais: return "vogal" 
            else: return "consoante"
        else: return False

    def mensagemUser():
        if vogalOuConsoante() == "vogal": return f"A letra {letra} é uma vogal."
        elif vogalOuConsoante() == "consoante": return f"A letra {letra} é uma consoante."
        else: return "caracter inválido"

    print (mensagemUser())
    
verifica_vogalConsoante()