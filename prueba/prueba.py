import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Función para generar los datos del sistema (bits)
def generar_datos(num_symbols, num_bits_per_symbol):
    # Genera los bits aleatorios para cada símbolo
    data = np.random.randint(0, 2, (num_symbols, num_bits_per_symbol))
    return data

# Función para mapear los bits a la constelación 16QAM
def modulación_16QAM(bits):
    # Niveles de amplitud para los ejes I y Q (4 niveles en cada eje)
    I = np.array([-3, -1, 1, 3])  # Niveles de amplitud en el eje I
    Q = np.array([-3, -1, 1, 3])  # Niveles de amplitud en el eje Q
    
    # Convertir los bits en un número decimal (de 0 a 15)
    # Los bits se agrupan de 4 en 4 para formar un número de 4 bits
    decimal_symbols = []
    for bit in bits:
        decimal_symbol = bit[0] * 8 + bit[1] * 4 + bit[2] * 2 + bit[3]  # Convertir 4 bits a decimal
        decimal_symbols.append(decimal_symbol)

    # Crear la constelación 16QAM (combinación de niveles de I y Q)
    constellation = np.array([complex(i, q) for i in I for q in Q])

    # Mapear los números decimales a los puntos de la constelación
    modulated_signal = constellation[decimal_symbols]
    return modulated_signal

# Función para guardar los datos en un archivo CSV
def guardar_datos_csv():
    num_symbols = 1000  # Número de símbolos
    num_bits_per_symbol = 4  # 4 bits por símbolo (para 16-QAM)
    
    # Generar los bits aleatorios (4 bits por símbolo)
    bits = generar_datos(num_symbols, num_bits_per_symbol)

    # Modulación 16QAM
    modulated_signal = modulación_16QAM(bits)

    # Guardar los datos de la señal modulada en un archivo CSV
    df = pd.DataFrame({"Real": np.real(modulated_signal), "Imag": np.imag(modulated_signal)})
    df.to_csv("datos_modulados_16qam.csv", index=False)
    print("Datos modulados guardados en datos_modulados_16qam.csv")

    # Graficar la constelación
    plt.figure(figsize=(6, 6))
    plt.scatter(np.real(modulated_signal), np.imag(modulated_signal))
    plt.title('Constelación 16QAM')
    plt.xlabel('Eje I')
    plt.ylabel('Eje Q')
    plt.grid(True)
    plt.show()

# Ejecutar la función para guardar los datos
if __name__ == "__main__":
    guardar_datos_csv()
