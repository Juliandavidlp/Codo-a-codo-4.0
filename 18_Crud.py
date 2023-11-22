# CRUD
# C Create
# R Read
# U Update
# D Delete


nombres = []


def agregar_nombre():
    nombre = input("Ingrese el nombre: ")
    nombres.append(nombre)
    print("Nombre agregado con éxito.")

def consulta_nombres(): 
    if len(nombres) == 0:
        print("La lista está vacía.")
    else:
        for i in range(0, len(nombres),1):
            print(str(i) + ". " + nombres[i])


def actualizar_nombre():
    consulta_nombres()
    print("\n")
    indice = int(input("Ingrese el número del nombre que desea actualizar: ")) 
    nombre = input("Ingrese el nuevo nombre: ")
    nombres[indice] = nombre
    print("Nombre actualizado con éxito.")



def eliminar_nombre():
    consulta_nombres()
    indice = int(input("Ingrese el número del nombre que desea eliminar: "))
    nombre_eliminado = nombres.pop(indice)
    print("Nombre eliminado: " + nombre_eliminado)



opcion = 0

while opcion!=5:
    print("\n")
    print("--- CRUD con Listas de Nombres ---")
    print("1. Agregar nombre")
    print("2. Mostrar nombres")
    print("3. Actualizar nombre")
    print("4. Eliminar nombre")
    print("5. Salir")

    print("\n")

    opcion = input("Seleccione una opción: ")

    print("\n")

    if opcion == "1":
        agregar_nombre()
    elif opcion == "2":
        consulta_nombres()
    elif opcion == "3":
        actualizar_nombre()
    elif opcion == "4":
        eliminar_nombre()
    elif opcion == "5":
        break;
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

    # print("\n")

print("¡Hasta luego!")




