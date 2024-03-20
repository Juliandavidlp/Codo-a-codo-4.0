"""
¿Cómo recorrer una tupla con un for?

 tupla=(0,1,2,3,4,5)

 for i in (tupla):
     print(i)

 Mostrar los números pares del uno al diez en una lista con un "para" usando la función range:
 lista=[1,2,3,4,5,6,7,8,9,10]

 for lista in range(0,11,2):
     print(lista)

#Hacer un ciclo mientras contando hasta cinco:

acumulador=0

while acumulador <= 5:
    print(acumulador)
    acumulador+=1

    
#La sintaxis es "while" + una expresión booleana + ":", primero hay que imprimir la variable 
y después incrementar la variable acumuladora. Un contador cuenta eventos, mientras que una variable acumuladora acumula valores.
Un contador se incrementa en 1, mientras que una variable acumuladora se actualiza con una operación matemática. El objetivo 
de un contador es obtener un conteo, mientras que el objetivo de una variable acumuladora es obtener un resultado total.

#Un contador

cont = 0
for i in range(10):
    if i % 2 == 0:
        cont += 1

print(f"Cantidad de números pares: {cont}")

#Variable acumuladora

suma = 0
for i in range(1, 11):
    suma += i

print(f"Suma de los números del 1 al 10: {suma}")


#Hacer dos ejercicios que impriman mediante un "for" y un "while" los números del diez al uno.


for variable in range (10,0, -1):
    print (variable)


# Una variable acumuladora:

sumaVentas=4
sumaVentas= sumaVentas + 4

print(sumaVentas)


# Se puede reescribir de esta manera...

sumaVentas=4               
sumaVentas+=4     

print(sumaVentas)

"""
variable=10

while variable >= 0: 
    print(variable)
    variable-=1

