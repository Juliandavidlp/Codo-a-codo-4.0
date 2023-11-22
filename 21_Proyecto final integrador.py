"""
Trabajo Práctico final - Codo a Codo 4.0
Comisión 23421


Alumno:
Dorao Julián


# Hacer un programa que permita ver el menú de una cafetería y comprar un producto:


-Definir una lista con la carta y los precios.
-Definir una función para agregar productos al carrito.
-Definir una función para mostrar el total de los productos seleccionados.
-Definir una función para eliminar un elemento seleccionado.


"""


# La carta:


Cafetería=[
     
     "1~CAFETERÍA",
    "Expresso     $ 700",
    "Americano     $ 760:",
    "Submarino     $1000",
    "Capuccino Expresso     $1160",
    "Mokaccino     $1160",
    "Yogurth con granola y frutas     $1160", 
    "Té de hebras     $ 990"

]



Panadería=[
    "2~PANADERÍA",
    "Croissant de jamón y queso     $2520",
    "Croissant     $ 880",
    "Croissant de almendras     $1070",
    "Croissant de dulce de leche     $1070"
]


Desayunos_y_Meriendas= [
    "3~DESAYUNOS Y MERIENDAS",
    "Café con leche, pan, mermelada y queso crema.       $3120",
    "Tostado inglés con jamón y queso.       $2640"
]




#La impresión de la carta:


print("\n")
print("\n")
print (":::MASSE du Marché:::")
print("\n")


for i in Cafetería:
    print(i, end="\n")

print("\n")
for i in Panadería:
    print(i, end="\n")

print("\n")
for i in Desayunos_y_Meriendas:
    print(i, end="\n")

print("\n")


#Funciones:

carrito=[]

def Agregar_al_carrito():
        
        carrito.append(input("Ingrese el producto seleccionado: "))
        print("Producto agregado con éxito.")
        print("\n")
        print("\n")
        

import re
def verCarrito():
    if carrito==0:
        print("El carrito está vacío.")
    else:
            print("Usted lleva: ", carrito)
            cadena="".join(carrito) 
            print("TOTAL:  $", sum([int(s) for s in re.findall(r'-?\d+\.?\d*', cadena)]))
            print("\n")
            print("\n")
            

#El método texto.join() es para pasar los elementos de una lista a una cadena de texto.
# El método re.findall() es para ubicar un elemento en una cadena e imprimirlo. En este caso, busca los números enteros y los imprime.


def eliminarProducto():

    productoaeliminar=input("Ingrese el producto que desea eliminar: ")
    carrito.remove(productoaeliminar)
    print("Producto eliminado.")
    print("\n")
    
    print("Usted lleva: ", carrito)
    cadena="".join(carrito) 
    print("TOTAL:  $", sum([int(s) for s in re.findall(r'-?\d+\.?\d*', cadena)]))
    print("\n")
    print("\n")


#El menú de opciones:

menú_de_opciones=0


while menú_de_opciones !=3:
    print("\n")
    print (":: Menu en Ligne ::")
    print("\n")
    print("1. Agregar al carrito")
    print("2. Ver el total, el contenido del carrito")
    print("3. Eliminar del carrito")
    print("4. Salir")


    print("\n")
    menú_de_opciones=int(input("Seleccione una opción: "))
    print("\n")

    if menú_de_opciones==1:
        Agregar_al_carrito()   

    elif menú_de_opciones==2:
        verCarrito()

    elif menú_de_opciones==3:
        eliminarProducto()

    elif menú_de_opciones==4:
        print("Hasta luego!")
        print ("\n")

        break
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 4.")
print ("\n")




