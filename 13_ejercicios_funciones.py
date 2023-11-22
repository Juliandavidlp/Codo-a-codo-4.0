# Ejercicios 1

# Hacer una funcion EsPar (param) que reciba como parametro un numero entero y retorne verdadero o falso segun sea par o no

# Ejercicio 2

# Crear una función que reciba como parámetro 3 numeros y retorne el mayor

'''
def mayor(num1, num2, num3):
    numMayor = -99999999       

    if (num1 > numMayor):
        numMayor = num1

    if (num2 > numMayor):
        numMayor = num2

    if (num3 > numMayor):
        numMayor = num3

    return numMayor

print("El resultado es " + str(sum(50, 20, 52)))

'''

# Ejercicio 3

# Hacer una función que se llame esPar que reciba un numero entero como parametro y retorne verdadero si es par y falso si no lo es.

'''
def esPar(numero):
    if (numero%2 == 0):
        return True; 
    else:
        return False;    

# print(esPar(9))

lista = [1004, 3, 4, 9]

for i in range(0, 4, 1):
    if(esPar(lista[i])):
        print(lista[i])
'''



# Ejercicio 4

# Hacer una función cuantasVeces que reciba dos parametros, el primero un texto y el segundo una letra, y retorne la cantidad de veces que aparece esa letra en el texto. Si no aparece retorne 0.

# def cuantasVeces(texto, caracter):
#     ...

# cuantasVeces("Pedro desconoce la ciudad", "e")

'''
def cuantasVeces(texto,letra):
    print("En el siguiente texto:",texto," , se encuentra presente la letra","",letra,"", texto.count(letra), ", veces")
'''


# cuantasVeces(texto,letra)

'''
def cuantasVeces(texto, letra):
    suma=0
    for i in range (0,len(texto),1):
        if letra == texto[i]:
            suma=suma+1

    return(suma)


text=input("Ingrese texto ")
letter=input("ingrese letra y le diremos cuantas veces la letra esta en el texto ")

print(cuantasVeces(text, letter))
'''
'''
# nombre = "Pedro"

# ("P","e","d","r","o")
'''

# Ejercicio 5

# Hacer una función llamada realizar_operaciones que que reciba dos parametros numéricos enteros, y retorne la suma, resta, multiplicacion y division entre ambos numeros y tambien retorno cual es el cuadrado de cada numero. 

'''
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def elevarAlCuadrado(num):
    # return pow(num,2)
    # return num * num
    return num**2

def elevarAlCubo(num):
    # return pow(num,2)
    # return num * num
    return num**3


def realizar_operaciones(numero1, numero2):
    print("La suma de los numeros es " + str(sumar(numero1, numero2)))
    print("La resta de los numeros es " + str(restar(numero1, numero2)))
    print("La multiplicacion de los numeros es " + str(multiplicar(numero1, numero2)))
    print("La division de los numeros es " + str(dividir(numero1, numero2)))
    print("El cuadrado del primer numero es " + str(elevarAlCuadrado(numero1)))
    print("El cuadrado del segundo numero es " + str(elevarAlCuadrado(numero2)))
    print("El cubo del primer numero es " + str(elevarAlCubo(numero1)))
    print("El cubo del segundo numero es " + str(elevarAlCubo(numero2)))


# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))

# realizar_operaciones(10, 5)

realizar_operaciones(4, 2)

'''


# Ejercicio 6

# Hacer una funcion que reciba un texto, y devuelva verdadero si el texto inicial es igual al texto escrito al reves

# Ej: Amigo  -> ogima false 
# Ej: Ana    -> anA   true 

# let text = "How are you doing today?";
# const myArray = text.split(" ");


'''

palabra = "Neuquen"

listaPalabra = list(palabra.lower())

listaPalabraReves = listaPalabra.copy()

listaPalabraReves.reverse()

print(listaPalabra)
print(listaPalabraReves)

if listaPalabra == listaPalabraReves:
    print("True")
else:    
    print("False")

# Solucion 1

def palindromo(texto):
    listaPalabra = list(texto.lower())

    listaPalabraReves = listaPalabra.copy()

    listaPalabraReves.reverse()

    if listaPalabra == listaPalabraReves:
        return "True"
    else:    
        return "False"


print(palindromo("Luz azul"))
'''
'''



'''

'''

# Solución 3

'''
def alReves(texto):

    reves = ""

    for i in range(len(texto)-1,-1, -1): 
        reves= reves + texto[i]

    return reves


def palindromo(texto):

    texto = texto.lower()
    print(texto)

    # texto = texto.replace(" ","")
    lista = texto.split()
    texto = "".join(lista)

    print(texto)

    if texto == alReves(texto):
        return True
    else: 
        return False


palabra = input("Ingrese una palabra o un texto: ")

print(palindromo(palabra))
'''

'''






# Ejercicio 7
# Hacer una función que reciba una frase es español, y devuelva cuantas palabras hay en la frase, dando por sentado que cada palabra se separa de un espacio de la siguiente.

# Ej: "hola que tal" => 3 
# Ej: "Buenas tardes como estan alumnos" => 5 

# txt = "I love apples, apple are my favorite fruit"

# x = txt.count("apple")

# print(x)

'''
def cantPalabras(texto):
    cantEspacios = texto.count(" ")
    cantPalabras = cantEspacios + 1

    return cantPalabras

cadena = input("Ingrese una frase es español: ")

print(cantPalabras(cadena))


frase = input('ingrese una frase en español: ')

def funcion_contar(palabras):
    lista = palabras.split()
    return(len(lista))

print(funcion_contar(frase))

'''
