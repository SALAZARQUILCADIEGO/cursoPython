#ejercicio 1
#escriba un  funcion en python que acepte una lista de numeros y 
#genere otra lista eliminando los duplicados.
# arrayD=[1,1,2,3,4,4,3,4,3,5,7,6,8,8,9,9,0,0]
# def delDuplicate(array):
#     newArray=[]
#     for el in array:
#         if el not in newArray:
#             newArray.append(el)
#     return newArray
# print(delDuplicate(arrayD))

#ejercicio2
#escriba una funcion que acepte una lista y genere otra con numeros pares
# def numPar(array):
#     newArray=[]
#     for i in range(array):
#         if i%2==0:
#             newArray.append(i)
#     return newArray
# array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(numPar(array))

#ejercicio3
#escriba una funcion que acepte una lista de texto y genere otra eliminando
#los duplicados
# def texto(lista):
#   lista1 = []
#   for i in lista:
#     if i not in lista1:
#       lista1.append(i)
#   return lista1
# listaL=["hola","como","estas","hola","estas","hello"]
# print(texto(listaL))

#ejercicio4
#escriba una funcion que acepte una lista y genere otra 
# lista con los nummero primos
import math
def es_primo(numero):
    """
    Funcion que determina si un numero es primo
    Tiene que recibir el numero entero
    """
    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
    # En este bucle, empezamos por el dos hasta un numero anterior a el, por lo
    # que si en el bucle, alguna vez se divide el numero, quiere decir que no es
    # primo
    if (numero<=1):
        return False
 
    for i in range(2, math.ceil(math.sqrt(numero))+1):
        if(numero%i==0 and i!=numero):
            return False
    return True
 
lista = [2, 3, 4, 5, 6, 7, 8, 9, 10]
nuevaLista=list(filter(lambda x: es_primo(x), lista))
print(nuevaLista) # [2, 3, 5, 7]



