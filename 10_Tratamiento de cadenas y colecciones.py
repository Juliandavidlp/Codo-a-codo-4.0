#Tratamiento de cadenas y colecciones:


#Operaciones con cadenas, métodos y funciones

cadena='4 Hours Chopin for Studying, Concentration & Relaxation' # declaro una variable

print(len(cadena)) # Devuelve longitud de la cadena.

print(cadena.count('Chopin')) # Cuenta la cantidad de veces que aparece el parámetro que le pasamos.
print(cadena.find('Concentration')) # Devuelve la posición de búsqueda de la cadena que le pasamos como parámetro.

cadena1= cadena.join('**') # Inserta los argumentos que le pasamos como parámetro entre la cadena de caracteres.
#print(cadena1)
lista= cadena.split(' ') # Divide una cadena en unidades menores separando los elementos en una lista.
#print(lista)
tupla= cadena.partition(' ') # Divide una cadena en unidades menores separando los elementos una tupla.
#print(tupla)
cadena1 = cadena.replace('Chopin','Mozart',1) # Busca/sustituye términos.
#print(cadena1)

if cadena.startswith("Tango"): 
    # evalúa si comienza por “tango” (Falta definir el bloque)
    pass 
elif cadena.endswith("Relaxation"): # evalúa si termina por “Relaxation” (Falta definir el bloque)
    pass 
elif cadena.find("Tango") != -1: 
    # evalúa si "Tango" es distinto a menos uno. (Falta definir el bloque)
    pass

print(cadena.upper()) # convierte la cadena a mayúsculas.
print(cadena.lower()) # convierte la cadena a minúsculas.


#Tuplas, listas, diccionarios y conjuntos.


#Tuplas:
tupla = () # creo una tupla vacía
tupla = tuple([1, 2, 3, 4, 5]) # La función tuple() convierte una lista en una tupla.
tupla[0:3] # (1, 2, 3), accede a los valores a partir de la posición con el formato "desde:hasta".
           #Contar desde el último valor, un elemento menos.


#Listas:

nombres= ["Damián","Julián","mamá"]# declaro una lista.          
print(nombres)# o print(nombres[0])

# Si quiero cambiar un elemento de una lista puedo volver a definirlo modificando el índice correspondiente.
nombres[2]="Patricia"
print(nombres) 

#El método list.append() es para agregar un elemento en la lista.
nombres.append("Néstor")
print(nombres)

#La función len() cuenta la cantidad de elementos que tiene una lista, 
# nos devuelve el valor de la longitud de la lista.
print(len(nombres))

#El método list.insert(i,"") permite insertar un elemento en un índice determinado de una lista.
# El método list.extend() permite agregar un elemento en una lista.
# El método list.pop() elimina lo que le pasemos como parámetro, o el último elemento de la lista por defecto.
# Y además, si queremos retornar el elemento eliminado se lo asocia a una variable y se lo imprime.
nombres.pop(3)
print(nombres)


#Diccionarios:

# Los diccionarios se definen con la forma llave-valor, key:value.
países= {"América_latina": ["Argentina","Uruguay","Brasil"]}

# La función dict() declara un diccionario a partir de cadenas simples.
dict = dict(América_latina="Argentina", Europa="Francia") 

# El método list.update() permite agregar o modificar elementos en un diccionario.
print(países.update({"América_Latina": "Colombia"}))

# El método list.remove() permite eliminar un elemento a partir su llave o su nombre en un diccionario o una lista.
print(nombres.remove("Julián"))

# El método .items a partir de un diccionario devuelve listas en una tupla con la forma llave:valor.
print(dict.items())

#El método .keys devuelve una lista con las claves del diccionario que le pasamos como argumento.
print(dict.keys())  

#El método .values devuelve una lista con las claves de un diccionario.
print(dict.values())


#Operadores para secuencias: in, not in, is, is not

cadena = 'Python'
if 'y' in cadena: 
    print('La letra “y” está en “Python”')

lista = [1, 2, 3, 4, 5]
if 6 not in lista:
    print('El número 6 no está en la lista') 

if 'abcabc' is 'abc' * 2: 
    print('Son iguales')


#Operaciones con conjuntos

conjunto = set() # Define un conjunto vacío
lista = ['vino', 'jugo de naranja', 'agua', 'vino'] # define lista
bebidas = set(lista) # define conjunto a partir de una lista

print('jugo de naranja' in bebidas) # True, 'vino' está en el conjunto
print('anis' in bebidas) # False, 'anis' no está en el conjunto
print(bebidas) # imprime {'agua', 'cerveza', 'vino'}

# El método .copy() crea unconjunto a partir de la copia de otra colección que le pasamos como parámetro.
bebidas1 = bebidas.copy() 
print(bebidas1) # Imprime la misma.

# El método .add() añade un nuevo elemento.
bebidas1.add('yogurt') 

#El método .discard() borra el elemento que le pasamos como parámetro.
bebidas.discard('agua') 

# El operador & permite comparar elementos comunes.
print(bebidas & bebidas1) 


