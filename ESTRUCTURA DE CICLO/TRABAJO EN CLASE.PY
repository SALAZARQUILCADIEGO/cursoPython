## crear  un programa que me pida mi edad
##si ingreso una edad incorrecta el programa seguira pidiendo mi edad
##si es la edad correcta me mostrata u  mensaje de correcto
## se terminara la ejecucion.

## datos para saber la edad actual
año = int(input("Ingrese el año en el que nacio"))
año_actual = int(input("Ingrese el año actual"))
edad_correcta = año_actual - año
print("su edad actual es ", edad_correcta)
## datos que el usuario me da 
edad_actual=1
while edad_actual <=3:
  edad_actual= int(input("introdusca su edad"))
if edad_actual != edad_correcta:
    edad_actual=int(input(" su edad no es la coreecta vuelva a introducir su edad que sea la correcta por favor"))
if edad_actual==edad_correcta:
    print("su edad es correcta el programa a terminado")

