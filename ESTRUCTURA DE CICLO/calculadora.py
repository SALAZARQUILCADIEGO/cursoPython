# from optparse import Option


# n1 = float(input("Introduce tu primer número: ") )
# n2 = float(input("Introduce tu segundo número: ") )

# opcion = 0
# while True:
#     print("""
#     Dime, ¿qué quieres hacer?
    
#     1) Sumar 
#     2) Restar 
#     3) Multiplicar 
#     4) dividir
#     5) salir
#     """)
#     opcion = int(input("Elige una opción: ") )     

#     if opcion == 1:
#         print(" ")
#         print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
#     elif opcion == 2:
#         print(" ")
#         print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
#     elif opcion == 3:
#         print(" ")
#         print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
#     elif opcion == 4:
#         print(" ")
#         print("RESULTADO: la divicion de",n1,"*",n2,"es igual a",n1/n2)
#     elif opcion == 5:
#         break
#     else:
#         print("Opción incorrecta")

## calculadora con match

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar 
    2) Restar 
    3) Multiplicar 
    4) dividir
    5) salir
    """)
    opcion =(input("Elige una opción: ") )   
    n1 = float(input("Introduce tu primer número: ") )
    n2 = float(input("Introduce tu segundo número: ") ) 

    match opcion:
        case "1":
            print(" ")
            print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
        case "2":
            print(" ")
            print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
        case "3":
            print(" ")
            print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1*n2)
        case "4":
            print(" ")
            print("RESULTADO: la divicion de",n1,"*",n2,"es igual a",n1/n2)
        case "5":
            break
        case __:
            print("esta opcion no existe")

