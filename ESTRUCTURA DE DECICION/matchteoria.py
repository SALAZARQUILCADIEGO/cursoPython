# Se da un título a la calculadora.
print("--- CALCULADORA MEJORADA ---")

# Se le pide al usuario que elija una opción y se evalúa
print("Hola, elija una opción:")
print("1- Suma.")
print("2- Resta.")
print("3- Multiplicación.")
print("4- División.")
print("5- Módulo.")
print("6- Exponente.")

# Se le pide al usuario
eleccion = int(input("Teclee un número y pulse ENTER:\n"))

# Una variable para el control de errores
error = True

# Un match para que el usuario decida la opción
match eleccion:
    case 1:
        print('Ha elegido la opción "suma".')
    case 2:
        print('Ha elegido la opción "resta".')
    case 3:
        print('Ha elegido la opción "multiplicación".')
    case 4:
        print('Ha elegido la opción "división".')
    case 5:
        print('Ha elegido la opción "módulo".')
    case 6:
        print('Ha elegido la opción "exponente".')
    case _:
        print('Error, opción inválida.')
        error = False

# Si el usuario elige un valor del menú, se ejecuta el if, si no, el else
if error:
    # Se solicitan los dos números
    numero_1 = float(input("Especifique el primer operando:\n"))
    numero_2 = float(input("Especifique el segundo operando:\n"))
    
	# Un match indentado que ejecuta solo la operación solicitada
    match eleccion:
        case 1:
            resultado = round(numero_1 + numero_2, 2)
            print(f"El resultado de sumar {numero_1} + {numero_2} es: {resultado}.")
        case 2:
            resultado = round(numero_1 - numero_2, 2)
            print(f"El resultado de restar {numero_1} - {numero_2} es: {resultado}.")
        case 3:
            resultado = round(numero_1 * numero_2, 2)
            print(f"El resultado de multiplicar {numero_1} por {numero_2} es: {resultado}.")
        case 4:
            resultado = round(numero_1 / numero_2, 2)
            print(f"El resultado de dividir {numero_1} entre {numero_2} es: {resultado}.")
        case 5:
            resultado = round(numero_1 % numero_2, 2)
            print(f"El resto de la división de {numero_1} entre {numero_2} es: {resultado}.")
        case 6:
            resultado = round(numero_1 ** numero_2, 2)
            print(f"{numero_1} elevado a {numero_2} es: {resultado}.")
else:
    print("Por favor, vuelva a ejecutar la calculadora.")