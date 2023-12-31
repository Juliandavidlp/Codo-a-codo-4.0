###Herencia

"""
La herencia es un mecanismo de la Programación Orientada a Objetos (POO) que permite crear clases nuevas a partir de
clases preexistentes. Usando este concepto, las clases nuevas pueden tomar (o heredar) atributos y métodos de clases
anteriores e incluso modificarlos.

La clase que aporta los métodos y atributos para heredar se denomina clase base, padre, madre o superclase,
y las que se construyen a partir de esta son clases hijas, derivadas o subclases.
"""
### Herencia, superclases y subclases

"""
Una superclase es una clase superior (o clase madre). Si habíamos considerado las clases como “plantillas” 
para construir objetos, siguiendo esa analogía las superclases serían “plantillas de plantillas”.
A partir de una superclase podemos definir subclases (o clases derivadas), que compartan atributos y métodos 
con la superclase, aunque también puedan sumar métodos y atributos propios.

Para utilizar el concepto de herencia es necesario identificar una clase base (la superclase) que tenga
atributos y métodos comunes, y luego crear otras clases heredadas o subclases, 
agregando los métodos y atributos que sean necesarios.
"""
###Herencia simple

class Madre: # Una clase madre o superclase.
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
print("\n")

"""
Este es un ejemplo del concepto de herencia simple donde el objeto hijo hereda los métodos y atributos
de la superclase Madre, y podemos utilizarlos en Damián. Entonces, vemos cómo un_mensaje() (de la superclase)
funciona en Damián como si fuera un método de la subclase. Y lo mismo ocurre con el atributo apellido. 

Lo importante es entender que las subclases se heredan o devienen de las superclases. De una superclase se pueden
construir muchas subclases derivadas... Por ejemplo, de una superclase Persona podríamos derivar Docente, Empleado,
Cliente, Proveedor, o las que sean necesarias para la aplicación que estemos desarrollando. 
"""

"""
Veamos un ejemplo más complejo. Supongamos que necesitamos una clase que sea capaz de instanciar objetos
que representen a los alumnos de Codo a Codo.
Dado que los alumnos comparten buena parte de sus atributos y métodos con otras personas sería útil 
contar con una superclase llamada Persona que contenga los atributos y métodos comunes todos, con una subclase 
Alumnos_de_Codoa_Codo que herede de ella esos elementos, y sume los que la superclase no tenga o sean necesarios. 
"""

#La definición de la superclase Persona no posee ninguna característica particular. 
class Persona(): #Se define como una clase más: 
    def __init__(self,identificación,apellido,nombre,dni): #El método constructor de persona.
        self.id = identificación #Los atributos de instancia...
        self.nombre = nombre   
        self.apellido = apellido
        self.documento = dni

    def __str__(self):
        return f"{self.id} - {self.nombre},{self.apellido} - DNI {self.documento} "
    
"""
La Persona, que es la superclase de nuestro ejemplo, posee varios atributos de instancia y un método. Y a pesar de que
la voy a utilizar como una superclase, puedo instanciar objetos Persona.
   
# Programa principal:
Damián=Persona(1,"Damián","Dorao",45494842)
print(Damián) 
""" 
"""
El método __str__ de la superclase Persona muestra la cadena de texto que contiene una representación de los atributos 
del objeto Damián. Este método también será heredado por la subclase AlumnoCodo.
""" 
#La subclase

"""
La definición de la subclase Alumno_de_Codo_a_codo incluye en su declaración el argumento “Persona”, que hace referencia
a la superclase. En su constructor,utiliza el método constructor de la superclase y agrega un nuevo atributo de clase, “curso”, 
que no estaba en la superclase Persona. Además, la subclase Alumno_de_Codo_a_codo hereda el método __str__ de la superclase Persona:
"""
class Alumno_de_Codo_a_codo(Persona): # La superclase como parámetro.
# La clase representa a un alumno de Codo a Codo
    def __init__(self,identificación,apellido,nombre,dni,curso): # El constructor del alumno.

        # Invoco al constructor de la superclase...
        Persona.__init__(self,identificación,apellido,nombre,dni)
        #Y le agrego el atributo propio del alumno
        self.comisión=curso 

    def __str__(self):
       return f"{self.id} - {self.nombre},{self.apellido} - DNI {self.documento} - {self.comisión}"

