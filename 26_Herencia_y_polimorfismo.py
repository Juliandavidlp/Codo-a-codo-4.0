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

La herencia múltiple ocurre cuando una subclase deriva de dos o más clases base. Al escribir el código de la subclase, las superclases de las que heredará 
métodos y atributos se indican de la misma forma, separando cada una con una coma. En caso de que ambas superclases tengan un método con el mismo nombre,
se hereda el método de la primera clase que haya declarado (en el ejemplo sería Madre).

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
El código entonces es una implementación de la herencia múltiple en Python. La clase Hijo tiene un método especial __str__ propio y hereda de las clases Madre y Padre dos métodos:
los métodos nombre_de_la_madre y nombre_del_padre se heredan de las clases Madre y Padre, respectivamente.
"""