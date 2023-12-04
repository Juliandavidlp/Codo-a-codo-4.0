###Programación orientada a objetos

"""
En el paradigma de programación orientada a objetos (POO) se utilizan
entidades que representan elementos del problema a resolver que tienen
atributos y comportamientos, que pueden almacenar datos y realizar acciones.
Las entidades se denominan objetos, Python proporciona soporte para este paradigma.

La POO permite que el desarrollo de grandes proyectos de software sea más
fácil e intuitivo, al representar en el software objetos del mundo real y sus
relaciones.

La programación orientada a objetos surgió en los años 70 y tuvo un gran auge en
los 90. Uno de los lenguajes destacados de este nuevo paradigma es Java.
Y por supuesto, el concepto de la POO excede a Java y a Python, ya que se aplica
a otros lenguajes.
"""

###Clases u objetos

"""
A diferencia de la programación estructurada, que está centrada en las
funciones, la programación orientada (POO) se basa en la definición de
clases u objetos.

Podemos pensar en las clases como capas o plantillas que definen de manera genérica
cómo van a ser los objetos de determinado tipo. Por ejemplo, una clase para
representar a las personas puede llamarse Persona y tener una serie de
propiedades como Nombre, Edad o Nro de DNI (similares a variables), y una
serie de comportamientos, como Hablar(), Caminar() o Comer(). Estos
comportamientos se implementan como métodos (similares a funciones).

Una clase no es más que un concepto, sin entidad real. Para poder utilizar un objeto
en un programa hay que instanciarlo, es decir, crear un objeto en una clase. 
Un objeto es una entidad concreta que se crea a partir de la capa de la clase.
Este tiene "existencia" real ya que ocupa memoria y se puede utilizar en el programa. 

Así, un objeto puede ser una persona que se llama Ivana, de 37 años cuyo DNI es 32456822, que en
nuestro programa puede hablar, caminar o comer, según los comportamientos definidos en la clase.
Una clase equivale a la generalización de un tipo específico de objetos. 
Y una instancia es la concreción de una clase en un objeto.


Conceptos relacionados:

● Atributos: Son datos que caracterizan al objeto y almacenan datos
relacionados con su estado.

● Métodos: Caracterizan el comportamiento del objeto. Son las acciones
que el objeto puede realizar por sí mismo, como responder a solicitudes
externas o actuar sobre otros objetos. Pueden depender de, o modificar
los valores de un atributo.

● Identidad: Cada objeto tiene una identidad que lo distingue de los otros
objetos, sin considerar su estado. Por lo general, esta identidad se crea
mediante un identificador que deriva naturalmente de un problema (por
ejemplo: un producto puede estar representado por un código, un
automóvil por un número de modelo, etc.).
"""

###Clases | Definición

"""
Los nombres de las clases se escriben en "camelCase". Las clases se definen 
con la palabra clave class, seguida del nombre de la clase y dos puntos. 
Los objetos se declaran como variables, y se accede a sus atributos utilizando la notación
punto.
"""

class persona: #Defino una clase
    piernas=2
    brazos="Tiene dos brazos"
    #Atributos, presentes en los objetos que pertenecen a la clase.


###Definición de objetos
"""
Ojo. Instancio un objeto como una variable de la clase. 
La variable de la clase tiene que tener el mismo nombre...
"""
Damián= persona() 

print(Damián.brazos)
#Imprimo un atributo del objeto instanciado.

"""
Los objetos pueden tener sus propios atributos, llamados atributos de instancia.
Una manera de crearlos es usar directamente la "notación punto":
"""

Damián.edad=19
#Creo un atributo de instancia para el objeto instanciado. Fijate la notación... Ojo!!!
print(Damián.edad)
print("\n") 

#Pero existe una manera más ordenada de hacer esto desde la clase.

###Atributos de clase

"""
Las variables dentro de la clase (atributos de clase) son compartidas por todos 
los objetos instanciados. Se definen dentro de la clase pero fuera de sus métodos:
"""

class Persona:
    piernas="Tiene dos piernas" 
    #Un atributo de clase.

Julián=Persona()
Julián.edad=27

