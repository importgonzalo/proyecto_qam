# modular_graficar.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Función para leer los datos desde el archivo CSV
def leer_datos_csv():
    df = pd.read_csv("datos_entrada.csv")
    return df["Datos"].values

# Función para modular los datos utilizando 16-QAM
def modular_datos(data, mod_order):
    constellation_points = np.array([complex(i, j) for i in range(-3, 4, 2) for j in range(-3, 4, 2)])
    symbols = constellation_points[data]
    return symbols

# Función para simular el canal y agregar ruido AWGN
def agregar_ruido(symbols, snr_db):
    snr_linear = 10 ** (snr_db / 10)
    noise_std = np.sqrt(1 / (2 * snr_linear))
    noise = noise_std * (np.random.randn(len(symbols)) + 1j * np.random.randn(len(symbols)))
    received_signal = symbols + noise
    return received_signal

# Guardar la señal modulada con ruido en un archivo CSV
def guardar_datos_modulados(received_signal):
    df = pd.DataFrame({"Real": received_signal.real, "Imag": received_signal.imag})
    df.to_csv("datos_modulados.csv", index=False)

# Función para graficar la constelación
def graficar_constelacion(symbols, received_signal):
    plt.figure(figsize=(10, 6))
    plt.scatter(symbols.real, symbols.imag, color='red', label='Transmitido')
    plt.scatter(received_signal.real, received_signal.imag, color='blue', alpha=0.5, label='Recibido con Ruido')
    plt.title('Constelación 16-QAM')
    plt.xlabel('In-Phase')
    plt.ylabel('Quadrature')
    plt.legend()
    plt.grid()
    plt.show()

# Función principal
def main():
    data = leer_datos_csv()
    mod_order = 16
    snr_db = 20

    symbols = modular_datos(data, mod_order)
    received_signal = agregar_ruido(symbols, snr_db)

    # Guardar los datos modulados con ruido
    guardar_datos_modulados(received_signal)

    # Graficar las constelaciones transmitida y recibida
    graficar_constelacion(symbols, received_signal)

if __name__ == "__main__":
    main()
