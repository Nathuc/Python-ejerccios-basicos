#En este codigo genera contraseñas aleatorias y luego muestra la contraseña generada en la consola
#Usaremos la libreria Ramdon para selecionar de forma aleatoria los caracteres en la contraseña  
#Lo primero que encontraras sera la función que contiene los letras numeros y simbolos que vamos a usar
#Dentro de esta función tambien se definira el tamaño de la contraseña y se almacenara como una cadena en la variable contrasena 
#Por ultimo se definira lo que el usuario vera en consola al ejecutatar el codigo 

import random
def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D' ,'E',' F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T','U', 'V', 'W','X','Y','Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    
    caracteres = mayusculas + minusculas + numeros + simbolos 
    
    contrasena = []

    for i in range(15):
        caracter_random =  random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('tu nueva contrasena es: ' + contrasena + """
    ❤️ ⏲️""") 


if __name__ ==  '__main__':
    run()