import random
def flipTheCoin():

    def jogaMoeda():
        elementoRandomico = (random.randrange(2,4,1)) % 2
        pares = 2 % 1               
        if elementoRandomico == pares: return "cara"
        else: return "coroa"

    def mensagemUser():
        return f"Nessa jogada, deu {jogaMoeda()}."
    
    print (mensagemUser())

flipTheCoin()