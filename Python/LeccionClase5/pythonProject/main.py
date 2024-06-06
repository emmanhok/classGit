# Clase 5

# OPERADORES LOGICOS

# Operador AND (OPERADOR BINARIO)
a = False
b = False
resultado = a and b
print(resultado)

# Operador OR (OPERADOR BINARIO)
resultado = a or b
print(resultado)

# Operador NOT (OPERADOR UNARIO)
resultado = not a
print(resultado)


# Ejercicio: Valor dentro de un rango
'''
valor = int(input("Digite un numero dentro del rango 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} no esta dentro del rango")
'''
"""
# Ejercicio Operador OR
vacaciones = True
diaDescanso = True
if vacaciones or diaDescanso:
    print("Puede asistir al juego")
else:
    print("Tiene trabajo que hacer")

# Ejercicio Operador NOT
if not (vacaciones or diaDescanso):  # Logica inversa
    print("Tiene trabajo que hacer")
else:
    print("Puede asistir al juego")
"""
# Ejercicio: Rango entre 20 y 30 años

# edad = int(input("Digite su edad: "))
# veinte = edad >= 20 and edad < 30
# print(veinte)
# treinta = edad >= 30 and edad < 40
# print(treinta)

"""
if veinte or treinta:
    print('Estas dentro del rango de los (20\'0) a (30\'0) años')
    # Se usa la diagonal inversa para que no time comilla como cierre
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")
    # Se puede combiar " y ' para que no tome como cierre
"""
"""
if veinte:
    print('Estas dentro del rango de los (20\'0)')
elif treinta:
    print('Estas dentro del rango de los (30\'0) años')
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")
"""
# Aqui vemos que en python no se usan llaves como en otros lenguajes
# Se usan solamente tabulaciones
# if veinte or treinta
"""
if veinte or treinta:  # Aqui un ej de if anidado
    if veinte:
        print('Estas dentro del rango de los (20\'0)')
    elif treinta:
        print('Estas dentro del rango de los (30\'0) años')
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")
"""
"""
if (edad <= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print('Estas dentro del rango de los (20\'0) a (30\'0) años')
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")
"""
"""
# Sintaxis simplificada del operador And
if (20 <= edad < 30) or (30 <= edad < 40):
    print('Estas dentro del rango de los (20\'0) a (30\'0) años')
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")
"""

# Ejercicio: Mayor de dos numeros
# Practica del RUN DEBUG
"""
numero1 = int(input("Digite el valor para el numero 1: "))  # Aqui colocamos el punto de ruptura
numero2 = int(input("Digite el valor para el numero 2: "))

if numero1 > numero2:
    print("El numero 1 es mayor")
else:
    print("El numero 2 es mayor")
"""
# Ejercicio: Tienda de libros
print("Digite los siguientes datos del libro")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el envio del libro es gratuito (True/Galse): ")  # No se especifica booleano para que
# no se genere algun error
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorecto, debe escribir True/False"
# Se usa la f de format que con las comillas simples luego agregamos tabulaciones para darle la apariencia deseada al
# String
print(f'''
        Nombre: {nombre}
        ID: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}
''')
