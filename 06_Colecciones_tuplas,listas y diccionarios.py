# Una colección es una variable que puede almacenar muchas variables simples. Las colecciones son objetos.
# Las listas son arreglos, conjuntos de elementos simples y contiguos en la memoria a los que se puede acceder 
# desde la posición cero. Con este tipo de objetos podemos guardar mucha información.



nombres= ["Damián","Julián","mamá"]
print(nombres)                                    

# o print(nombres[0])


"""


# Si quiero cambiar un elemento de una lista puedo volver a definirlo modificando el índice correspondiente.

nombres[1]="Néstor"
print(nombres) 





# Tuplas, listas y diccionarios:

#Son tipos de colecciones diferentes que tienen algunas diferencias. Las tuplas no se pueden modificar y
#los diccionarios se construyen a partir de la forma [key]:"value", llave/valor.

países = (´Argentina´,´Uruguay´, ´Brasil´)
países= [´Argentina´, ´Uruguay´, ´Brasil´]
países= {"América_latina": [´Argentina´,´Uruguay´,´Brasil´]}





# La programación se establece bajo el concepto de que todo existe a partir de objetos con características (propiedades)
# y funciones (o métodos), que se comunican entre sí todo el tiempo. Entonces tenemos métodos y funciones asociadas a objetos, 
# por ejemplo, distintos métodos y funciones orientados a un arreglo.



#El método list.append() es para agregar un elemento en la lista.
nombres.append("Néstor")
print(nombres)


#La función len() cuenta la cantidad de elementos que tiene una lista, 
# nos devuelve el valor de la longitud de la lista.

print(len(nombres))


#El método list.insert(i,"") permite insertar un elemento en un índice determinado de una lista.

nombres.insert(3,"Néstor")
print(nombres)


# El método list.extend() permite agregar varios elementos en una lista.

nombres.extend("Argentina", "Uruguay","Brasil")
print(nombres)


# El método list.update() permite agregar o modificar varios elementos al mismo tiempo en un diccionario.

países.update([América Latina]: "Chile", "Colombia")
print(países)


# El método list.remove() permite eliminar un elemento a partir su nombre en un diccionario o una lista.

nombres.remove("Julián")
print(nombres)


"""

# El método list.pop() elimina lo que le pasemos como parámetro, o el último elemento de la lista por defecto.

nombres.pop()
print(nombres)

# Y además, si queremos retornar el elemento eliminado se hace lo siguiente:

elementoremovido=nombres.pop()
print(elementoremovido)


"""















"""

