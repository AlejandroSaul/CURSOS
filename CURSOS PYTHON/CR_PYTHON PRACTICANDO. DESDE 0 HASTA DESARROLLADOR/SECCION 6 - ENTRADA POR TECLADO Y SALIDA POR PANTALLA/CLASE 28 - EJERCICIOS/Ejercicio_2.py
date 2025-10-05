'''Ejercicio 2
Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
Considere:
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final'''

P1 = float(input('Digite la calificacion de la practica 1: '))
P2 = float(input('Digite la calificacion de la practica 2: '))
P3 = float(input('Digite la calificacion de la practica 3: '))
EP = float(input('Digite la calificacion del examen parcial: '))
EF = float(input('Digite la calificacion del examen final: '))

PP = ( P1 + P2 +P3 ) / 3 
PROM = ( PP + 2*EP + 3*EF ) / 6
print(PP)