#aqui creare mis funciones
def operaciones(num1,num2,operador):
    if operador=="suma":
        total=num1+num2
    if operador=="resta":
        total=num1-num2
    if operador=="multiplicacion":
        total=num1*num2
    if operador=="divicion":
        total=num1/num2
    return total
def saludo():
    mensaje="hola queridos amigos"
    return mensaje

