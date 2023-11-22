#Definir una función:

def hello_world():
    print('Hola mundo con funciones')


def sumar(a,b):
    resultado= a + b
    return resultado
    # return a+b

# hello_world()
# r = sumar(30)
# numero_1 = int(input('Ingrese un valor 1: '))
# numero_2 = int(input('Ingrese un valor 2: '))

# print(f'La suma es {sumar(numero_1,numero_2)}')

#Parámetros por defecto:
def saludar(nombre="Pepe",saludo="Hola"):    
    print(f'{saludo}, {nombre}')

# saludar('Pedro','Buen día')
# saludar('Damián')
# saludar()

#Indicando los argumentos de forma explicita:
# saludar(saludo="Buenas tardes",nombre="Nicolás")


"""
###Tipos de parámetros en una función de Python

A la hora de definir una función, podemos indicar una serie de parámetros.
Sin embargo, si al llamar a la función no le pasamos todos sus argumentos,
el intérprete nos lanzará una excepción donde nos va a indicar que falta
un argumento posicional obligatorio y no se ha especificado.

#Parámetros opcionales en una función

Consideremos a continuación la siguiente función:

def saludo(nombre, mensaje="cómo andás?"):
	print("Hola {}, {}".format(nombre, mensaje))
     
El parámetro "nombre" no indica un valor por defecto, por lo tanto, es posicional u obligatorio. No ocurre lo mismo con el parámetro "mensaje", cuyo valor por defecto es "cómo andás?". 
En caso de no pasar este argumento, se tomará dicho valor por defecto. Por el contrario, si se indica, se sobreescribirá con un nuevo valor pisado.

En una función se pueden especificar tantos parámetros opcionales como se quiera. Pero una vez que se indica uno, los demás parámetros a la derecha deben ser opcionales. 
Entonces, primero se colocan los parámetros posicionales u obligatorios, después los parámetros opcionales.


#Parámetros posicionales y parámetros con nombre en una función:

Cuando invocamos una función en Python con diferentes argumentos, los valores se asignan a los parámetros en el orden que le indicamos.
Sin embargo, el orden se puede cambiar si llamamos a la función a partir del nombre de los parámetros. Para que lo veas más claro, los siguientes ejemplos son todos válidos.

saludo(mensaje="¿cómo estás?", nombre="Damián")
#Hola Damián, ¿cómo estás?

>>>saludo(nombre="Julián", mensaje="¿cómo estás?")
#Hola Julián, ¿cómo estás?

###Conclusión

Por defecto, al llamar a una función los valores de los argumentos se asignan en el
mismo orden en el que se pasan al invocar a dicha función.

Los parámetros opcionales se indican con el operador ‘=’, tienen un valor por defecto y siempre se definen después de los parámetros obligatorios.
Se puede modificar el orden de los argumentos con el que se invoca a una función si se indica el nombre de los parámetros. Los parámetros con nombre siempre aparecen después de los posicionales.
"""


