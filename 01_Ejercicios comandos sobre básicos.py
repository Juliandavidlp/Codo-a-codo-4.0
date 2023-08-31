#Ejercicios sobre comandos básicos


cantMujeres= int(input("Ingrese la cantidad de mujeres del curso: "))
cantHombres=  int(input("Ingrese la cantidad de hombres del curso: "))

totalAlumnos= cantMujeres + cantHombres

porcentajeHombres= round(cantHombres / totalAlumnos * 100, 2)
porcentajeMujeres= round(cantMujeres / totalAlumnos * 100, 2)



print ("El total de alumnos es: ", totalAlumnos)
print ({porcentajeHombres}, "son hombres y ", {porcentajeMujeres}, "son mujeres.")







