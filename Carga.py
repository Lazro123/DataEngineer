import pandas as pd
import json

# Cargar los archivos CSV y JSON en DataFrames y diccionarios, respectivamente
df = pd.read_csv('instituciones_educativas.csv',on_bad_lines='skip')
with open('universidades.json', 'r') as f:
    universidades = json.load(f)

# Crear un diccionario para almacenar las universidades homologadas
homologadas = {}

# Recorrer cada fila del DataFrame
for index, row in df.iterrows():
    # Convertir el nombre de la universidad a minúsculas y eliminar espacios en blanco
    universidades = row['universidad'].lower().strip()
    
    # Buscar la universidad en el diccionario de universidades
    for u in universidades:
        # Recorrer los sinónimos de cada universidad
        for sinonimo in u['sinonimos']:
            # Si se encuentra un sinónimo que coincide con el nombre de la universidad, homologarla
            if sinonimo.lower().strip() == universidad:
                homologadas[row['candidateld']] = {
                    'value': row['value'],
                    'universidad_homologada': u['nombre_universidad']
                }
    
    # Si no se encontró ninguna universidad homologada, agregar la original al diccionario
    if row['candidateld'] not in homologadas:
        homologadas[row['candidateld']] = {
            'value': row['value'],
            'universidad_homologada': universidad
        }

# Convertir el diccionario de universidades homologadas en un DataFrame y guardarlo en un archivo CSV
homologadas_df = pd.DataFrame.from_dict(homologadas, orient='index', columns=['value', 'universidad_homologada'])
homologadas_df.to_csv('universidades_homologadas.csv')

# Crear un diccionario para almacenar los sinónimos de cada universidad homologada
sinonimos = {}

# Recorrer cada universidad del diccionario de universidades
for u in universidades:
    # Agregar la universidad como clave en el diccionario de sinónimos
    sinonimos[u['nombre_universidad']] = {
        'sinonimos': u['sinonimos']
    }
    
# Convertir el diccionario de sinónimos en un archivo JSON y guardarlo en un archivo
with open('sinonimo_universidades.json', 'w') as f:
    json.dump(sinonimos, f)