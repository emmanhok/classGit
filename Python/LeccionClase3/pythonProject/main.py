# CLASE 3

# TIPOS DE DATOS

# LOS TIPOS DE DATOS SON CLASES POR ESO SI IMPRIMIMOS TYPE NOS FIGURA CLASS STR, CLASS INT, ETC.

a = "Hola alumnos"
print(type(a))
a: str = "Se usa str para mostrar la referencia"
print(type(a))

a = 10
print(type(a))

a = 10.78
print(type(a))

a = True
print(type(a))

a = False
print(type(a))

# TIPOS: int, float, String, Bool
x = 10
print(x)
print(type(x))

x = 14.5
print(x)
print(type(x))

x = "Hola Alumnos"
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = False
print(x)
print(type(x))

# MANEJO DE CADENAS (String)

miGrupoFavorito = "Red Hot Chili Peppers"
print("")
print(miGrupoFavorito)

# Concatenacion de cadenas
print("")
print("Mi grupo favorito es: "+miGrupoFavorito)

miGrupoFavorito = "Red Hot Chili Peppers" + " The Best Rock Band"
print("")
print(miGrupoFavorito)

miGrupoFavorito = "Red Hot Chili Peppers: " "The Best Rock Band"
print("")
print(miGrupoFavorito)

miGrupoFavorito = "Red Hot Chili Peppers:"
caracteristicas = "The Best Rock band"
print("")
print("Mi grupo favorito es: "+miGrupoFavorito+" "+caracteristicas)

miGrupoFavorito = "Red Hot Chili Peppers:"
caracteristicas = "The Best Rock band"
print("")
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print("")
print(numero1 + numero2)

numero1 = "7"
numero2 = "8"
print("")
print(int(numero1) + int(numero2))

# Tipos Booleanos (Bool) Nunca se va a ejecutar True y False al mismo tiempo, es una o la otra.

miBooleano = True
print("")
print(miBooleano)

miBooleano = False
print("")
print(miBooleano)

miBooleano = 1 > 2
print("")
print(miBooleano)

miBooleano = 3 > 2
print("")
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

miBooleano = 1 > 2
print("")
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario (FUNCION INPUT)

nombre = input("Escriba su nombre: ")
print("")
print(nombre)

resultado = input("Digite un numero: ") # REGRESA UN DATO TIPO STRING
print("")
print(resultado)

# Conversion de la entrada de datos (FUNCION INPUT)

print("")
numero1 = int(input("Escribe el primer numero: ")) # 78
print("")
numero2 = int(input("Escribe el segundo numero: ")) # 22
resultado = numero1 + numero2
print("")
print("El resutlado de la suma es: ", resultado)

# ACTIVIDAD
# EJERCICIO 1: CALIFICA TU DIA

print("")
dia = int(input("¿Cómo estuvo tu día del 1 al 10?"))
print("")
print("Mi día estuvo de", dia)

# EJERCICIO 2: LIBRO

print("")
titulo = input("Escribe el nombre del libro: ")
print("")
autor = input("Escribe el nombre del autor: ")
print("")
print(titulo, "fue escrito por", autor)