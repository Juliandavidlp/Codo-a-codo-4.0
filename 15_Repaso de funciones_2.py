#Pasaje de argumentos por valor con datos inmutables.
def triplicar_valor(numero):
    numero *= 3
    return numero

valor_original = 10
print(f'El valor triplicado es: {triplicar_valor(valor_original)}')



#Pasaje de argumentos por referencia a partir de datos mutables 
def agregar_elemento(lista,elemento):
    lista.append(elemento)

lista_original = [4,5,7,10]
agregar_elemento(lista_original,89)

print(lista_original)

#¿Cómo devolver varios valores en una función?:

def obtener_estadisticas(lista):
    suma= sum(lista)
    promedio= suma / len(lista)
    maximo= max(lista)
    minimo= min(lista)

    return (suma, promedio,maximo, minimo) 
            #Devuelve las operaciones en una lista.
    

valores=[4,6,1,70,44]
resultados= obtener_estadisticas(valores)
print(resultados)


# ¿Cómo desempaquetar la lista?
s,p,maxi,mini= obtener_estadisticas(valores)
#Desempaquetar los elementos o variables.

#Desempaquetado ignorando elementos finales

suma= obtener_estadisticas(valores)
promedio= obtener_estadisticas(valores)
print(f"La suma es {s} y el promedio es {p}")

#Desempaquetado ignorando elementos intermedios

s, _, _, minimo= obtener_estadisticas(valores)
print(f"La suma es {s}, el mínimo: {minimo}")

