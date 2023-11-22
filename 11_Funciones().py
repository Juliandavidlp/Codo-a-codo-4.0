# Funciones:

# Una función es una variable que desarrolla un código interno que puede devolver 
# un valor o realizar alguna acción. Los problemas se pueden dividir en funciones.
"""
def saludar():
    print("Buen día mundo")

# Así, se encapsulan procesos en funciones de manera simplificada. 
# Invocamos la función cuando la llamamos:

saludar()


# Las funciones pueden tener parámetros y argumentos:

def saludar1(nombre):
    print("Hola", nombre)

saludar1("Damián")


# La instrucción return retorna un valor de manera especificada:

def saludar2(nombre):
    return("Hola", nombre)


# Además, los argumentos pueden ser posicionales o nombrados, 
# si hay más de un parámetro primero se colocan los posicionales, luego los nombrados.
"""


def sumar100(num1,num2=100):
    return (num1+num2)


print(sumar100(100))

