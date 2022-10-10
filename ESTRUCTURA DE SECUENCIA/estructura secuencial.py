##estructura secuencial en python
## La estructura secuencial es aquella en la que una accion (instruccion) sigue a otra en secuencia.
## Las tareas se suceden de tal modo que la salida de una es la entrada de la siguiente y asi 
## sucesivamente hasta el fin del proceso. Una estructura secuencial  se representa de la siguiente forma:

  Inicio

     Accion1

     Accion2

     AccionN

  Fin
  ## ejercicio .
  ##Un alumno desea saber cual sera su calificacion final en la materia de Algoritmos.
  ## Dicha calificacion se compone de los siguientes porcentajes:
##55% del promedio de sus tres calificaciones parciales.
##30% de la calificacion del examen final.
##15% de la calificacion de un trabajo final.
  Inicio

         Leer c1, c2, c3, ef, tf

         prom = (c1 + c2 + c3)/3

         ppar = prom * 0.55

         pef = ef * 0.30

         ptf = tf * 0.15

         cf = ppar + pef + ptf

         Imprimir cf

  Fin
  