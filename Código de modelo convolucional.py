import numpy as np
import matplotlib.pyplot as plt

def convoluted_model():

    # Setting parameters
    depth = [0, 10, 30, 50]  
    speed = [1500, 2000, 2500] 
    density = [1.8, 2.0, 2.2] 

    # Computing the impedance
    impedance = [vel * dens for vel, dens in zip(speed, density)]

    # Computing the reflexivity
    reflexivity= [(impedance[i+1] - impedance[i]) / (impedance[i+1] + impedance[i])
                      for i in range(len(impedance) - 1)]

    # Defining the Ricker Wavelet

    def wavelet_ricker(f, dt, length):
        t = np.arange(-length / 2, length / 2, dt)
        ricker = (1 - 2 * (np.pi ** 2) * (f ** 2) * (t ** 2)) * np.exp(-(np.pi ** 2) * (f ** 2) * (t ** 2))
        return t, ricker

    f_central = 25  # Frequency
    dt = 0.001  # Intervals
    length = 0.4  # Wavelet duration
    t_wavelet, wavelet = wavelet_ricker(f_central, dt, length)

    # Computing the convolution
    reflexivity_series = np.zeros(100)
    reflexivity_series[10] = reflexivity[0]  # reflexivity related to the first interface
    reflexivity_series[30] = reflexivity[1]  # reflexivity related to the second interface
    convoluted_signal = np.convolve(reflexivity_series, wavelet, mode='same')

    # Speed Plot
    plt.figure(figsize=(8, 4))
    plt.step(depth[:-1], speed, where='post', label='Velocidade')
    plt.title('Speed Model')
    plt.xlabel('Depth (m)')
    plt.ylabel('Speed (m/s)')
    plt.grid()
    plt.show()

    # Density Plot
    plt.figure(figsize=(8, 4))
    plt.step(depth[:-1], density, where='post', label='Densidade', color='orange')
    plt.title('Density Model')
    plt.xlabel('Depth (m)')
    plt.ylabel('Density (g/cm³)')
    plt.grid()
    plt.show()

    # Impedance Plot
    plt.figure(figsize=(8, 4))
    plt.step(depth[:-1], impedance, where='post', label='Impedância', color='green')
    plt.title('Impedance')
    plt.xlabel('Depth (m)')
    plt.ylabel('Impedance')
    plt.grid()
    plt.show()

    # Reflexivity Plot
    plt.figure(figsize=(8, 4))
    plt.stem(range(len(reflexivity_series)), reflexivity_series, linefmt='red', markerfmt='ro', basefmt='k')
    plt.title('Reflexivity coeficients')
    plt.xlabel('Samples')
    plt.ylabel('Reflexivity')
    plt.grid()
    plt.show()

    # Convoluted Signal
    plt.figure(figsize=(8, 4))
    plt.plot(convoluted_signal, label='Seismic Signal')
    plt.title('Convoluted Signal')
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

convoluted_model()
