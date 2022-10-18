# mensaje="hola"
# for letra in  mensaje:
#     print(letra)

#ejercicio2

# mostrar por consola cuantas vocales a tiene la palabra
mensaje=input("ingrese una palabra")
contador=0
for letra in mensaje:
    if letra=="a":
        contador+=1
print("es esta palabra tienes: " , contador ,"la vocal a") 