print(Julián.edad)
print(Persona.piernas)

# Podemos acceder a los atributos de clase o del objeto por medio de la notación punto:
# clase_u_objeto.atributo
print("\n")


"""
#Un ejercio:

#Crear una clase individuo e instanciar un objeto con un atributo de instancia.
#Imprimir los atributos de clase e instancia.

class Individuo:
    sexo="masculino"

Damián=Individuo() #Instancio un objeto como una variable de la clase
Damián.altura="Mide 1,90 mts"

print(Damián.altura)
print(Individuo.sexo)

"""


###Clases | Métodos
"""
Los métodos permiten a los objetos de una clase realizar distintas acciones. Se declaran 
con def:, como las funciones, pero dentro de la clase. Reciben parámetros y su primer
parámetro (self) es obligatorio:
"""

class Persona:
    situación_académica="Estudia"

    def estudiar(self): #Defino un método. 
        #Self hace referencia a que la instancia pertenece a la clase. 
        print("Lo está logrando.")
        print("\n")

Julián= Persona() 

print(Persona.situación_académica)
Julián.estudiar() #Invoco el método estudiar por medio de la notación punto.

"""
Como excepción, si quiero cambiarle el valor a un atributo de clase desde un método
necesito utilizar self para referirme al mismo, ya que self hace referencia
a la instancia de la clase. Por ej.:
"""

class Persona:
    situación_académica="Estudia"
    def estudiar(self): 
        self.situación_académica="Está recibido"
        print("Lo hizo.")
        


### Clases | Método constructor
"""
Un constructor es un método que nos permite asignarle valores a la clase a partir de parámetros, con los atributos de clase. 
Su primer parámetro es self, y los que sean requeridos para la inicializar el método.

Una vez instanciado el objeto, establecemos los valores de los atributos de clase por medio del constructor,
y ya podemos utilizarlos normalmente. Por ejemplo:
"""

class Persona:
    def constructor(self,nombre,edad): #El método constructor.
        self.nombre=nombre
        self.edad=edad
        #La palabra "self" antecede al nombre del atributo
        
    def imprimir(self): #Un método normal.
        print(f"Hola {self.nombre}, cómo andás? Tenés {self.edad} años.")
    
        
Damián=Persona()
Damián.constructor("Damián",20) #El constructor crea los atributos cuyo nombre comienza por self 
# y copia en ellos los valores pasados como parámetros. 
Damián.imprimir()


###Clases | Método __init__()

"""
Python ofrece un método especial denominado __init__() que simplifica el proceso de instancia y asignación de valores a los atributos.
__init__() permite asignarle valores a los atributos cuando instanciamos un objeto. Por ejemplo:
"""

class Persona:
    def __init__(self,nombre,edad): #El método __init__()
        self.nombre=nombre
        self.edad=edad   

    def imprimir(self): #Un método normal.
        print(f"Hola {self.nombre}, cómo andás? Tenés {self.edad} años.")

# Entonces pasamos los argumentos directamente para que el constructor los asigne a la instancia creada.
Damián=Persona("Damián",21) 
Damián.imprimir()


###Clases | Método __str__()

"""
Para mostrar objetos, Python provee otro método especial, llamado __str__ , que devuelve una cadena de caracteres, por ejemplo,
al imprimir un objeto. El método __str__ tiene un solo parámetro, self. 
"""
class Alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def __str__(self):
        return f"La nota de {self.nombre} es {self.nota}"
    
Damián=Alumno("Damián",10)
print(Damián)
print("\n")


###Clases | Método __del__()

"""
El método especial __del__() se invoca automáticamente cuando el objeto se elimina de la memoria. Se puede utilizar para realizar alguna 
acción especial cuando tiene lugar este evento. Su sintaxis es la que vemos en el ejemplo, y tiene como único parámetro self. 
Los objetos se borran con del, o se eliminan al finalizar el programa.
"""

class Mascota:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def __str__(self):
        return f"El nombre del conejo es {self.nombre}."
    
    def __del__(self): #El método delete(self)
        print("Mascota donada")
        print("\n")

Conejo=Mascota("Frufru")
print(Conejo)


    



