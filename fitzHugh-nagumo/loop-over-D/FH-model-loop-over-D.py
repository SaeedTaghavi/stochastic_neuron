import numpy as np
import pylab as plt
from matplotlib import rc, rcParams
rc('text',usetex=True)
# Change all fonts to 'Computer Modern'
rc('font',**{'family':'serif','serif':['Computer Modern']})

a=1.05
# a=0.99
epsilon=0.01

t_end = 1000.0
dt=epsilon/10
# min D can be .3 but it will took a long time until desired number of spikes
D_array=np.linspace(0.3,1.0,10)
FF_isi=[]
CV_isi=[]
for D in D_array:
    t=[0.0] 
    x=[1.5]
    y=[0.2]
    spike_times=[]
    # for i in range(1000):
    i=0
    time=0.0
    # while time<t_end:
    number_of_spikes=1000
    while len(spike_times)<number_of_spikes:
    # for i in range(1000):
        i=i+1
        time = dt*i
        # D = .3
        kesi=np.random.normal(loc = 0.0, scale = 1.0)
        x_temp = x[-1] + dt * ( x[-1] - (x[-1]**3.0/3.0) -y[-1] ) / epsilon
        y_temp = y[-1] + dt * ( x[-1] + a ) +  (D * kesi ) * np.sqrt(dt) #inja sqrt dt ezafe shod
        if x_temp*x[-1]<0:
            if x_temp>x[-1]:
                spike_times.append(time)
        x.append(x_temp)
        y.append(y_temp)
        t.append(time)
    
    isi= np.zeros(number_of_spikes-1)
    for i in range(number_of_spikes-1):
        isi[i]=spike_times[i+1]-spike_times[i]
    FanoFactor=np.var(isi)/np.mean(isi)
    coefficient_of_variation=np.sqrt(np.var(isi))/np.mean(isi)
    FF_isi.append(FanoFactor)
    CV_isi.append(coefficient_of_variation)
    print("D:",D)
    print("time:",t[-1])

plt.figure(1)
plt.title(r'stochastic FitzHugh-Nagumo model ', fontsize=18)
plt.subplot(211)
plt.plot(D_array, FF_isi)
plt.xlabel(r'$D$',fontsize=17)
plt.ylabel(r'Fano Factor', fontsize=17)

plt.subplot(212)
plt.plot(D_array, CV_isi)
plt.ylabel(r'coefficient of variation', fontsize=17)
plt.xlabel(r'$D$',fontsize=17)

plt.savefig('stochastic_FitzHugh-Nagumo_model.png')

plt.figure(2)
plt.title(r'stochastic FitzHugh-Nagumo model ', fontsize=18)
plt.subplot(211)
plt.loglog(D_array, FF_isi)
plt.xlabel(r'$D$',fontsize=17)
plt.ylabel(r'Fano Factor', fontsize=17)

plt.subplot(212)
plt.loglog(D_array, CV_isi)
plt.ylabel(r'coefficient of variation', fontsize=17)
plt.xlabel(r'$D$',fontsize=17)

plt.savefig('loglog-stochastic_FitzHugh-Nagumo_model.png')

plt.show()



#sample plots


# print(t)
# print(x)
# print(y)

# plt.savefig('xt.png')

# plt.figure(1)
# plt.title(r'stochastic FitzHugh-Nagumo model ', fontsize=18)
# plt.subplot(211)
# plt.plot(t, x)
# plt.vlines(spike_times,2,3)
# plt.xlabel(r'time',fontsize=17)
# plt.ylabel(r'x', fontsize=17)

# plt.subplot(212)
# plt.plot(t, y)
# plt.vlines(spike_times,.5,1.5)
# plt.ylabel(r'y', fontsize=17)
# plt.xlabel(r'time',fontsize=17)

# plt.show()

