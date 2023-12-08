###Herencia

"""
La herencia es un mecanismo de la Programación Orientada a Objetos (POO) que permite crear clases nuevas a partir de
clases preexistentes. Usando este concepto, las clases nuevas pueden tomar (o heredar) atributos y métodos de clases
anteriored, e incluso pueden modificarlos.

La clase que aporta los métodos y atributos para heredar se la denomina clase base, superclase o clase padre,
y las que se construyen a partir de esta son clases hijas, derivadas o subclases.
"""
### Herencia, superclases y subclases

"""
Una superclase es una clase superior (o clase madre). Si habíamos considerado las clases como “plantillas” 
para construir objetos, siguiendo esa analogía las superclases serían “plantillas de plantillas”.
A partir de una superclase podemos definir subclases (o clases derivadas), que compartan atributos y métodos 
con la superclase, aunque también puedan sumar métodos y atributos propios.

Para utilizar el concepto de herencia es necesario identificar una clase base (la superclase) que tenga
atributos y métodos comunes, y luego crear otras clases heredadas (las subclases), 
agregando los métodos y atributos que sean necesarios.
"""
###Herencia simple

class Madre: # Superclase
    def __init__(self):
        self.apellido = "Su apellido es Tilbe."
        
    def un_mensaje(self):
        print("Mi vieja es preceptora.")

class Hijo(Madre): #Una subclase
    def estudiar(self):
        print("Yo estoy estudiando.")
        
Damián = Hijo() 
Damián.un_mensaje()
Damián.estudiar()
print(Damián.apellido)


"""
Este es un ejemplo muy simple del concepto de herencia. El objeto hijo ha heredado los métodos y atributos
de la superclase Madre, y podemos utilizarlos en Damián. Vemos cómo un_mensaje() (de la superclase) funciona en
Damián como si fuera un método de la subclase. Y lo mismo ocurre con el atributo apellido. 

Lo importante es entender las subclases se heredan o devienen de las superclases. De una superclase se pueden
construir muchas subclases derivadas. Por ejemplo, de una superclase Persona podríamos derivar Docente, Empleado,
Cliente, Proveedor, o las que sean necesarias para la aplicación que estemos desarrollando. 
"""