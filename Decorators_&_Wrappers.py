print("""
#####################################################################
---------------------------------------------------------------------
##################################################################### 
""")
print(""""DECORATORS" & "WRAPPERS" nos van a permitir tomar una función común 
y corriente, y agregarle más funciones ó funcionalidades. 
""")

# "DECORATORS" & "WRAPPERS"
def decorador(funcion):
    def envoltorio():
        print("Esta funcionalidad se dispararía antes de la función que nos pasen por argumento.")
        funcion()
        print("Esta funcionalidad se dispararía después de la función que nos pasen por argumento.")
    return envoltorio
def saludar():
    print("Hola, estoy saludando.")

saludo_decorado = decorador(saludar)
saludo_decorado()
print("""
Aca estoy ejecutando una función pero usando a otra función de pantalla ó envoltorio. 
""")
print("""El "DECORADOR" y el "WRAPPER" nos sirve para, por ejemplo, si estuviésemos haciendo 
algún tipo de acción con productos y nosotros antes de hacer cualquier acción tenemos que 
chequear si tiene saldo Y podríamos poner dentro de un "DECORADOR" y chequear si tiene saldo 
o no; Ó siempre antes de hacer una compra deberíamos mostrar cierta información; Ó siempre antes 
de que un producto se quede sin Stock deberíamos hacer una acción de ponerlo en color gris en la 
página.
""")
print("""Entonces tenemos la función final que es "saludar()" ó "vender()", y nosotros con el 
decorador le agregamos funcionalidad para que chequee antes de hacer la función nuestra el 
resto de las condiciones que son necesarias para que esa función termine de funcionar 
correctamente. 
""")
print("""
#####################################################################
---------------------------------------------------------------------
#####################################################################
""")