evalue=True
while evalue==True:
    numero=int(input("ingrese el numero de la tabla que deseas mostrar:"))
    if numero==0:
        print("error saliendo del programa")
        break
    else:
        for numeros in range(1,11):
            print(numeros,"*",numero, "=",numeros*numero)


        # if numero!=0:
        #  for numeros in range(1,11):
        #     print(numeros,"*",numero, "=",numeros*numero)  
        # else:
        #  for numeros in range(1,11): 
        #     print("error saliendo del programa")
        # break