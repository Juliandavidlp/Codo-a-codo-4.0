
#Conjuntos
"""
El tipo set en Python es la clase utilizada por el lenguaje para representar conjuntos. Un conjunto es una colección desordenada de elementos únicos que no se repiten. 
Cuando trabajamos con conjuntos de elementos la principal característica de este tipo de datos es que son una colección cuyos elementos no guardan ningún orden y no se repiten.

Los conjuntos por lo general se usan para conocer si un elemento pertenece o no a una colección y eliminar duplicados de otros tipos de elementos (list, tuple o str).
Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {}, o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable 
(como una lista, una tupla, una cadena, etc.).

Por ejemplo:
"""

conjunto= {"Damián", "Julián", "Mamá", "Mamá"}
# Los elementos repetidos se eliminan
print(conjunto)

#IMPORTANTE: {} NO crea un conjunto vacío, sino un diccionario vacío. 
"""Para crear un conjunto vacío, simplemente llama al constructor set() sin parámetros. Usar set() si queremos crear un conjunto sin elementos.
"""

"""
¿Cómo acceder a los elementos de un conjunto en Python?

Dado que los conjuntos son colecciones desordenadas, en ellos no se guarda la posición en la que son insertados los elementos como ocurre en los tipos list o tuple.
Es por ello que no se puede acceder a los elementos a través de un índice. Sin embargo, sí se puede acceder y/o recorrer todos los elementos de un conjunto usando un bucle for.

¿Cómo añadirle elementos a un conjunto (set)?

Para añadir un elemento a un conjunto se utiliza el método add(). También existe el método update(), que puede tomar como argumento una lista, tupla, string, conjunto 
o cualquier objeto de tipo iterable. Recordar que los elementos no pueden estar duplicados.

¿Cómo eliminar un elemento de un conjunto?

La clase set ofrece cuatro métodos para eliminar elementos de un conjunto. Son: discard(), remove(), pop() y clear(). 
El método discard(elemento) y remove(elemento) eliminan un elemento, la única diferencia es que si elemento no existe, discard() no hace nada mientras que remove() lanza la excepción KeyError.
El método pop() devuelve un elemento aleatorio del conjunto y lo elimina. Si el conjunto está vacío, lanza la excepción KeyError.
Y, por último, clear() elimina todos los elementos del conjunto.

                                                                                                                    
¿Cómo unir conjuntos en Python?
Se utiliza el operador | para realizar la unión de dos o más conjuntos.
"""

a = {1, 2, 3, 4}
b = {5, 6, 7, 8}

print(a | b) #{1, 2, 3, 4, 6, 8}

"""
¿Cómo cotejar la igualdad de dos conjuntos?

En Python dos conjuntos son iguales si y solo si todos los elementos de un conjunto están contenidos en el otro, por lo que que cada uno es un subconjunto del otro. 
Por ej.:
"""

a = {1, 2}
b = {1, 2}

id(a) 
id(b) 

a == b #True