import random

def flipTheCoin():

    def jogaMoeda():
        elementoRandomico = (random.randrange(2,4,1)) % 2
        pares = 2 % 1               
        if elementoRandomico == pares: return "Heads"
        else: return "Tails"

    def mensagemUser():
        return f"You've got {jogaMoeda()}."
    
    print (mensagemUser())

flipTheCoin()