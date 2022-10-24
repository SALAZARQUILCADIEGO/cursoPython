condicion=True
while condicion==True:
    numero=int(input("ingrese un numero"))
    if numero%2==0 or numero%3==0:
        print("no es primo")
    else:
        print("es primo")
        condicion=False

