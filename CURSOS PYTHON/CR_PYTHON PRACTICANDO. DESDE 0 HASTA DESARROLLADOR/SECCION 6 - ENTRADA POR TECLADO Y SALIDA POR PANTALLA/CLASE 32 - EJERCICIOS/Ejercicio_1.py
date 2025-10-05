'''Ejercicio 1
Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas'''

vocalMinuscula = input('Escriba una letra vocal en minuscual: ')
while(vocalMinuscula != 'a' and vocalMinuscula != 'e' and vocalMinuscula != 'i' and vocalMinuscula != 'o' and vocalMinuscula != 'u'):
    vocalMinuscula = input('No es una vocal en minuscual digite nuevamente: ')

letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letraMayuscula = input('Escriba una letra en mayuscula: ')
while(letraMayuscula not in letras):
    letraMayuscula = input('Lo digitado no es una letra en mayuscula: ')

print(vocalMinuscula.upper()+letraMayuscula.lower())


