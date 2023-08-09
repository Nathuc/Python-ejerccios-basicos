#Este programa determina si un número es primo 1️⃣2️⃣3️⃣.
# Siga las instrucciones del programa. 

#Definimos la función donde se almacenara el parametro 
#que retornara TRUE si el parametro cumple con las condiciones para ser primo y FALSE de ser lo contrario.

def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

# Definimos la función que interactuara con el usuario.
def run():
    numero = int(input ('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    run()
