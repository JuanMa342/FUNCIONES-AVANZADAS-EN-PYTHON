print("""
#####################################################################
---------------------------------------------------------------------
##################################################################### 
          """)
print("""Las "FUNCIONES LAMBDAS" son una función anónima y concisa definida con la palabra clave "LAMBDA"
utilizada para tareas simples y temporales.      
      """)

print("""Ejemplo 1 - FUNCIÓN NORMAL EN PYTHON""")
def duplicar(num):
    return num * 2
# Esta es una "FUNCIÓN NORMAL"
print(duplicar(5))

print("""
Ejemplo 2 - FUNCIÓN LAMBDA EN PYTHON""")
duplicar_lambda = lambda num : num * 2
# Esta es una "FUNCIÓN LAMBDA"
print(duplicar_lambda(5))

print("""
Ejemplo 3 - FUNCIÓN NORMAL EN PYTHON""")
def multiplicar(a,b):
    return a * b
# Esta es una "FUNCIÓN NORMAL"
print(multiplicar(4,5))

print("""
Ejemplo 4 - FUNCIÓN LAMBDA EN PYTHON""")
multiplicacion_lambda = lambda a,b : a * b
# Esta es una "FUNCIÓN LAMBDA"
print(multiplicacion_lambda(5,4))

print("""
Ejemplo 5 - FUNCIÓN NORMAL EN PYTHON""")
def cuadrado(num):
    return num * num
# Esta es una "FUNCIÓN NORMAL"
print(cuadrado(3))

print("""
Ejemplo 6 - FUNCIÓN LAMBDA EN PYTHON""")
cuadrado_lambda = lambda num : num * num
# Esta es una "FUNCIÓN LAMBDA"
print(cuadrado_lambda(3))

print("""
Ejemplo 7 - FUNCIONES MULTIPLES USANDO LAMBDA EN PYTHON""")
def multiplicador(n):
    return lambda x : x * n
# Esta es una "FUNCION MÚLTIPLE USANDO LAMBDA"
triplicar = multiplicador(3)
print(triplicar(5))
duplicar2 = multiplicador(2)
print(duplicar2(5))

print("""
Ejemplo 8 - UN ARMADOR DE FUNCIONES MULTIPLES EN PYTHON
Esta función es un armador de otras funciones; y para esto es que se usa la función "LAMBDA"
Esta función "LAMBDA" es un creador de otras funciones""")
def operaciones(operacion):
    if operacion == "suma":
        return lambda x,y : x + y
    elif operacion == "resta":
        return lambda x,y : x - y
    elif operacion == "multiplicacion":
        return lambda x,y : x * y
    else:
        return lambda x,y : x / y
# Esta es una "ARMADOR DE FUNCIONES MÚLTIPLES USANDO LAMBDA"
suma = operaciones("suma")
print(suma(2,5))
resta = operaciones("resta")
print(resta(2,5))
multiplicacion = operaciones("multiplicacion")
print(multiplicacion(2,5))
division = operaciones("division")
print(division(10,5))

print("""
Ejemplo 9 - FUNCIÓN LAMBDA EN PYTHON PARA ORDENAR LOS DICCIONARIOS (CONJUNTOS CLAVE-VALOR) DENTRO DE LA LISTA""")
estudiantes = [
    {"nombre":"Juan" , "edad":20},
    {"nombre":"Maria" , "edad":25},
    {"nombre":"Pedro" , "edad":22}
]
estudiantes_ordenados = sorted(estudiantes , key = lambda x : x['edad'])
print(estudiantes_ordenados)

print("""
#####################################################################
---------------------------------------------------------------------
#####################################################################

""")