#Funciones Lambda (o anónimas)

"""
En Python, las funciones lambda son también conocidas como funciones anónimas porque se definen sin un nombre.
Como sabemos, una función en Python se define con la palabra reservada def. Sin embargo, una función anónima se define con la palabra reservada lambda.

La sintaxis para definir una función lambda es la siguiente:

lambda parámetros: expresión

#¿Cuáles son sus características?

Son funciones que pueden definir cualquier número de parámetros pero una única expresión. Esta expresión es evaluada y devuelta.
Se pueden usar cuando una función así sea requerida.

Estas funciones están restringidas a una expresión. Y se pueden combinar con otras funciones, generalmente como argumentos de funciones comunes.
Por ej.:
"""
cuadrado = lambda x: x ** 2

"""
Como ves, la función no tiene nombre y toda la definición devuelve una función que se
le asigna al identificador cuadrado.

En el siguiente ejemplo se aprecian las similitudes y diferencias de usar una función
anónima y una función normal:
"""

def cuadrado(x):
    return x * 2

cuad=lambda x: x * 2

print(cuadrado(10))
print(cuad(5)) 

#Llamar la función anónima a partir del identificador, 
# como una función común, digamos.


"""
Un ejemplo de uso


La función map() en Python aplica una función a cada uno de los elementos de una lista.
map(una_funcion, una_lista)

Imagina que tienes una lista de enteros y quieres obtener una nueva lista con el
cuadrado de cada uno de ellos.

Seguramente, lo primero que se te ha ocurrido es algo similar a lo siguiente:

enteros = [1, 2, 4, 7]
cuadrados = []
for e in enteros:
 cuadrados.append(e ** 2)

print(cuadrados)
[1, 4, 16, 49]

Sin embargo, podemos usar una función anónima en combinación con map() para
obtener el mismo resultado de una manera mucho más simple:

"""

enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))

print(cuadrados)

