# Ejercicio 1:

# Crear una función que reciba como parámetro un número entero 
# y retorne V o F según este sea par o impar.
"""
def espar(numero):

    if numero %2 == 0:
        print("Verdadero")
    else:
        return("Falso")

print(espar(19))



# Ejercicio 2: 
# Hacer una función que reciba dos números enteros y retorne el mayor de ambos.


def elnumero_mayor(num1,num2):
    if num1>num2:
        print(f"El {num1} es mayor")
    elif num1<num2:
        print (f"El {num2} es mayor")
    else: 
        print("Ambos son iguales")        

elnumero_mayor(10,1)


# Ejercicio 3:
# Hacer un algoritmo que reciba dos parámetros, primero un texto, después una letra, 
# y una función que devuelva la cantidad de veces que aparece esa letra en el texto respectivo.

def cuántasVeces (texto, letra): 
        
        suma=0

        for i in range(0,len(texto),1):
            if letra==texto[i]:  
                suma+=1
        return  ("La cantidad de veces que aparece la letra es:",suma)



print(cuántasVeces("Todo va a salir bien, Julian","a"))



# Ejercicio 4:
# Hacer una función que reciba dos parámetros numéricos enteros y retorne la suma
# y la resta entre ambos argumentos, y una función que las englobe.



def sumar (num1,num2):
    return num1+num2

def restar (num1,num2):
    return num1-num2


def sumar_y_restar (num1,num2):

    print("La suma es", str(sumar(num1,num2)))
    print("La resta es", str(restar(num1,num2)))


sumar_y_restar(10,5)



# Ejercicio 5:

# Crear un programa que coteje si una palábra es un palíndromo,
# y devuelva Verdadero o Falso según ese criterio.

def alReves(palábra):
    revés=""            #Crea una variable vacía de texto.

    for i in range (len(palábra),1,-1):
        revés+=palábra
        return revés
    
alReves("Neuquén")
def palíndromo(texto): 

    texto=texto.lower()   #Transformo en minúscula el texto pasado como argumento.
    if texto==alReves(palábra):
        return True
    else: 
        return False  


palábra=input("Por favor, ingrese una palábra sin acentos: ")

print(palíndromo(palábra))

"""



# Otra solución:


def palíndromo (palábra1):
    return palábra1 [::-1]

palábra1=input('ingrese una palábra sin acentos para cotejar si es un palíndromo: ')
palábra1.lower()

palábra2 = palíndromo(palábra1)

if palábra1 == palábra2:
    print(f'{palábra1} es un palindromo')
else:
    print(f'{palábra1} no es un palindromo')

palábra1.lower()
















