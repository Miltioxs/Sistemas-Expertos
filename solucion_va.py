#Refactorizacion por Milton Mejia
import pandas as pd

#Leo toda la data proporcionada
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

#Calculo de la mediana de la propiedad
mediana_alcohol = df.alcohol.median()
mediana_pH = df.pH.median()
mediana_azucarResidual = df.residual_sugar.median()
mediana_acidoCitrico = df.citric_acid.median()



def nivel_propiedad(mediana_propiedad, columna_propiedad, nombre_columna): 
    for i, propiedad_vino in enumerate(columna_propiedad):
        if propiedad_vino >= mediana_propiedad:
            df.loc[i, nombre_columna] = 'alto'
        else:
            df.loc[i, nombre_columna] = 'bajo'
    return print(df.groupby(nombre_columna).quality.mean())
    

#Mandamos los datos de las propiedades a la funcion nivel_propiedad       
alcohol = nivel_propiedad(mediana_alcohol, df.alcohol, 'alcohol')
ph = nivel_propiedad(mediana_pH, df.pH, 'pH')
azucar_residual =  nivel_propiedad(mediana_azucarResidual, df.residual_sugar,
'residual_sugar') 
acido_citrico = nivel_propiedad(mediana_acidoCitrico,  df.citric_acid, 'citric_acid')
    






