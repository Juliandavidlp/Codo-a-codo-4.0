"""Los parámetros *Args y **kwargs:

En los lenguajes de programación de alto nivel, Python entre ellos, al declarar una función podemos definir una serie de parámetros con los que invocar a dicha función.
Por regla general, el número y el nombre de estos parámetros son inmutables. Sin embargo, hay situaciones en las que es mucho más apropiado que el número de parámetros sea opcional y/o variable.

### ¿Qué significan los parámetros indefinidos en Python?

En Python, el parámetro especial *args en una función se usa para pasar, de forma opcional, un número variable de argumentos posicionales.
Lo que realmente indica que el parámetro es de este tipo es el símbolo ‘*’, el nombre args se usa por convención.
El parámetro recibe los argumentos como una tupla. Es un parámetro opcional. Se puede invocar a la función haciendo uso del mismo, o no.
Entonces el número de argumentos al invocar la función es variable.
"""

def sumar_dos(a,b,*args): #*args guarda o devuelve una tupla con todas las variables que le pasemos como parámetro.
    total= a + b

    for numero in args:        
        total += numero #"total" es igual a "total" más "numero"...    
    return total

resultado1= sumar_dos(1,4,10,3)
resultado2= sumar_dos(1,4,77)
print(f'El resultado: {resultado1}')
print(f'El resultado: {resultado2}')

"""
Otra opción es reimplementar nuestra función de la siguiente manera:
"""

def sum(*args):
    valor= 0

    for i in args:
        valor += i    
          
    return valor

"""
Con esta nueva implementación, podemos llamar a la función con cualquier número variable de valores, por ejemplo:
sum()

sum(2, 3)
sum(2, 3, 4)
sum(2, 3, 9, 90)


Veamos ahora el uso de **kwargs como parámetro. En Python, el parámetro especial **kwargs en una función se usa para pasar, de manera opcional,
un número variable de argumentos con nombre. Las principales diferencias con respecto *args son:

Lo que realmente indica que el parámetro es de este tipo es el símbolo **, el nombre kwargs se usa por convención.
El parámetro recibe argumentos como un diccionario, por lo que, al tratarse de un diccionario, el orden de los parámetros no importa.
Los parámetros se asocian en función de las claves del diccionario.
"""

#**kwargs sirve para guardar en un diccionario en forma de llave-valor los elementos que le pasemos como parámetro.

def saludar_dos(nombre,saludo, **kwargs):
    """
    print(f'{saludo}, {nombre}')
    print(kwargs)
    """
    for key,value in kwargs.items():
        print(f'Key: {key}, Value:{value}')

saludar_dos(nombre='Julian', saludo='Hi!', primerkwarg='Como estas?', segundokwarg='Nos vemos')
