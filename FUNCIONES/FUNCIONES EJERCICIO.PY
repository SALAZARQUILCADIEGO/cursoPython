#EJERCICIOS
def calcular(importe, descuento): 
    return importe - (importe * descuento / 100) 

datos = {"descuento": 10, "importe": 1500} 
print (calcular(**datos))
