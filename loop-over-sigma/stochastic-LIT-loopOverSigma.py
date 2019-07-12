import numpy as np
import pylab as plt
from matplotlib import rc, rcParams
rc('text',usetex=True)
# Change all fonts to 'Computer Modern'
rc('font',**{'family':'serif','serif':['Computer Modern']})

tau_m =10.0     #ms
Rm = 10.0       #Mohm
Vth = -50.0     #mV
EL=Vr=-65.0     #mV

# tau_m * dV/dt = EL - V + Rm * Ie


sigma_array = np.linspace(0.01,3.0,10)
FF_isi=[]
CV_isi=[]
for sigma in sigma_array:
    t=[0.0]
    V=[-65.0]
    spike_times=[]
    dt = 0.1
    # for i in range(1000):
    i=0
    Ie=[0.0]
    while len(spike_times)<501:
    # for i in range(10000):
        i=i+1
        time = dt*i
        # Ie=1.5 is thereshold of spiking 
        # with Ie<= 1.5 the neuron will never spikes
        mu = 1.50
        # sigma=.1
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

    
    # a dimensionless measure of spike train variability is the coefficient of variation (CV)
    # defined as the ratio of ISIs standard deviation to the mean ISI
    # CV = sqrt( <T^2> - <T>^2)/<T>
    # # The variance is the square of the standard deviation, sigma^2 = var[X] = E[X^2]-E[X]^2
    number_of_spikes=len(spike_times)
    isi= np.zeros(number_of_spikes-1)
    for i in range(number_of_spikes-1):
        isi[i]=spike_times[i+1]-spike_times[i]

    FanoFactor=np.var(isi)/np.mean(isi)
    coefficient_of_variation=np.sqrt(np.var(isi))/np.mean(isi)
    FF_isi.append(FanoFactor)
    CV_isi.append(coefficient_of_variation)
    
    # print(FF_isi)

# plt.plot(sigma_array,FF_isi)
plt.loglog(sigma_array,FF_isi)
plt.title(r'stochastic LIF neuron', fontsize=18)
plt.xlabel(r'$\sigma $',fontsize=17)
plt.ylabel(r'Fano Factor', fontsize=17)
plt.savefig('log-log.png')
plt.show()

plt.plot(sigma_array,CV_isi)
plt.title(r'stochastic LIF neuron', fontsize=18)
plt.xlabel(r'$\sigma $',fontsize=17)
plt.ylabel(r'coefficient of variation (CV)', fontsize=17)
plt.savefig('CV.png')



