print("""
      
#####################################################################
---------------------------------------------------------------------
##################################################################### 
         
          """)
print("""Vamos a ver a continuacion ejemplos de Funciones en Python con sus respectivas Calls o llamadas a la Función
      
      
      """)

print("""Ejemplo 1""")
# Es un ejemplo de una Funcion normal en Python, junto con su llamada
def mostrar_mercaderia(mercaderia):
    for item in mercaderia:
        print(item)

lista_frutas=["Manzana","Pera","Platano"]
mostrar_mercaderia(lista_frutas)

print("""Ejemplo 2""")
# Es un ejemplo de una Funcion normal en Python usando el comando "RETURN", junto con su llamada
def suma(a,b):
    return a+b

print(suma(2,3))

print("""Ejemplo 3""")
# Es un ejemplo de una Funcion normal en Python usando el comendo "RETURN", junto con su llamada
def suma2(a,b):
    resultado = a+b
    return resultado

print(suma2(2,3))

print("""Ejemplo 4""")
# Es un ejemplo de una Funcion normal en Python usando el comendo "RETURN", junto con su llamada
def suma3(a,b):
    resultado = a+b # Variable Local (solo va a estar disponible dentro de la función)
    return resultado

resultado = suma3(2,3) # Variable Global (está disponible de forma Global)
print(resultado)

print("""Ejemplo 5""")
# Es un ejemplo de una Funcion normal en Python usando el comando "PASS", junto con su llamada
def suma4(a,b):
    pass

resultado2 = suma4(2,3)
print(resultado2)

print("""Ejemplo 6""")
# Es un ejemplo de una Funcion normal en Python usando el comendo "RETURN", junto con su llamada. Además estoy describiendo brevemente lo que hace la funcionentre comillas triples.
def suma5(a,b):
    """Esta Función sumará los 2 argumentos que se pasen"""
    return a+b

resultado3 = suma(2,3)
print(resultado3)

print("""Ejemplo 7""")
# Es un ejemplo de una Funcion normal en Python usando el comendo "RETURN", junto con su llamada
def devolver_cuadrado(x):
    return x**2

print(devolver_cuadrado(2))
print(devolver_cuadrado(x=2))

print("""Ejemplo 8""")
# Es un ejemplo de una Funcion normal en Python usando el comendo "RETURN", junto con su llamada y un "DOCSTRING" explicando que hace la funcion.
def devolver_cuadrado2(x,/):
    """Devuelve el cuadrado del valor pasado por argumento"""
    # Al poner "(x,/)" estoy anulando la posibilidad de usar los "Keywords Arguments" al llamar a la funcion.
    return x**2

print(devolver_cuadrado(2))

print("""Ejemplo 9""")
# Es un ejemplo de una Funcion normal en Python usando el comendo "RETURN", junto con su llamada y un "DOCSTRING" explicando que hace la funcion.
def devolver_cuadrado3(*,x):
    """Devuelve el cuadrado del valor pasado por argumento"""
    # Al poner "(*,x)" estoy anulando la posibilidad de usar los "Positional Arguments" al llamar a la funcion.
    return x**2

print(devolver_cuadrado3(x=2))

print("""       
El "(x,/)" me obliga a llamar a la función usando el "Positional Argument".
El "(*,x)" me obliga a llamar a la funcion usando el "Keyword Argument".
      
      """)

print("""Ejemplo 10""")
# Es un ejemplo de una Funcion normal en Python usando el comendo "RETURN", junto con su llamada.
def calcular_resultado(a,b,/,*,c,d):
# Al poner el argumento "(a,b,/,*,c,d)" las variables "a" y "b" solo permiten ser llamadas mediante "Positional Arguments".
# Al poner el argumento "(a,b,/,*,c,d)" las variables "c" y "d" solo permiten ser llamadas mediante "Keywords Arguments".   
    print(a+b+c+d)

calcular_resultado(1,2,c=3,d=4)

print("""Ejemplo 11""")
# Es un ejemplo de una Funcion normal en Python usando el comendo "RETURN", junto con su llamada.
def operaciones(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b # Este conmando de division "/" me devuelve un dato de tipo "Flotante" o "Float"
    return [suma,resta,multiplicacion,division]

print(operaciones(4,2))
print(type(operaciones(4,2)))

print("""
El comando "RETURN" en una Función hace que al ser llamada la Función,
la Función me devuelva todo lo que esta seguido o a continuacion de la palabra "RETURN",

      """)

print("""Ejemplo 12""")
# Es un ejemplo de una Funcion normal en Python usando el comendo "RETURN", junto con su llamada.
def operaciones2(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    return (suma,resta,multiplicacion,division)

print(operaciones2(4,2))
print(type(operaciones2(4,2)))

print("""Ejemplo 13""")
# Es un ejemplo de una Funcion normal en Python usando el comendo "RETURN", junto con su llamada.
def operaciones3(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    return {suma,resta,multiplicacion,division}

print(operaciones3(4,2))
print(type(operaciones3(4,2)))

print("""
      

#####################################################################
---------------------------------------------------------------------
#####################################################################

""")