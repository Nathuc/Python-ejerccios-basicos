# Conversor de de pesos colombianos, mexicanos y argentinos a dolares 🤑 """
# Se debe ajustar los factores de conversión a la fecha actual


def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuatos pesos "+ tipo_pesos +" tienes?:")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares" )


menu = """
Bienveenido al conversor de monedas 💸
Seleccione 
1- pesos colombianos
2 - pesos argentinos 
3- pesos mexicanos
Elija una opción:"""

opcion = int(input(menu))

if opcion == 1:
  conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion ==3:
    conversor("Mexicanos", 24)
else:
    print('ingrese una opcion valida')
    
