"""trabajo de repaso"""

"""a) Nombre, edad y preguntas del día
Escribe un programa que pida al usuario su nombre y edad, muestre un mensaje de bienvenida y le pregunte dos cosas de su día (por ejemplo: si comió y si estudió). Finalmente, muestra un resumen.
b) Mantel para mesa
Escribe un programa que calcule cuánto mantel se necesita para cubrir una mesa rectangular. El usuario ingresa largo y ancho (en metros).
c) Conversor de minutos a horas
Pide al usuario un número de minutos y muestra cuántas horas y minutos equivalen.
"""
#punto A
edad=input("ingrese su edad: ")
nombre=input("ingrese su nombre: ")
print(f"Hola bienvenido, {nombre}")
comio = input("¿Comiste? ").lower()
estudio = input("¿Estudiaste? ").lower()
print(f"Entonces {comio} comiste y {estudio} estudiaste")

print("------")
#punto B 
largo = float(input("Ingrese el largo de la mesa(En centimetros): "))
ancho = float(input("Ingrese el ancho de la mesa(En centimetros): "))
largo_mantel = largo + 15
ancho_mantel = ancho + 15
print(f"El largo del mantel tiene que ser: {largo_mantel}")
print(f"El ancho del mantel tiene que ser: {ancho_mantel}")


print("--------")
#punto C
minutos = int(input("Ingrese una cantidad en minutos: "))
horas=minutos/60 
minutos %= 60
print(f"La equivalencia en horas es {horas}")

print("----------")

"""a) Velocidad del vehículo
Pide al usuario la velocidad a la que viaja (km/h) y muestra si va lento (<40), rápido (>120) o normal.
b) Mayor de edad con análisis de vida
Pide la edad y determina si es mayor de edad. Luego pregunta si trabaja y su pasatiempo, y muestra un mensaje final describiendo cómo es su vida.
c) Par o impar
Pide un número al usuario e indica si es par o impar.
"""
velocidad = int(input("Introduzca su velocidad en km/h: "))
if velocidad < 40:
    print("Vas lento")
elif velocidad > 120:
    print("Vas rápido")
else:
    print("Vas a una velocidad normal")
print("-------")

    #punto  B
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
trabaja = input("¿Trabajas? (sí/no): ")
pasatiempo = input("¿Cuál es tu pasatiempo? ")
print(f"\nTienes {edad} años, {'trabajas' if trabaja.lower() == 'sí' else 'no trabajas'} y tu pasatiempo es {pasatiempo}.")


# punto C
def condicional_c():
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

"""a) Números del 1 al 10 con for
Muestra los números del 1 al 10.
b) Suma del 1 al 100 con while
Calcula la suma de los números del 1 al 100.
c) Tabla de multiplicar
Pide un número y muestra su tabla de multiplicar del 1 al 10.
"""
for i in range(1, 11):
    print(i)
    
    
"""a) Suma hasta ingresar 0
Pide números hasta que se ingrese 0. Luego muestra la suma total.
b) Contraseña correcta
Pide una contraseña. Mientras no sea correcta, vuelve a pedirla.
c) Adivinar número secreto
Genera un número secreto y deja que el usuario lo adivine con pistas.
"""
suma = 0
while True:
    num = int(input('Ingrese un número (0 para terminar): '))
    if num == 0:
        break
    suma += num
print(f"La suma total es {suma}.")


# punto b
def bucle_cond_b():
    clave_correcta = "1234"
    clave = input("Ingrese la contraseña: ")
    while clave != clave_correcta:
        print("Contraseña incorrecta, intente de nuevo.")
        clave = input("Ingrese la contraseña: ")
    print("¡Contraseña correcta!")


# punto c 
import random
def bucle_cond_c():
    secreto = random.randint(1, 10)
    intento = int(input("Adivina el número secreto (1-10): "))
    while intento != secreto:
        if intento < secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        intento = int(input("Intenta de nuevo: "))
    print("¡Adivinaste!")


"""a) Nombres de compañeros
Declara una lista con 5 nombres y muestra el primero y el último.
b) Reemplazar elemento
Crea una lista de 5 números, reemplaza el tercero por 99 y muestra la lista.
Lista desordenada
c) Lista desordenada
Con la lista [7, 42, 15, 3, 28, 91, 54], muestra los primeros 3 elementos y los últimos 2.
d) Lista de frutas
Pide al usuario 3 frutas y muéstralas en una lista.
e) Lista anidada (matriz)
Declara una matriz 2x3 e imprime los elementos en [0][1], [1][0] y [1][2].
f) Números positivos y negativos
Crea una lista de 6 números (algunos positivos y otros negativos). Muestra por separado solo los positivos y solo los negativos.
Menú con Listas (Mini Proyecto — Tienda de ropa)
Consigna:
Una tienda de ropa necesita llevar el control de las prendas.
Crea dos listas:
•	prendas[] → nombres de las prendas.
•	stock[] → cantidad disponible.
Menú con las siguientes opciones:
1.	Ingresar prendas y stock.
2.	Ver inventario.
3.	Ver prendas agotadas.
4.	Salir.
"""
#punto a

nombres = ["Ana", "Luis", "Carlos", "María", "Pedro"]
print("Primer nombre:", nombres[0])
print("Último nombre:", nombres[-1])


# punto b
numeros = [10, 20, 30, 40, 50]
numeros[2] = 99
print(numeros)


# punto c

lista = [7, 42, 15, 3, 28, 91, 54]
print("Primeros 3:", lista[:3])
print("Últimos 2:", lista[-2:])


# punto d
frutas = []
for i in range(3):
    fruta = input(f"Ingrese la fruta {i+1}: ")
    frutas.append(fruta)
print("Lista de frutas:", frutas)


# punto e
matriz = [[1, 2, 3],[4, 5, 6]    ]
print("Elemento [0][1]:", matriz[0][1])
print("Elemento [1][0]:", matriz[1][0])
print("Elemento [1][2]:", matriz[1][2])


#punto f

numeros = [5, -3, 10, -7, 8, -2]
positivos = [n for n in numeros if n > 0]
negativos = [n for n in numeros if n < 0]
print("Positivos:", positivos)
print("Negativos:", negativos)


# punto

prendas = []
stock = []

while True:
    print("\n--- Menú Tienda de Ropa ---")
    print("1. Ingresar prendas y stock")
    print("2. Ver inventario")
    print("3. Ver prendas agotadas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        prenda = input("Ingrese el nombre de la prenda: ")
        cantidad = int(input("Ingrese la cantidad disponible: "))
        prendas.append(prenda)
        stock.append(cantidad)
        print("Prenda registrada.")
    elif opcion == "2":
        print("\n--- Inventario ---")
        for i in range(len(prendas)):
            print(f"{prendas[i]} - {stock[i]} unidades")
    elif opcion == "3":
        print("\n--- Prendas agotadas ---")
        for i in range(len(prendas)):
            if stock[i] == 0:
                print(prendas[i])
    elif opcion == "4":
        print("Saliendo de la tienda...")
        break
    else:
        print("Opción inválida.")


