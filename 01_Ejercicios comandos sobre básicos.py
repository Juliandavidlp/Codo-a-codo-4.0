#Ejercicios sobre comandos básicos


cantMujeres= int(input("Ingrese la cantidad de mujeres del curso: "))
cantHombres=  int(input("Ingrese la cantidad de hombres del curso: "))

totalAlumnos= cantMujeres + cantHombres

porcentajeHombres= round(cantHombres / totalAlumnos * 100, 2)
porcentajeMujeres= round(cantMujeres / totalAlumnos * 100, 2)

# La función round() en Python redondea un número a una precisión dada por el número de cifras decimales indicadas.
# Si no se indica el número de cifras decimales como argumento, se toma 0 como valor de referencia.
# Su sintaxis es la siguiente: round(número, ndigitos)

print ("El total de alumnos es: ", totalAlumnos)
print (f"{porcentajeHombres}, son hombres y, {porcentajeMujeres}, son mujeres.")
