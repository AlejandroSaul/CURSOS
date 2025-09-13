'''Ejercicio 1
Crea una función llamada ejercicio1, que recibe la ruta donde se encuentra un dataset y devuelve una DataFrame con los datos que hay en el dataset. Para comprobar esta función utiliza el dataset titanic.csv que se incluye en esta actividad.'''
import pandas as pd

def ejercicio1(ruta):
    try:
        df = pd.read_csv(ruta)
        return df
    except Exception as e:
        print("Error al cargar el archivo")
        return None
df = ejercicio1('./titanic.csv')
'''Ejercicio 2
Crea otra función llamada ejercicio2. Esta función recibe un único argumento que es un dataframe. En concreto debe recibir el dataframe que se ha obtenido de leer el dataset titanic.csv. Esta función devolverá otro dataset que incluya únicamente a los pasajeros menores de 35 años y que viajaban en 3ª clase.'''
def ejercicio2(df):
    return df[(df['Age'] < 35) & (df['Pclass'] == 3)]

'''Ejercicio 3
Crea una función llamada ejercicio3, que recibiendo como argumento el dataframe de salida del ejercicio 2, calcule el porcentaje de pasajeros menores de 35 años de 3ª clase que sobrevivieron.'''

def ejercicio3(df):
    
    total_pasajeros = len(df)
    sobrevivientes = df['Survived'].sum()
    porcentaje = (sobrevivientes / total_pasajeros) * 100 if total_pasajeros > 0 else 0
    return porcentaje

'''Ejercicio 4
Implementa una función llamada ejercicio4 que recibiendo el dataframe con los datos del Titanic, devuelva en una tupla el porcentaje de hombres y mujeres que viajaban en el Titanic, redondeados al segundo decimal.'''

def ejercicio4(df):
    
    total_pasajeros = len(df)
    porcentaje_hombres = round((df[df['Sex'] == 'male'].shape[0] / total_pasajeros) * 100, 2)
    porcentaje_mujeres = round((df[df['Sex'] == 'female'].shape[0] / total_pasajeros) * 100, 2)
    return porcentaje_hombres, porcentaje_mujeres
    

'''Ejercicio 5
Implementa una función llamada ejercicio5 que recibiendo el dataframe con los datos del Titanic, devuelva en una lista el número de pasajeros que viajaban en 1ª, 2ª y 3ª clase.'''
def ejercicio5(df):
    pasajeros_por_clase = [df[df['Pclass'] == i].shape[0] for i in range(1, 4)]
    return pasajeros_por_clase


print(len(df))