"""
En este punto, tengo la superclase y la subclase definidas. Puedo instanciar objetos de la superclase. 
Y ahora también puedo hacer lo mismo con la subclase:

Damián=Alumno_de_Codo_a_codo(1,"Damián","Dorao",45494842,"Full-Stack en Python de Codo a Codo")
print(Damián)

Pero al imprimir el objeto Damián, estoy usando el método __str__ de la superclase Persona, que fue heredado 
por la subclase Alumno_de_Codo_a_codo, motivo por el que el curso al que pertenece Damián no se muestra por pantalla. 
Y para solucionarlo tuve que agregarle a la subclase un método __str__ que reemplaze al método heredado de la superclase.


"""
# Programa principal:
Damián=Alumno_de_Codo_a_codo(1,"Damián","Dorao",45494842,"Full-Stack en Python de Codo a Codo")
print(Damián) 
print("\n")
print("\n")


###Herencia múltiple
"""

Los casos que hemos analizado tienen lo que se conoce como herencia simple, que tiene lugar cuando una clase derivada (subclase) hereda 
atributos y métodos de una única clase base (o superclase).

La herencia múltiple ocurre cuando una subclase deriva de dos o más clases base. Al escribir el código de la subclase, las superclases 
de las que heredará métodos y atributos se indican de la misma forma, separando cada una con una coma. En caso de que ambas superclases 
tengan un método con el mismo nombre, se hereda el método de la primera clase que haya declarado (en el ejemplo sería Madre).

Desarrollo un ejemplo donde una subclase Hijo hereda métodos y atributos de dos superclases: Madre y Padre.

"""

class Madre(): #Superclase 1
    def nombre_de_la_madre(self):
        print ("Mi mamá es Ema")

class Padre(): #Superclase 2
    def nombre_del_padre(self):
        print ("Mi papá se llama Gabriel")
        print("\n")

class Hijo(Madre, Padre): #Herencia múltiple en la subclase
    
    def __str__(self):
        return ("Voy a aprobar.")
    

Nicolás=Hijo() #Instancio el objeto
Nicolás.nombre_de_la_madre()
Nicolás.nombre_del_padre()

print(Nicolás)


"""
El código entonces es una implementación de la herencia múltiple en Python. La clase Hijo tiene un método especial __str__ propio y hereda de las 
clases Madre y Padre dos métodos: los métodos nombre_de_la_madre y nombre_del_padre se heredan de las clases Madre y Padre, respectivamente.
"""


###Clases abstractas

"""
Un concepto importante en Programación Orientada a Objetos es el de las clases abstractas. Son clases en las que se pueden definir tanto métodos
como propiedades,pero que no pueden ser instanciadas directamente. Solamente se pueden usar para construir subclases (como si fueran moldes), 
permitiendo tener una única implementación de los métodos compartidos. Esto evita la duplicación de código.

Las clases abstractas definen una interfaz común para las subclases. Proporcionan atributos y métodos comunes para todas las subclases evitando así 
la necesidad de duplicar código, imponiendo además los métodos que deben ser implementados para evitar inconsistencias entre las subclases.

Las clases abstractas:

● No pueden ser instanciadas, simplemente proporcionan una interfaz para las subclases derivadas evitando así la duplicación de código.
● No es obligatorio que tengan una implementación de todos los métodos necesarios, ya que estos pueden ser abstractos. Los métodos abstractos 
  son aquellos que solamente tienen una declaración, pero no una implementación detallada de las funcionalidades.
● Las clases derivadas de las clases abstractas deben implementar necesariamente todos los métodos abstractos para poder crear una clase que se ajuste
a la interfaz definida. En el caso de que no se defina alguno de los métodos no se podrá crear la clase.
"""


# Clases abstractas | Creación

"""

Para poder crear clases abstractas en Python es necesario importar la clase ABC y el decorador abstractmethod del módulo abc (Abstract Base Classes).
Si intento crear una instancia de la clase Animal sin lo anterior, Python no lo permite. 

Si importo la clase ABC o el código contiene por lo menos un método abstracto, Python permite crear instancias de la clase. 
De lo contrario, me sale un TypeError con "Can't instantiate abstract class Animal with abstract method mover" o con 
"Can't instantiate abstract class Animal without a implementation for abstract merhod "mover".


from abc import ABC, abstractmethod

class Animal(): #Sin importar la clase ABC
    @abstractmethod #Hay que ponerlo, es como un getter o un setter para definir métodos abstractos.
    def mover(self):
        pass #"Aprobar"

perro=Animal()


Las subclases tienen que implementar todos los métodos abstractos definidos en la clase abstracta, o Python no me va a dejar instanciar la clase hija.
Desde los métodos de las subclases se pueden utilizar las implementaciones de la clase abstracta con el comando super() seguido del nombre del método. 
Por ejemplo:
"""

