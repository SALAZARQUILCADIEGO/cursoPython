#difinicion de funciones
# numero="10"##"10"
# int(numero)##10
## int es el nombre de la funcion
##()y dentro de los parentesis van los parametros
sentence=input("ingrese una oracion")
def countvocals(texto):
    vocales=["a","e","i","o","u"]
    contadorvocales=0
    for letras in texto:
        if letras in vocales:
            contadorvocales+=1
    return contadorvocales
print("la cantidad de vocales es : " ,countvocals("sentence"))

