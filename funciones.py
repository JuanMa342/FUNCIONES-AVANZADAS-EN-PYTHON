print("""
      
#####################################################################
---------------------------------------------------------------------
##################################################################### 
         
          """)
print("""Vamos a ver a continuacion ejemplos de Funciones en Python con sus respectivas Calls o llamadas a la Función
      
      
      """)

print("""Ejemplo 1""")
# Es un ejemplo de una Funcion normal en Python, junto con su llamada
def saludar():
    print("Hola Mundo")

saludar()

print("""
Ejemplo 2""")
# Es un ejemplo de una Funcion normal en Python, junto con su llamada
def saludar2(nombre):
    print("Hola", nombre)

saludar2("Sergio")

print("""
Ejemplo 3""")
# Es un ejemplo de una Funcion normal en Python, junto con su llamada
def saludar3(nombre,apellido):
    print("Hola", nombre)

saludar3("Sergie","Code")

print("""
Ejemplo 4""")
# Es un ejemplo de una Funcion normal en Python, junto con su llamada
def saludar4(nombre,apellido):
    print("Hola",nombre,apellido)

saludar4("Sergie","Code")

print("""
Ejemplo 5""")
# Es un ejemplo de una Funcion con un parametro predefinido en Python, junto con su llamada
def saludar5(nombre,apellido="Code"):
    print("Hola",nombre,apellido)

saludar5("Sergie")

print("""
Ejemplo 6""")
# Es un ejemplo de una Funcion con varios argumentos o varios valores reales en su llamada en Python, junto con su llamada
def Saludar(*nombres):
    print("Los valores Reales son los siguientes: ",nombres)
    print(type(nombres))
    print("Hola",nombres[0],nombres[1])

Saludar("Sergie","Code")

print("""
Ejemplo 7""")
# Es un ejemplo de una Funcion con varios argumentos o varios valores reales en su llamada en Python Y con estructuras logicas de "IF", junto con su llamada
def Saludar1(*nombres):
    print("Los valores Reales son los siguientes: ",nombres)
    print(type(nombres))
    if len(nombres)>1:
        print("Hola",nombres[0],nombres[1])
    else:
        print("Hola",nombres[0])

Saludar1("Sergie")
Saludar1("Sergie","Code")

print("""
Ejemplo 8""")
# Es un ejemplo de una Funcion con "Keywords Arguments" o con "Arbitrary Arguments" predefinido en Python, junto con su llamada
def padre_orgulloso(nene1,nene3,nene2):
    print("Mis hijos son: ",nene1,", ",nene2," y ",nene3)
    print("Y el mas pequeño es ",nene3)

padre_orgulloso(nene1="Ricardito",nene2="Nicolas",nene3="Juancito") # En esta llamada usamos los "Keywords Arguments"
padre_orgulloso("Ricardito","Nicolas","Juancito") # Aca NO uso los "Keywords Arguments" por lo que da distintos valores la funcion debido al desorden en sus parámetros de entrada

print("""
Ejemplo 9""")
# Es un ejemplo de una Funcion con "Keywords Arguments" o con "Arbitrary Arguments" predefinido en Python, junto con su llamada
def padre_orgulloso1(**nenes):
    print("Los valores Reales son los siguientes: ",nenes)
    print(type(nenes))
    print("Mis hijos son: ",nenes["a"],", ",nenes["b"]," y ",nenes["c"])
    print("Y el mas pequeño es ",nenes["c"])

padre_orgulloso1(a="Ricardito",b="Nicolas",c="Juancito")

print("""
      

#####################################################################
---------------------------------------------------------------------
#####################################################################

""")