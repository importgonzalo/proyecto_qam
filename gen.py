# generar_datos_csv.py
import numpy as np
import pandas as pd

# Función para generar los datos del sistema
def generar_datos(num_symbols, mod_order):
    data = np.random.randint(0, mod_order, num_symbols)
    return data

def guardar_datos_csv():
    num_symbols = 1000  # Número de símbolos
    mod_order = 16      # Orden de QAM (16-QAM)

    # Generar datos aleatorios
    data = generar_datos(num_symbols, mod_order)

    # Guardar los datos en un archivo CSV
    df = pd.DataFrame(data, columns=["Datos"])
    df.to_csv("datos_entrada.csv", index=False)
    print("Datos guardados en datos_entrada.csv")

# Ejecutar la función para guardar los datos
if __name__ == "__main__":
    guardar_datos_csv()
