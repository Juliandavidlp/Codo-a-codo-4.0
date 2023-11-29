###Clases u objetos: Un ejercicio.
"""
El siguiente ejercicio implementa lo explicado:

● Primero hago una clase llamada "Alumno", que posee un atributo de clase (nro_alumnos) que lleva la cuenta de los objetos instanciados.
● Entonces se definen los métodos para inicializar los atributos de cada objeto que posee un nombre y una nota, para imprimir el estado del objeto 
  y para eliminarlo de la memoria. 
● En el programa principal se instancia un objeto de la clase Alumno y se 
muestran algunas de sus características. Al salir del programa se ve como sus datos se eliminan de la memoria.
●Además, se muestra un mensaje según el mérito del alumno, según la nota.
"""
#Primero instancio la clase.
class Alumno:
    nro_alumnos=0   

#Con el método constructor le instancio valores a la clase:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

        Alumno.nro_alumnos+=1

#Muestro los datos del objeto.
    def __str__(self):
        return f"Nombre: {self.nombre} (Nota:{self.nota})"

    
#Doy de baja un valor, un alumno.
    def __del__(self):
        Alumno.nro_alumnos-=1  #Resto un alumno
    
        print("Alumno dado de baja.")
        print(f"Quedan {Alumno.nro_alumnos} alumnos")
        print(end="\n")
    

    def mostrar_estado(self):
        if alumno.nota < 4:
            print("La nota es regular.")
            print(end="\n")
        elif alumno.nota >4 and 8:
            print("Está aprobado.")
            print(end="\n")
        else: 
            print("La nota, excelente.")
            print(end="\n")


#Instancio un objeto
alumno=Alumno("Damián", 10)

#El programa principal:
print(alumno)
alumno.mostrar_estado()



