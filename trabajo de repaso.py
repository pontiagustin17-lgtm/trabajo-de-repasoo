"""trabajo de repaso"""

"""a) Nombre, edad y preguntas del día
Escribe un programa que pida al usuario su nombre y edad, muestre un mensaje de bienvenida y le pregunte dos cosas de su día (por ejemplo: si comió y si estudió). Finalmente, muestra un resumen.
b) Mantel para mesa
Escribe un programa que calcule cuánto mantel se necesita para cubrir una mesa rectangular. El usuario ingresa largo y ancho (en metros).
c) Conversor de minutos a horas
Pide al usuario un número de minutos y muestra cuántas horas y minutos equivalen.
"""
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
"""
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
velocidad= int(imput("intrudusca su velocidad en km/h"))
if velocidad < 40:
    print("Vas lento")
elif velocidad > 120:
    print("Vas rápido")
else:
    print("Vas a una velocidad normal")
    #punto  
