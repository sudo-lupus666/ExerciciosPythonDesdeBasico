#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, 
#return 0(for languages that do have them)

def teste():

    numberx = 20
    if numberx <= -1:
        print (0)
    else:    
        def lista_de_numeros_abaixo_do_input_user():
                lista = []
                input_lista = numberx
                while input_lista != 0: 
                    lista.append(input_lista) 
                    input_lista -=1
                return lista

        def multiplos():
                multiplos5 = 5 % 1
                multiplos3 = 3 % 1
                soma = []
                lista = lista_de_numeros_abaixo_do_input_user()
                for numero in lista:
                    if numero % 3 == multiplos3 or numero % 5 == multiplos5: soma.append(numero)
                else: pass
                return soma  

        def soma():
            lista = sum(multiplos())
            return lista

        print (soma())

teste()
''''
def solution(number):
    if number <= -1: return 0
    else:  
        number -=1
        lista = []
        while number != 0: 
            lista.append(number) 
            number -=1
        soma = []
        for number in lista:
            if number % 3 == 0 or number % 5 == 0: soma.append(number)
            else: pass  
        lista2 = []
        lista2 = sum(soma)
        return lista2  '''