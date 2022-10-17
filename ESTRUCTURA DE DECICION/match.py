mensaje="hola mundo"
texto=input("ingresa un texto :")
match texto:
    case "hola":
     print (mensaje[:])
    case "como estas":
        print(mensaje[:4])
    case "saludos":
        print(mensaje[5:])
    case _:
        print("error")