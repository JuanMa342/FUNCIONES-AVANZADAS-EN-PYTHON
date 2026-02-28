print("""
#####################################################################
---------------------------------------------------------------------
##################################################################### 
         
          """)
print("""La Documentación de Funciones es el "DOCSTRING". Las "DOCSTRINGS" son cadenas de documentación colocadas
en la parte superior de una función para describir su propósito, parámetro, comportamiento y cualquier otra 
informacion reelevante.
      
      
      """)

print("""Ejemplo 1""")
def suma(a,b):
    """
    Esta Función suma dos números y devuelve el resultado

    Args:
        a (int): El primer número a sumar.
        b (int): El segundo número a sumar.
    Return:
        int: La suma de los dos números.
    """
    return a + b
# Esta es una "FUNCIÓN DOCUMENTADA CON DOCSTRINGS"
print(suma(2,3))

print("""
Ahora vamos a usar el comando "help(suma)" Y el comando "suma.__doc__" de forma tal de ver unicamente el DOSCTRING de la función.
""")
help(suma)
print(suma.__doc__)

print("""
Ejemplo 2""")
def resta(c,d):
    """
    Esta Función resta dos números y devuelve el resultado

    Args:
        a (int): El primer número a restar.
        b (int): El segundo número a restar.
    Return:
        int: La resta de los dos números.
    """
    return c - d
# Esta es una "FUNCIÓN DOCUMENTADA CON DOCSTRINGS"
print(resta(2,3))

print("""
Ahora vamos a usar el comando "help(resta)" Y el comando "resta.__doc__" de forma tal de ver unicamente el DOSCTRING de la función.
""")
help(resta)
print(resta.__doc__)

print("""
#####################################################################
---------------------------------------------------------------------
#####################################################################

""")