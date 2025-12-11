while True:
    try:
        num1 = int(input("Ingresa un numero: "))
        resultado = 100 / num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre cero ")
    except ValueError:
        print("No es un numero ")
    except KeyboardInterrupt:
        print("has cancelado por error la ejecucion ")
    except:
        print("Error desconocido ")