import numpy as np
import pandas as pd

# Función para generar los datos del sistema (bits aleatorios)
def generar_datos(num_symbols, num_bits_per_symbol):
    # Genera los bits aleatorios para cada símbolo
    data = np.random.randint(0, 2, (num_symbols, num_bits_per_symbol))
    return data

def guardar_datos_csv():
    num_symbols = 1000  # Número de símbolos
    num_bits_per_symbol = 4  # 16-QAM tiene 4 bits por símbolo

    # Generar datos aleatorios (bits)
    data = generar_datos(num_symbols, num_bits_per_symbol)

    # Guardar los datos en un archivo CSV
    df = pd.DataFrame(data, columns=[f"Bit{i+1}" for i in range(num_bits_per_symbol)])
    df.to_csv("datos_entrada.csv", index=False)
    print("Datos guardados en datos_entrada.csv")

# Ejecutar la función para guardar los datos
if __name__ == "__main__":
    guardar_datos_csv()
