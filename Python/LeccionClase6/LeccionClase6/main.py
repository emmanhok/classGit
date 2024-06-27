# CLASE 6

# En esta clase veremos la sentencia if/else
"""
print("")
condicion = False
if condicion:
    print("Condicion Verdadera")
else:
    print("Condicion Falsa")

# Evaluar si una variable está vacia o tiene un dato dentro?

print("")
condicion = 10
if condicion:
    print("Condicion Verdadera")
else:
    print("Condicion Falsa")

print("")
condicion = ""
if condicion:
    print("Condicion Verdadera")
else:
    print("Condicion Falsa")

# A continuacion se evalua si hay una condicion booleana para
# imprimir Verdadero o Falso
# Como la variable contiene una cadena
# Ira al else ya que no es una expresion booleana

print("")
condicion = "Hola alumnos"
if condicion == True:
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion Sin Especificar")

print("")
condicion = True
if condicion == True:
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion Sin Especificar")

print("")
condicion = False
if condicion == True:
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion Sin Especificar")
"""

# Ejecución Debug en if/else
# Punto de ruptura en linea 65
# Ejecutamos en debug quiere decir depurar
"""
print("")
condicion = 10
if condicion == True:
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion Sin Especificar")
"""
# Ejercicio: Conversión de número a texto
# Atajo para comentar un conjunto de líneas: ctrl + diagonal

# num = int(input("Digite un numero en el rango del 1 al 3: "))
# numTexto = ""
# if num == 1:
#     numTexto = "Numero uno"
# elif num == 2:
#     numTexto = "Numero dos"
# elif num == 3:
#     numTexto = "Numero tres"
# else:
#     numTexto = "Has ingresado un numero fuera del rango"
# print(f"El numero ingresado es: {num} - {numTexto}")

# Sintaxis simplificada (Operador Ternario)
# Se recomienda esta sintaxis simplificada solo si el codigo es pequeño
# Si se utiliza elif por ejemplo no se recomienda su uso

condicion = True
# if condicion:
#     print("Condicion Verdadera")
# else:
#     print("Condicion Falsa")
print("Condicion Verdadera ") if condicion else print("Condicion Falsa")
