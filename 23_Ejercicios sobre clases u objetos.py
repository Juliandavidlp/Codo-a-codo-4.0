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


"""Otro ejercicio:"""

class Movie:
    #pass

    #Atributos generales de las clases
    movies_count = 0

    #Método constructor de la clase
    def __init__(self, title_value, director_value, release_date_value, banner_value):
    #Self hace referencia a la instancia misma de la clase
    #para acceder a los atributos internos de la clase.
    #Es como el this de JavaScript.
        self.title= title_value
        self.director=  director_value  
        self.release_date= release_date_value
        self.banner = banner_value

        self.genres =[]
        Movie.movies_count +=1 #Cuando hago referencia al atributo de la clase uso otra notación

    #Método de la clase
    def play(self):
        print(f"Reproduciendo la película: {self.title}")

    def save(self):
        #Crear el método para que guarde en BBDD
        #Conexión a MySQL -  INSERT INTO movies ()
        #values(self.title, self.banner,self.director)
        pass

    def add_genre(self, genre):
        self.genres.append(genre)

#Ejecuto el método constructor y le paso valores para crear un objeto:
movie1 = Movie("Avatar","Cameron","2023-12-01", "avatar.png") 
#Imprimo con un print y la notación punto:
print(movie1.director)
print(movie1.title)
print(movie1.movies_count)

movie1.title="Titanic" #Modifico un atributo del primer objeto, modifico el valor
#Ejecuto el método play
movie1.play()
#movie1.save()

#Segundo objeto a partir de las mismas intancias de la clase
movie2 = Movie("Batman","Nolan", "2006-01-01", "batman.jpg")
print(movie2.title)
print(movie2.director)
print(movie2.movies_count)

movie2.play()


"""Colaboración entre clases"""
#Movies y reviews, y movies y géneros

#Una clase es parte de otra, en la composición hay relaciones de inclusión, de dependencia entre clases distintas.
#También dos clases pueden tener relaciones de agregación, cuando trabajan de forma independiente.

class Genre:

    #Constructor
    def __init__(self,name):
        self.name=name

    #Método para devolver un valor
    def __str__(self):
        return f"Género: {self.name}"
    
action = Genre("Action")
print(action)

drama = Genre("Drama")
print(drama)

comedy= Genre("Comedy")
print (comedy)




