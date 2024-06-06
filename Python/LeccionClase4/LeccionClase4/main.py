# CLASE 04
# OPERADORES PARTE 1

# OPERADORES ARITMETICOS

# SUMA
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("")
# print("Resultado de la suma:", suma)
print(f'El resultado de la suma es: {suma}')
# RESTA
resta = operandoA - operandoB
print("")
print(f'El resultado de la suma es: {resta}')
# MULTIPLICACION
multiplicacion = operandoA * operandoB
print("")
print(f'El resultado de la suma es: {multiplicacion}')
# DIVISION 1
division = operandoA / operandoB
print("")
print(f'El resultado de la suma es: {division}')
# DIVISION 2
division = operandoA // operandoB
print("")
print(f'El resultado de la suma es: {division}')
# MODULO
modulo = operandoA % operandoB
print("")
print(f'El resultado de la suma es: {modulo}')
# EXPONENTE
exponente = operandoA ** operandoB
print("")
print(f'El resultado de la suma es: {exponente}')

# EJERCICIO RECTANGULO
print("")
alto = int(input("Proporciona el alto del rectangulo: "))  # 5
print("")
ancho = int(input("Proporciona el ancho del rectangulo: "))  # 3
area = alto * ancho
perimetro = (alto + ancho) * 2
print("")
print(f"Area: {area}")
print("")
print(f"Perimetro: {perimetro}")

# OPERADORES DE ASIGNACION Y COMPARACION

miVariable3 = 10
print("")
print(miVariable3)

# Operadores de reasignacion
miVariable3 = miVariable3 + 1
print("")
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# Operadores de Comparacion
d = 4
b = 6

# Operador igual que
resultado = d == b  # Comprobamos si son iguales
print(resultado)

# Operador diferente que
resultado = d != b  # Comprobamos si son diferentes
print(resultado)

# Operador Mayor que
resultado = d > b
print(resultado)

# Operador Menor que
resultado = d < b
print(resultado)

# Operador Mayor o Igual que
resultado = d <= b
print(resultado)

# Operador Menor o Igual que
resultado = d >= b
print(resultado)

# Ejercicio Numero Par o Impar
a = int(input("Digite un número: "))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un número PAR")
    print("")
else:
    print(f"El valor a es: {a} es un número IMPAR")
    print("")

# Ejercicio Determinar si es mayor de edad

edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es: { edadPersona} años, usted es mayor de edad")
    print("")
else:
    print(f"Su edad es: {edadPersona} años, usted es menor de edad")
    print("")
