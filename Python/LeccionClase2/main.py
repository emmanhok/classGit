# CLASE02
# VARIABLES PARTE 1
# LAS VARIABLES SON DE TIPO DINAMICAS NO ES NECESARIO DEFINIRLAS
# REUTILIZACION DE VARIABLE
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben (con los ultimo 3 numeros)
# Esos 3 numeros se van modificando cada vez que se ejecuta nuevamente el programa
# variable x = x512, variable y = x256, variable z = x576
print(id(y))
print(id(z))
