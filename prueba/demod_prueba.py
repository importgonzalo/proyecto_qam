import numpy as np
import matplotlib.pyplot as plt

# Función para generar la constelación 16-QAM
def constelacion_16QAM():
    # Niveles de amplitud para los ejes I y Q (4 niveles en cada eje)
    I = np.array([-3, -1, 1, 3])  # Niveles de amplitud en el eje I
    Q = np.array([-3, -1, 1, 3])  # Niveles de amplitud en el eje Q
    
    # Crear la constelación 16QAM (combinación de niveles de I y Q)
    constellation = np.array([complex(i, q) for i in I for q in Q])
    return constellation

# Función para agregar ruido AWGN (ruido blanco aditivo gaussiano)
def agregar_ruido(signal, SNR_dB):
    # Calcular la potencia de la señal
    signal_power = np.mean(np.abs(signal) ** 2)
    # Calcular la potencia del ruido usando la SNR (Relación Señal a Ruido)
    noise_power = signal_power / (10 ** (SNR_dB / 10))
    # Generar ruido con distribución normal diferente en cada ejecución
    noise = np.sqrt(noise_power / 2) * (np.random.randn(len(signal)) + 1j * np.random.randn(len(signal)))
    # Señal ruidosa
    noisy_signal = signal + noise
    return noisy_signal

# Función para graficar la constelación 16-QAM con ruido
def graficar_constelacion_ruidosa():
    # Generar la constelación 16QAM
    constellation = constelacion_16QAM()
    
    # Agregar ruido a la constelación (SNR bajo para más dispersión)
    SNR_dB = 10  # Relación Señal a Ruido en dB (puedes ajustarlo a un valor más bajo para más ruido)
    noisy_constellation = agregar_ruido(constellation, SNR_dB)
    
    # Graficar la constelación con ruido
    plt.figure(figsize=(8, 8))
    plt.scatter(np.real(noisy_constellation), np.imag(noisy_constellation), color='red', label='Constelación Ruidosa')
    plt.scatter(np.real(constellation), np.imag(constellation), color='blue', marker='x', label='Constelación Ideal (sin ruido)')
    
    # Agregar detalles al gráfico
    plt.title(f'Constelación 16-QAM con Ruido (SNR = {SNR_dB} dB)')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

# Ejecutar la función para graficar la constelación ruidosa
if __name__ == "__main__":
    graficar_constelacion_ruidosa()
