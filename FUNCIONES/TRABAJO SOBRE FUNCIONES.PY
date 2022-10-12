# funciones en Python serán una parte del código de nuestro programa encargadas
# de cumplir algún objetivo específico definido por nosotros o por el lenguaje,
# recibiendo ciertos “datos de entrada” (Argumentos) en los llamados Parámetros
# para procesarlos y brindarnos “datos de salida” o de retorno.
# en las funciones encontramos a def , return , len() , print(),none
#return // se utiliza  para devolver un valor 
#def // Dividir y organizar el código en partes más sencillas
# len() // obtiene el número de elementos de un objeto contenedor como una lista
# print () // muestra por consola un texto.
# none // cuando en una función no aparece la sentencia return o esta no devuelve nada.
# NOTA: Cuando la primera instrucción de una función es un string encerrado entre
#    tres comillas simples ''' o dobles """, a dicha instrucción se le conoce como  docstring.
#  El docstring es una cadena que se utiliza para documentar la función, es decir, indicar qué hace dicha función.

#ejercicios
def multiplica_por_5(numero):
    print(f'{numero} * 5 = {numero * 5}')
print('Comienzo del programa')    
multiplica_por_5(7)
print('Siguiente')
multiplica_por_5(113)
print('Fin')
#IMPORTANTE: Diferencia entre parámetro y argumento. 
#La función multiplica_por_5() define un parámetro llamado numero.
#Sin embargo, cuando desde el código se invoca a la función, por ejemplo, multiplica_por_5(7),
# se dice que se llama a multiplica por cinco con el argumento 7.