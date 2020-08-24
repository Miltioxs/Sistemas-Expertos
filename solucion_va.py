
import pandas as pd

#Leo toda la data proporcionada
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

#Calculo de la mediana de la propiedad
mediana_alcohol = df.alcohol.median()
mediana_pH = df.pH.median()
mediana_azucarResidual = df.residual_sugar.median()
mediana_acidoCitrico = df.citric_acid.median()

def nivel(mediana_propiedad, columna_propiedad): 
    for i, propiedad in enumerate(columna_propiedad):
        if propiedad >= mediana_propiedad:
            df.loc[i, propiedad] = 'alto'
        else:
            df.loc[i, propiedad] = 'bajo'
    resultado = df.groupby(propiedad).quality.mean()
    return print(resultado)

#mandamos los datos de las propiedades a la funcion nivel        
alcohol = nivel(mediana_alcohol, df.alcohol)
ph = nivel(mediana_pH, df.pH)
azucar_residual =  nivel(mediana_azucarResidual, df.residual_sugar) 
acido_citrico = nivel(mediana_acidoCitrico,  df.citric_acid) 



  
    
    






