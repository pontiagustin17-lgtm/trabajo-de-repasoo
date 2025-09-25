"""
Consigna 1 :
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
peliculas = [""]
butacas = [""]
while True:
    print("-----MENU-----")
    print("1) Agregar pelicula")
    print("2) Consulltar la cantidad de butacas para una pelicula")
    print("3) Ver cartelera completa")
    print("4) Listar peliculas sin butacas")
    print("5) Reservar / Cancelar butacas")
    print("6) Salir")
    opcion = int(input("Ingrese el numero de la operacion que desea realizar: "))
    if opcion == 1:
        peliculas.append = input("Ingrese el nombre de la pelicula: ")
        butacas.append = int(input("Ingrese la cantidad de butacas disponibles: "))
        if peliculas[-1] == "" or peliculas[-1] in peliculas[:-1]:
            print("Error, el nombre de la pelicula no puede estar vacio o repetido")
            peliculas.remove(-1)
            butacas.remove(-1)
    elif opcion == 6:
        break
    else:
        print("Opcion invalida, intente nuevamente")