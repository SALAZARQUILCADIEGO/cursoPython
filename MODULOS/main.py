#aqui en main ejecutare mis funciones
from funciones import operaciones,saludo
#import funciones as op
respuesta1=operaciones(10,8,"suma")
respuesta2=operaciones(100,20,"resta")
respuesta3=operaciones(5,10,"multiplicacion")
print(f'la suma es {respuesta1}')
print(f'la resta es {respuesta2}')
print(f'la multiplicacion es {respuesta3}')
print(saludo())