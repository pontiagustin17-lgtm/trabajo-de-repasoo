"""1.	Consigna:
Un cine necesita un programa para administrar las funciones y la cantidad de butacas disponibles. Usar listas paralelas peliculas[] y butacas[].
El programa debe utilizar un menú con bucle while que permita al usuario elegir diferentes opciones hasta que decida salir.


Opciones del menú:
Agregar película:
El usuario ingresa el nombre de la película y la cantidad inicial de butacas.
Validar que el nombre no esté vacío ni repetido.
La cantidad de butacas debe ser un número entero mayor o igual a 0.
Consultar butacas disponibles de una película:
El usuario ingresa el nombre de una película.
El programa muestra cuántas butacas le quedan disponibles.
Si no existe, informar al usuario.
Ver cartelera completa:
Mostrar todas las películas con la cantidad de butacas disponibles.
Listar películas sin butacas:
Mostrar únicamente aquellas películas cuyo número de butacas sea 0.
Reservar / Cancelar butacas:
El usuario ingresa el nombre de una película.
Elegir si desea:
Reservar → resta 1 butaca (si hay disponibles).
Cancelar → suma 1 butaca (libera un lugar).
Si no hay butacas para reservar o la película no existe, mostrar mensaje de error.
Salir:
Terminar la ejecución del programa.

"""
peliculas =[]
butacas =[]
#
while True:
    print("menu ")
    print("1 agregar peliculas ")
    print(" 2 agregar cantidad de butacas ")
    print ("3 nombre de la pelicula ")
    print("4 Consultar butacas disponibles de una película")
    print(" Reservar / Cancelar butacas")
    print("Ver cartelera completa")
    print("5  salir " )
    
    opcion = input("Elige una opción (1-6): ")
    if