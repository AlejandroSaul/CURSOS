#Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

letra = input("Ingresa una letra: ")

'''if letra.lower() == "a":
    print("Es una vocal")
else:
    if letra.lower() == "e":
        print("Es una vocal")
    else:
        if letra.lower() == "i":
            print("Es una vocal")
        else:
            if letra.lower() == "o":
                print("Es una vocal")
            else:
                if letra.lower() == "u":
                    print("Es una vocal")
                else:
                    print("NO es una vocal")'''

if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("NO es una vocal")