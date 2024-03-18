"""
# ¿Cómo recorrer una tupla con un for?

# tupla=(0,1,2,3,4,5)

# for i in (tupla):
#     print(i)

# Mostrar los números pares del uno al diez con un "para" usando la función range:
lista=[1,2,3,4,5,6,7,8,9,10]

for lista in range(0,11,2):
    print(lista)
    

# ¿Cómo hacer un ciclo "mientras" en Python contando hasta cinco?

variable=0

while variable<=5:

    print (variable)
    variable= variable+1     #La sintaxis es "while" + expresión booleana + : , y después hay que imprimir la variable y el contador respectivo.

"""


#Hacer dos ejercicios que impriman mediante un "for" y un "while" los números del diez al uno.

"""
variable=10

for variable in range(10,0,-1):
    print (variable)
    



variable=10

while variable > 0:

    print (variable)
    variable= variable-1



# Una variable acumuladora:

sumaVentas=4
sumaVentas= sumaVentas + 4

print(sumaVentas)



# Se puede reescribir de esta manera...

sumaVentas=4               
sumaVentas+=4     

print(sumaVentas)


"""
