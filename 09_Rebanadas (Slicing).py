#Rebanadas (Slicing)

"""
¿Cómo hacer rebanadas -cortar porciones- de tuplas, listas y cadenas de caracteres?

Python nos facilita una sintaxis sencilla para recuperar un trozo de una lista, tupla o de una cadena de caracteres.
Para recuperar una "porción" o un trozo de una lista debemos indicar en el subíndice dos valores separados por el caracter ":".
Del lado izquierdo indicamos a partir de qué elementos queremos recuperar y del lado derecho hasta cual posición sin incluir dicho valor.
Por ejemplo:

"""

lista1=[0,1,2,3,4,5,6]
lista2=lista1[2:5]

print(lista2) 
# 2,3,4

"""
Estamos recuperando de la posición 2 hasta la 5 sin incluirla. 
También es posible no indicar alguno de los dos valores:
"""

lista4=lista1[:3]
print(lista4) # 0,1,2

"""
Si no indicamos el primer valor estamos diciendo que queremos recuperar desde el principio de la lista hasta la posición menos uno indicada después de los dos puntos.
En cambio, si no indicamos el valor después de los dos puntos se recupera hasta el final de la lista:
"""

lista5=lista1[2:]
print(lista5) # 2,3,4,5,6
"""

Hay que tener en cuenta que el concepto de "porciones" se puede aplicar en forma indistinta a tuplas, listas y cadenas de caracteres.

Valores negativos

Ahora veremos que podemos utilizar un valor negativo para acceder a un elemento de la estructura de datos.
En Python podemos acceder fácilmente al último elemento de la secuencia indicando un subíndice -1:
"""

print(lista1[-1]) # 6

"""
Luego el anteúltimo se accede con la sintaxis:
"""

print(lista1[-2]) # 5
