#tendremos una variable con el mensaje hola mundo
#pedimos al usuario un texto
#si el texto ingresado es hola
#mostrara el mensaje completo
#si el texto ingresado es como estas
#mostrara lka palabra hola
#si el mensjae es saludos 
#mostrara la paalabra mundo
#si engresa otras letras 
#mostrara error
# mensaje="hola mundo"
# texto=input("ingresa un texto :")
# match texto:
#     case "hola":
#      print (mensaje[:])
#     case "como estas":
#         print(mensaje[:4])
#     case "saludos":
#         print(mensaje[5:])
#     case _:
#         print("error")

# comvirtiendo match a if 

from distutils.log import error


mensaje="hola mundo"
texto=input("ingresa un texto")
if texto == "hola":
    print("hola mundo")
elif texto =="como estas":
    print("hola")
elif texto=="saludos":
    print("mundo")
else:
    print("error")