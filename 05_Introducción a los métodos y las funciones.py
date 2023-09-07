"""
Introducción a los métodos y las funciones:

Respecto a las cadenas, para las cadenas de texto hay funciones y métodos. Las funciones, como por ejemplo len()
que es para saber cuántos caracteres tiene una cadena, se colocan por fuera del paréntesis, antes de la cadena.
Por el contrario, los métodos se colocan dentro de la cadena, con un punto, en el paréntesis. Ejemplos:
"cadena".capitalize()  #Para poner la primera letra de un texto en mayúscula y las demás en minúscula

"cadena".upper()   #Para poner todas las letras de la cadena en mayúsculas.



Nota: La función round() redondea una número entero para arriba. Si quiero agregar dos decimales,
le agrego una coma y le indico que me lo redondee con dos decimales incluidos después después del número
en el argumento, por ej.: print (round(45.8999,2)).
"""



from math import sqrt, trunc

print (trunc(sqrt(25)))


""" 
Para trabajar con sqrt y trunc hay que invocar o llamar a la librería que las contiene:

* sqrt Es para hacer la raíz cuadrada del número que le pasamos como argumento.
* trunc El truncado conserva el número entero, eliminando los decimales.



"""
