print("""
      
#####################################################################
---------------------------------------------------------------------
##################################################################### 
         
          """)
print("""La recursión es la técnica de llamarse a una función a si misma dentro. Esto es similar a un Bucle Y nos puede quedar haciendo un bucle infinito
      
      
      """)

print("""Ejemplo 1""")
def suma_naturales(n):
    if n==1: 
        return 1
    else:
        return n + suma_naturales(n-1)
# Esta es una "FUNCION RECURSIVA"
print(suma_naturales(5))

print("""
Ejemplo 2""")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Esta es una "FUNCION RECURSIVA"
print(factorial(5))

print("""
Ejemplo 3""")
def contador(n):
    print(n) # Imprime 1 // imprime 9
    n += 1 # suma 1 quedando 2 // suma 1 quedando en 10 Y como "n" NO es menor a 10 se termina el bucel
    if n < 10: # Como 2 es menor a 10, entonces "contador(2)"; y asi se repite el bucle o la recursion
        contador(n)
# Esta es una "FUNCION RECURSIVA"
contador(1)

print("""
      

#####################################################################
---------------------------------------------------------------------
#####################################################################

""")