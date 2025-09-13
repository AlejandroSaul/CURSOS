'''Algoritmo expresion Booleana
 Inicio
    Asignar True a A
    Asignar False a B
    Asignar True a C
    
    evaluar la expresion (A and B) OR (NOT C)
    mostrar resultado de la evaluacion
 FIN'''

A = True
B = False
C = True

D = (A and B) or (not C)
D = A and B or not C

print("D es",D)
