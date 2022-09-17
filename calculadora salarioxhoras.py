#CALCULADORA DE SALARIO POR HORAS 💸 

'''Segun la cantidad de horas trabajadas y el valor por horas ejecute un 
programa que calcule el salario por horas del trabajador'''


nombre = str(input('''Bienvenido a la calculdora de salario por horas
si desea calcular su salario por favor ingrese su nombre: '''))
horas = int(input('escriba la cantidad de horas trabajadas: '))
coste_horas = float(input('Escriba el costo x horas de su salario: '))
paga = print(nombre, ' ','su paga es de: $',horas*coste_horas)