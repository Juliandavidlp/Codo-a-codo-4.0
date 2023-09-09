"""
#Ejercicio 1:

#Hacer un algoritmo en el que se cree una variable de tipo lista, donde se le puedan ingresar países 
# y mostrar los elementos sin cambiar la lista original.

Lista=["Argentia", "Brasil","Uruguay", "Chile"]

Lista.append(input("Ingrese un país: "))
print(Lista)


#Otra solución: 
# ¿Cómo recorrer una lista y mostrar los elementos del arreglo uno debajo del otro?


Lista=["Damián","Patricia","Julián"]

for i in range (0,3,1):
    print(Lista[i])


    
# Ejercicio 2: Hacer un algoritmo donde se declare una variable de tipo 
# lista que contenga números enteros en cada elemento y muestre la suma de los mismos.

"""

Lista=[5,10,20,15]
print(Lista)
suma=0

for i in range (0,4,1):
    suma+=Lista[i]

print("El total de la suma de los elementos es:", suma)



































