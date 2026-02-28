print("""
#####################################################################
---------------------------------------------------------------------
##################################################################### 
""")
print("""Estas Funciones pasadas como argumento se llaman "CALLBACKS". Cuando me digan que 
hay que pasar una "CALLBACK" es que hay que pasar una funcion con argumento que dentro de 
la otra funcion resuelva algo puntual.      
""")

print("""Ejemplo 1""")
def aplicar_funcion(func,valor):
    return func(valor)

def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

print(aplicar_funcion(cuadrado,3)) # Salida: 9
print(aplicar_funcion(cubo,3)) # Salida: 27

print("""
#####################################################################
---------------------------------------------------------------------
#####################################################################

""")