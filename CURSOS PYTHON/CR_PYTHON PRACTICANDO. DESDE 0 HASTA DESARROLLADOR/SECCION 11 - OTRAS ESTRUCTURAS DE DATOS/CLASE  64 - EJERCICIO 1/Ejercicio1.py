#En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

#{"Guatemala": "Ciudad de Guatemala", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

diccionario = {"Guatemala": "Ciudad de Guatemala", "Honduras": "Tegucigalpa","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid" , "El Salvador" : "San Salvador"}

pais = input('Ingrese un pais para conocer su capital: ')
letra = pais.title() in diccionario

if letra:
    print(diccionario[pais.title()])
else:
    print("El pais no se encuentra en el diccionario")