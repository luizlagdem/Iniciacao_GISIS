import numpy as np
import matplotlib.pyplot as plt

def direct_wave(d, v1):
    return d / v1

def reflected_wave(d, z, v1):
    return np.sqrt(d**2 + 4 * z**2) / v1

def refracted_wave(d, z, v1, v2):
    return (2 * z / np.sqrt(v2**2 - v1**2)) + (d / v2) 

# Set variables
z = 100
v1 = 5e2
v2 = 5e3
d = np.linspace(0, 2000, 500)

# Calcular tempos
dw_time = direct_wave(d, v1)
rfltw_time = reflected_wave(d, z, v1)
rfrtw_time = refracted_wave(d, z, v1, v2)

# Plotting the results 
plt.figure(figsize=(10, 6))
plt.plot(d, dw_time, label="Direct wave", linestyle="-")
plt.plot(d, rfltw_time, label="Reflected wave", linestyle="--")
plt.plot(d, rfrtw_time, label="Refracted wave", linestyle="-.")

# Configurações do gráfico
plt.title("Waves travel time")
plt.xlabel("Distance (m)")
plt.ylabel("Travel time (s)")
plt.gca().invert_yaxis()
plt.legend()
plt.grid()
plt.show()