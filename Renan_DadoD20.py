import random
def rodaodado():

    def rodada():
        dado = random.randrange(1,21,1)
        return dado
        
    def mensagemUser():
        return f"Nessa jogada, deu {rodada()}."
    
    print (mensagemUser())

rodaodado()