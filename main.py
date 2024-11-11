import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Función para generar los datos del sistema
def generar_datos(num_symbols, mod_order):
    data = np.random.randint(0, mod_order, num_symbols)
    return data

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

# Función para demodular la señal recibida
def demodular_datos(received_signal, mod_order):
    constellation_points = np.array([complex(i, j) for i in range(-3, 4, 2) for j in range(-3, 4, 2)])
    demodulated_data = np.array([np.argmin(np.abs(received_signal[i] - constellation_points)) for i in range(len(received_signal))])
    return demodulated_data

# Función para visualizar las gráficas
def visualizar_graficas(symbols, received_signal, snr_db_range):
    # Graficar la constelación transmitida y recibida
    plt.figure(figsize=(10, 6))
    plt.scatter(symbols.real, symbols.imag, color='red', label='Transmitido')
    plt.scatter(received_signal.real, received_signal.imag, color='blue', alpha=0.5, label='Recibido con Ruido')
    plt.title('Constelación 16-QAM')
    plt.xlabel('In-Phase')
    plt.ylabel('Quadrature')
    plt.legend()
    plt.grid()
    plt.show()

    # Graficar la tasa de error de bits (BER) en función de SNR
    ber_values = []
    for snr_db in snr_db_range:
        received_signal = agregar_ruido(symbols, snr_db)
        demodulated_data = demodular_datos(received_signal, 16)
        ber = np.sum(symbols != received_signal) / len(symbols)
        ber_values.append(ber)
    
    plt.figure(figsize=(10, 6))
    plt.semilogy(snr_db_range, ber_values, marker='o')
    plt.title('Tasa de Error de Bits (BER) vs SNR')
    plt.xlabel('SNR (dB)')
    plt.ylabel('BER')
    plt.grid(True)
    plt.show()

# Main: Ejecutar todo el proceso
def main():
    num_symbols = 1000  # Número de símbolos a transmitir
    mod_order = 16      # Orden de QAM (16-QAM)
    snr_db_range = np.arange(10, 40, 2)  # Rango de SNR más alto, de 10 a 40 dB

    # Generar los datos
    data = generar_datos(num_symbols, mod_order)

    # Modular los datos
    symbols = modular_datos(data, mod_order)

    # Agregar ruido al canal
    received_signal = agregar_ruido(symbols, snr_db_range[0])  # Usar el SNR más bajo de la simulación

    # Visualizar gráficas
    visualizar_graficas(symbols, received_signal, snr_db_range)

# Ejecutar la simulación
if __name__ == "__main__":
    main()
