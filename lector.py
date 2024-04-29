import pandas as pd

# Intentar leer el archivo CSV
try:
    data_frame = pd.read_csv("horas2.csv")
except FileNotFoundError:
    print("Error: El archivo 'horas1.csv' no se encontró en el directorio actual.")
    exit()

def analisis_estadistico(df):
    # Asegurar que la columna 'fi' existe
    if 'fi' in df.columns:
        df["Fi"] = df["fi"].cumsum()
        df["ri"] = df["fi"] / df["fi"].sum()
        df["Ri"] = df["ri"].cumsum()
        df["pi%"] = df["ri"] * 100
        df["Pi%"] = df["Ri"] * 100
    else:
        available_columns = ', '.join(df.columns)
        print(f"La columna 'fi' no existe en el DataFrame. Columnas disponibles: {available_columns}")
    return df

# Llamar a la función de análisis estadístico y guardar el resultado
data_frame = analisis_estadistico(data_frame)
data_frame.to_clipboard(index=False)

# Imprimir el DataFrame modificado
print(data_frame)
