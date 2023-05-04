import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('instituciones_educativas.csv',on_bad_lines='skip')

# Verificar los nombres de las columnas
print(df.columns)