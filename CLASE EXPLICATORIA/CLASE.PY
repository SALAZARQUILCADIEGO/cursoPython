#ejercicio for
contraseña="73465571"
for intentos in range(1,4):
    print("este es tu ",intentos,"intento")
    newcontraseña=input("ingresa la contraseña correcta:")
    if newcontraseña==contraseña:
        print("bienvenido al sistema joven")
        break
    else:
        print("contraseña incorrecta sigue intentando")
