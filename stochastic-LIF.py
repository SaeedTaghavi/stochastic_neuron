import numpy as np
import matplotlib.pyplot as plt
tau_m =10.0     #ms
Rm = 10.0       #Mohm
Vth = -50.0     #mV
EL=Vr=-65.0     #mV

# tau_m * dV/dt = EL - V + Rm * Ie

t=[0.0]
V=[-65.0]
spike_times=[]
dt = 0.1
# for i in range(1000):
i=0
Ie=[0.0]
while len(spike_times)<1000:
# for i in range(10000):
    i=i+1
    time = dt*i
    # Ie=1.5 is thereshold of spiking 
    # with Ie<= 1.5 the neuron will never spikes
    mu = 1.50
    sigma=2.1
    kesi=np.random.normal(loc = 0.0, scale = 1.0)
    Ie.append(mu+sigma*kesi)
    v= V[-1] + dt * (EL-V[-1]+Rm*Ie[-1])/tau_m
    if v>Vth:
        v=Vr
        spike_times.append(time)
    V.append(v)
    t.append(time)
# plt.plot(t,V)
# plt.vlines(spike_times,0,1)
# plt.plot(t,Ie)
# plt.show()

# print(len(spike_times))
# print("len I:",len(Ie))
# print("len time:",len(t))

number_of_spikes=len(spike_times)
isi= np.zeros(number_of_spikes-1)
for i in range(number_of_spikes-1):
    isi[i]=spike_times[i+1]-spike_times[i]

FF_isi=np.var(isi)/np.mean(isi)
# The variance is the square of the standard deviation
print(FF_isi)




