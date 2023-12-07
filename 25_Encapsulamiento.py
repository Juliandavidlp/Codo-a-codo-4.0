### Encapsulación | Atributos y métodos protegidos

"""Si el nombre de un atributo de instancia está precedido por doble guión bajo, significa que es un atributo protegido. Solo puede ser accedido por esa clase. Esto es una buena práctica para los atributos (o métodos)
de uso interno, sobre todo en programas complejos con muchas clases. De lo contrario, resulta innecesario.

La encapsulación es el ocultamiento de los atributos o métodos de una clase, para que no se puedan acceder ni modificar desde fuera. Por defecto Python no los oculta. Para hacerlo se usa doble guión bajo (__) 
al comienzo del nombre del método o del atributo con el que trabajo y esto hará que Python lo interprete como “privado”. Por ejemplo:

class Vehiculo: 
    def __init__(self, marca, color):
        self.__marca = marca
        self.__color = color

coche = Vehiculo("Ford", "Rojo")
print(coche.marca)
"""

###Decoradores: getters y setters
"""

Un getter y un setter son métodos que se utilizan en Programación Orientada a Objetos para acceder y modificar los atributos o los métodos de una clase cuando el código está encapsulado.
Un getter es un método que se utiliza para obtener el valor de un atributo y permite acceder a un método o atributo privado, mientras que un setter es un método que se usa para modificar o establecer el valor 
de un atributo dado. 

En Python, los getters y setters se definen utilizando los decoradores @property y @nombre.setter. El decorador @property se utiliza para definir un método en un getter, y, por otro lado, el decorador 
@nombre.setter se usa para definir un método en los setteres.
"""

class Bebidas:
    def __init__(self):
        self.__bebida = "de manzana."
        
    @property #Con el método getter accedo a la variable encapsulada...
    def jugo_favorito(self):
        return f"La bebida es {self.__bebida}"
    
    @jugo_favorito.setter
    def jugo_favorito(self,bebida):
        self.__bebida = bebida
        
    

#Programa principal

máquina_expendedora=Bebidas()
print(máquina_expendedora.jugo_favorito) #La imprimo...
máquina_expendedora.jugo_favorito= "de pomelo." #Y con el método setter modifico la variable respectiva.
print(máquina_expendedora.jugo_favorito)
print("\n")
