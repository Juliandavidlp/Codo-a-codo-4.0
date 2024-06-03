"""
# Pedirle al usuario que ingrese un número, sumarlo y que el programa repita el proceso hasta llegar al número 999.

num= int(input("Por favor, ingrese cualquier número para iniciar el programa: "))

nrodeciclo=0
acumulador=0


while num<=999:

    nrodeciclo+=1
    acumulador+=num
    num= int(input("Por favor, ingrese un número: "))


    print("Número de ciclo:", nrodeciclo)
    print("Acumulado:", acumulador)





# Hacer un algoritmo que permita ingresar un número entero positivo y dé por pantalla su tabla de multiplicar.

num= int(input("Ingrese un número entero positivo: "))

for i in range (0,11):           #El "hasta" en Python es hasta el número anterior asignado.

    print(num, "*", i, "=", num*i )





# Hacer un algoritmo donde la persona ingrese el número de mundiales que ganó Argentina y el sistema retorne la cantidad de estrellas que ganó la selección.

num=int(input("Ingrese el número de mundiales que ganó Argentina: "))

for i in range (num):
    print("*", end=" ")  
    
    

                         #El bloque end=" " es para imprimir en la misma línea y agregar un espacio.

                         



# Mostrar los números pares del 0 al 100

for i in range (0,101,2):
    print (i)

"""

#Estructuras repetitivas
peliculas=[" Batman ", " Avatar ", " Titanic ", " El padrino "]

#Ciclo Mientras-WHILE
i=0
while i < len(peliculas):
    print(f'Película:{peliculas [i]}')
    i=i+1 #i+=1


#Ciclo FOR
#rango=range(2,10,2);

for x in range(2,10,2):
    print(x)

for peli in peliculas:
    print(f'Película: {peli}')

for i in range(len(peliculas)):
    print(peliculas[i])




