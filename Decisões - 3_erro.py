#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - 
#Feminino, M - Masculino, Sexo Inválido.

def verifica_sexualidade(): 

    print ("**Programa que verifica o input de um user e determina se esse user é homem ou mulher**")
    identificacao = (input("**Por favor, digite 'f' para sexo feminino ou 'm' para sexo masculino: **")).lower()

    def validador_input():
        if identificacao == 'f' or 'm': return True
        else: return False

    print (validador_input())        

    def define_sexo():
        if validador_input() == True:
            if identificacao == 'f': return 'feminino'
            else: return 'masculino'
        else: print ('Opção inválida')  

    def resposta():
        print (f' De acordo com o que você nos infornou, você é uma pessoa do sexo {define_sexo()}')

    resposta()

verifica_sexualidade()
