#definir una funcion max() que tome como argumento un array de numeros y devuelva el mayor del array
# max_num=(1,2,3,4,5)
# def max_num(a,b,c,d,e):
#     if(a > b > c > d > e):
#         return a
#     if(e > d > c > b > a):
#         return e
# print("el numero maximo de array es ")
# print(max_num(1,2,3,4,5))
# escribir una funcion que almacene en una lista los siguientes precios
#  50,75,46,22,80,65,8 y muestre por pantalla el menor y el mayor de los precios 
# precios = [50, 75, 46, 22, 80, 65, 8]
# min = max = precios[0]
# for precio in precios:
#     if precio < min:
#         min = precio
#     elif precio > max:
#         max = precio 
# print("El mínimo es " + str(min)) 
# print("El máximo es " + str(max))

#escribir una funcion mas larga () que tome una array de palabras y devuelva la mas larga
def mas_larga(lista):
	palabra_mayor = len(lista[0])
	palabra_mostrar = lista[0]
	for palabra in lista:
		if palabra_mayor <= len(palabra):
			palabra_mostrar = palabra
			palabra_mayor = len(palabra)
		else:
			palabra_mostrar = palabra_mostrar
	print(palabra_mostrar)
lista = ["diego", "salazar", "836352293 diego salazar"]
mas_larga(lista)

#escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene

 