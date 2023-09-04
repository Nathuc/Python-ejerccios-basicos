import random # Importamos el módulo random para generar números aleatorios.

# Definimos una función llamada adivina_el_numero que toma un argumento x.

def adivina_el_numero(x):
    print("""========================================= 
Bienvenido al juego
Debes intentar adiviar el valor del número 
===========================================""")
    
    numero_aleatorio = random.randint(1,x)

    prediccion = 0 # Inicializamos la variable prediccion en 0.

# Comenzamos un bucle while que se ejecuta hasta que el jugador adivine correctamente.
    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))
        if prediccion < numero_aleatorio:
            print("Intenta otra vez este número es muy pequeño")
        elif prediccion >numero_aleatorio:
            print("Intenta otra vez este numero esmuy grande")
    print(f"""Felicitaciones adivinaste es número {numero_aleatorio} correctamente!
          
          
          ⭐⭐⭐⭐⭐⭐⭐⭐""")   

# Llamamos a la función adivina_el_numero con un argumento de 50.
adivina_el_numero(50)
