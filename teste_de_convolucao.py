import numpy as np
import matplotlib.pyplot as plt

def wavelet_ricker(t, f):
    
    # ricker = (1-2*(np.pi*f*t**2))*(np.exp-(np.pi*f*t**2))
    aux=(np.pi*f*t)*(np.pi*f*t)
    ricker = (1-2*aux)*np.exp(-aux)
    return ricker

#nt = espaço de tempo 
#dt = taxa de amostragens
dt= 0.0001 # ll
nt = 1001
t= np.linspace(0, nt*dt, nt, endpoint=False)

#wavelet para cada espaço de tempo
w= wavelet_ricker(t-0.03, 60)

plt.figure
plt.plot(t,w,'--.')
plt.show()

vel = np.zeros(nt)
vel[0:nt//3]=1500
vel[nt//3:2*nt//3]=2000
vel[2*nt//3:]=2500

plt.figure()
plt.plot(t,vel,'--')
plt.show()
reflec=np.zeros(nt)
reflec[500]=-1
reflec[900]=1

plt.figure()
plt.plot(t,reflec,'--')
plt.show()

trace= np.convolve(reflec,w,mode="same")

plt.figure()
plt.plot(t,trace,'--')
plt.show()


