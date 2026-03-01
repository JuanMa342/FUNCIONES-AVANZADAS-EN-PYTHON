print("""
#####################################################################
---------------------------------------------------------------------
##################################################################### 
""")
print("""En esta sección vamos a ver "Funciones de Orden Superior", y vamos a ver específicamente
"MAPS", "REDUCE" y "FILTER" que son propias de Python.
Las "FUNCIONES DE ORDEN SUPERIOR" son auqellas que reciben y devuelven funciones cómo argumentos.     
""")

#  Función "MAP"
print("""La función "MAP" toma una función y un iterable cómo argumentos, y aplica la función a
cada elemento del iterable.
""")
def cuadrado(x):
    return x * x

numeros = [1 , 2 , 3 , 4 , 5]
cuadrados = list(map(cuadrado,numeros))
print(cuadrados)

#  Función "FILTER"
print("""
La función "FILTER" toma una función que devuelve "TRUE" o "FALSE" y un iterable, y
devuelve solo los elementos que devuelvan "TRUE" cómo argumento de la función.
""")
def es_par(x):
    return x % 2 == 0

pares = list(filter(es_par , numeros))
print(pares)

#  Función "REDUCE"
print("""
La función "REDUCE" toma una función que recibe dos argumentos y un iterable, y 
aplica la función de forma acumulativa a los elementos del iterable, Y además va de izquierda a 
derecha y los termina reduciendo a un solo valor.
""")
from functools import reduce
def suma(x,y):
    return x + y

sumatoria = reduce(suma,numeros)
print(sumatoria)

# Funcion "LAMBDA"
print("""
Usamos la función "LAMBDA" para reducir las líneas de código en las funciones a armar. 
""")
numeros = [1 , 2 , 3 , 4 , 5]
cuadrados1=list(map(lambda x: x * x , numeros))
print(cuadrados)
pares = list(filter(lambda x: x % 2 == 0 , numeros))
print(pares)

print("""
#####################################################################
---------------------------------------------------------------------
#####################################################################
""")