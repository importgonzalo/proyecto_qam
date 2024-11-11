# demod.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Función para leer los datos modulados desde CSV
def leer_datos_modulados():
    df = pd.read_csv("datos_modulados.csv")
    return df["Real"].values + 1j * df["Imag"].values

# Función para demodular la señal recibida
def demodular_datos(received_signal, mod_order):
    constellation_points = np.array([complex(i, j) for i in range(-3, 4, 2) for j in range(-3, 4, 2)])
    demodulated_data = np.array([np.argmin(np.abs(received_signal[i] - constellation_points)) for i in range(len(received_signal))])
    return demodulated_data

# Función para graficar la constelación demodulada
def graficar_constelacion_demodulada(received_signal):
    plt.figure(figsize=(10, 6))
    plt.scatter(received_signal.real, received_signal.imag, color='green', label='Señal Demodulada')
    plt.title('Constelación Demodulada')
    plt.xlabel('In-Phase')
    plt.ylabel('Quadrature')
    plt.legend()
    plt.grid()
    plt.show()

# Función principal
def main():
    mod_order = 16

    # Leer los datos modulados desde el CSV
    received_signal = leer_datos_modulados()

    # Demodular los datos
    demodulated_data = demodular_datos(received_signal, mod_order)

    # Graficar la constelación de la señal demodulada
    graficar_constelacion_demodulada(received_signal)

if __name__ == "__main__":
    main()