from abc import ABC, abstractmethod

class Animal(ABC):#Importo la clase ABC
    @abstractmethod 
    def mover(self): #Un método abstracto
        pass

    @abstractmethod
    def emitir_sonido(self):
        print("Miuau, miau!")
        print("\n")

class mascota(Animal):

    def mover(self): 
        pass

    def emitir_sonido(self):
        super().emitir_sonido() 

"""

Los métodos emitir_sonido() y mover() de la subclase mascota completan o complementan el código disponible en los métodos abstractos
homónimos de la clase abstracta Animal. Solo resta instanciar un objeto y ver cómo se comporta:
"""

gato=mascota() 
gato.mover()
gato.emitir_sonido()


###Polimorfismo
"""


El polimorfismo es uno de los pilares básicos en la Programación Orientada a Objetos. El término polimorfismo tiene origen en las palabras poly (muchos)
y morfo (formas), y aplicado a la programación hace referencia a que los objetos pueden tomar diferentes formas. 
Esto significa que objetos de diferentes clases pueden ser accedidos utilizando la misma interfaz, mostrando un comportamiento distinto 
(tomando diferentes formas) según cómo sean accedidos.

En Python, el polimorfismo va muy relacionado con el duck typing o “tipado del pato”, que se resume en una frase: “Si camina como un pato y habla como un pato, 
entonces es un pato”. Como Python es un lenguaje de tipado dinámico no es necesario que los objetos compartan una interfaz, basta con que los objetos compartan los 
métodos que se quieran utilizar. Por ejemplo:
"""

#Defino las clases Pato, Perro y Cerdo
class Pato:
 def hablar(self): 
    print("Cuac")

class Perro:
 def hablar(self):
    print("Guau! "*2)
    
class Cerdo:
 def hablar(self):
    print("Oink..." * 3)



#El programa principal
def hacer_hablar(x): 
    x.hablar() 
    #Gracias al método hacer_hablar(), hablar() será compartido por los objetos del programa.
"""
El programa principal entonces define una función que recibe un objeto, y utiliza (sin importar cual sea) su método hablar(). 
Esto es posible gracias al polimorfismo: no es necesario escribir código para acceder a un mismo atributo o método de objetos de distinta clase,
cuando estos tienen el mismo nombre.

"""
#Creo los tres animales y los hago "hablar":
pato=Pato()
hacer_hablar(pato)

perro=Perro()
hacer_hablar(perro)

cerdo=Cerdo()
hacer_hablar(cerdo)


### Diagrama de clases
"""


Un diagrama de clases en Lenguaje Unificado de Modelado (UML) es un tipo de diagrama de estructura estática que describe la estructura 
de un sistema mostrando las clases del sistema, sus atributos, operaciones (o métodos), y las relaciones entre los objetos.
UML proporciona mecanismos para representar los miembros de la clase, como atributos y métodos, así como información adicional sobre ellos.

En los lenguajes orientados a objetos, los algoritmos se expresan definiendo 'objetos' y haciendo que los objetos interactúen entre sí. 
Los lenguajes orientados a objetos dominan el mundo de la programación porque modelan los objetos del mundo real, y la relación entre sus clases,
atributos y métodos puede modelarse mediante UML.

La figura una clase en sí misma consiste en un rectángulo de tres filas. La fila superior contiene el nombre de la clase, la fila del centro 
contiene los atributos de la clase y la última expresa los métodos o las operaciones que la clase puede utilizar. Por otro lado, cada atributo y método 
de una clase está ubicado en una línea separada. 

Una relación de herencia se simboliza mediante una línea de conexión recta con una punta de flecha cerrada que señala a la superclase. Y una relación
predeterminada entre clases se representa mediante una línea recta.

Para especificar la visibilidad de un miembro de la clase (es decir, cualquier atributo o método), se coloca uno de los siguientes signos
delante de ese miembro:

● Público (+)
● Privado (-)
● Protegido (#)

Una imagen vale más que mil palabras. Es por eso que se creó la generación de diagramas con el Lenguaje Unificado de Modelado (UML): 
para forjar un lenguaje visual común en el complejo mundo del desarrollo de software que también fuera comprensible por los usuarios de negocios 
y quienquiera que desee entender un sistema.

                    Más info. en https://www.lucidchart.com/pages/es/que-es-el-lenguaje-unificado-de-modelado-uml
                                 https://informaticapc.com/poo/uml.php
                                 https://elvex.ugr.es/decsai/java/pdf/3c-relaciones.pdf
"""
