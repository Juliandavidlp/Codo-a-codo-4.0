###Colaboración de clases
"""
Normalmente en un problema resuelto con la metodología de programación orientada a objetos no interviene una sola clase, sino que hay muchas clases que interactúan y se comunican. 
Esta colaboración entre clases se manifiesta como la posibilidad de utilizar en una clase objetos instanciados en una clase diferente. Este mecanismo potencia el alcance que tiene 
la Programación Orientada a Objetos, facilitando aún más el desarrollo de soluciones a problemas complejos sin necesidad de escribir código extenso de difícil de lectura.
Para entender cómo se produce la colaboración entre clases voy a desarrollar un ejemplo, explicando el código paso a paso:

#Un banco tiene dos clientes que pueden hacer depósitos y extracciones, y al final del día necesita imprimir un reporte con la cantidad de dinero depositado.
Entonces, a partir del enunciado, puedo deducir que necesito objetos de dos clases: clientes y un banco.
Para cada entidad necesito crear una clase e instanciar la cantidad necesaria de objetos de la misma. Identificadas las clases, que voy a llamar "Cliente" y "Banco" respectivamente, 
tengo que definir qué atributos y métodos implemento en cada una.

Colaboración de clases | Clase Cliente

En el método __init__ se inicializan los atributos nombre con el valor del parámetro y monto con el valor cero.
Los métodos depositar, extraer, retornar_monto e imprimir se definen como se ve a la derecha.
No se instancian objetos de esta clase en el cuerpo del programa porque los mismos serán atributos de la clase Banco.
"""

class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=2000

    def depositar(self,monto):
        self.monto+=monto

    def extraer(self,monto):
        self.monto-=monto
    
    def retornar_monto(self):  
        return self.monto
    
    def imprimir (self):
        print (f"{self.nombre} tiene depositada la suma de {self.monto}.")

"""
Colaboración de clases | Banco

Al definir la clase Banco se incluye en su constructor la instancia de tres objetos de la clase Cliente. Estos objetos serán utilizados por la clase Banco
para que su instancia (sólo se instancia un objeto de la clase Banco) sea capaz de operar con los clientes.

En el método operar se invocan algunos métodos de la clase Cliente, para generar las transacciones (depósitos y extracciones).
Con el método depositos_totales se calcula la suma de los montos depositados por los objetos de la clase Cliente, y se guardan en la variable total, que luego se muestra
en la terminal mediante print()
"""
class Banco:
    def __init__(self): #Instancio dos objetos de la clase cliente y los asigno a la clase banco como atributos para operar con ellos.
        self.cliente1=Cliente("Damián")
        self.cliente2=Cliente("Julián")

    def operar(self):
        self.cliente1.depositar(2000)
        self.cliente2.extraer(1000)

    #El método operar () llama al método depositar() del objeto cliente1 para depositar 2000 pesos en su cuenta y llama al método extraer() del objeto
    # cliente2 para extraer 1000 pesos de su cuenta. En el Banco anteriormente había 2000 pesos.
     
    def depósitos_totales(self):

        total= self.cliente1.retornar_monto() + self.cliente2.retornar_monto()
        print(f"Los depósitos de los totales son: ${total}")
        print("\n")

        self.cliente1.imprimir()
        self.cliente2.imprimir()
        print("\n")
        print("\n")

"""
Colaboración de clases | Programa principal

En el programa principal se instancia un objeto de la clase Banco, y se invocan sus métodos operar() y depositos_totales():
Al invocar el método operar() de la clase Banco se llama a los métodos depositar() y extraer() de la clase Cliente. Y al llamar al método depositos_totales() de la clase Banco
se llama al método retornar_monto() e imprimir() de la clase Cliente. Ambas clases colaboran para resolver el problema planteado.
"""

#Programa principal:
Banco_Nación=Banco()
Banco_Nación.operar()
Banco_Nación.depósitos_totales()

"""
Atributos de clase

Los atributos de clase, a diferencia de los atributos de instancia, son compartidos por todos los objetos de dicha clase. 
Una clase puede tener varios atributos de instancia, métodos y atributos de clase, que se definen dentro de la clase pero por fuera de los métodos:
"""

class Persona:
    edad=20 #Un atributo de clase.

    def __init__(self,nombre):
        self.nombre=nombre


dato1=Persona("Damián")
dato2=Persona("Ema")

print(f"La edad es {dato1.edad}")
print(f"La edad es {dato2.edad}")
print("\n")

dato1.edad=21 #Un atributo de instancia

print(f"La edad es {dato1.edad}")
print(f"La edad es {dato2.edad}")

"""
Nota: dato1.edad = 21 no modifica el valor del atributo de clase, sino que crea un atributo de instancia que existe solo para ese objeto.
Por lo tanto, cuando vuelvo a consultar su valor, Python imprime "21" que es el valor de su atributo de instancia. Si existe un atributo de clase y uno de instancia con el mismo nombre,
tiene prioridad el de la instancia. En el ejemplo, el cambio de valor no afecta a dato2, que sigue mostrando el valor del atributo de clase.
"""