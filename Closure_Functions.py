print("""
#####################################################################
---------------------------------------------------------------------
##################################################################### 
""")
print(""""CLOSURE FUNCTIONS" ó "CLAUSURAS" es cuando una función interna hace referencia 
a variables locales de la función externa, y esto hace que haya una especie de memoria y 
retiene esas variables por cierto tiempo.   
""")

# CLOSURE
def exterior(x):
    def interior(y):
        return x + y
    return interior

# Creamos una clausura llamando a la función exterior.
clausura = exterior(10)

# Ahora cuando llamemos a la función clausura va a recordar el valor que le dimos.
resultado = clausura(5)
print(resultado)

print("""
#####################################################################
---------------------------------------------------------------------
#####################################################################
""")