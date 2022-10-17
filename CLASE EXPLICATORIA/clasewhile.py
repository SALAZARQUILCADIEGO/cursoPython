# ejercicio while
contraseña="73465571"
condicion=True
intentos=1
while condicion==True:
    print("este es tu ",intentos,"intentos")
    newcontraseña=input("ingresa la contraseña correcta:")
    if newcontraseña==contraseña:
        print("bienvenido al sistema joven ilustre")
        condicion=False
    else:
        print("contraseña incorrecta sigue intentando")
        intentos+=1