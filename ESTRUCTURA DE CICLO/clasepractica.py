# escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario 
#escriba "salir" para terminar la ejecucion


# mensaje =""
# while  mensaje!="salir":
#     mensaje=input("escriba algo")
#     print(mensaje)


#ejercicio mostrar las vocales que hay en una palabra u oracion 
# palabra = input(" ingrese la palabra: ")
# vocales = 'aeiou' # tambien se utiliza array
# contador=0
# for x in palabra:
#     if x in vocales:
#       contador+=1
# print("la palabara que ingresaste tiene ",contador ,"vocales")

# otra manera
sentence=input("ingrese un oracion")
countvocals=0
for words in sentence:
    match words:
        case "a":
            countvocals +=1
        case "e":
            countvocals +=1
        case "i":
            countvocals +=1
        case "o":
            countvocals +=1
        case "u":
            countvocals +=1
print("la cantidad de vocales es : ",countvocals)

