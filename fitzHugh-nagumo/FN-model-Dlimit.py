import numpy as np
import pylab as plt
from matplotlib import rc, rcParams
rc('text',usetex=True)
# Change all fonts to 'Computer Modern'
rc('font',**{'family':'serif','serif':['Computer Modern']})

a=1.05
# a=0.99
epsilon=0.01

t_end = 100.0
dt=epsilon/10
spike_times=[]
# for i in range(1000):
i=0
time=0.0
# while time<t_end:
D=1.0
while (D>.1):
    t=[0.0] 
    x=[1.5]
    y=[0.2]
    spike_times=[]
    while len(spike_times)<2:
    # for i in range(1000):
        i=i+1
        time = dt*i
        kesi=np.random.normal(loc = 0.0, scale = 1.0)
        x_temp = x[-1] + dt * ( x[-1] - (x[-1]**3.0/3.0) -y[-1] ) / epsilon
        y_temp = y[-1] + dt * ( x[-1] + a + D * kesi )
        if x_temp*x[-1]<0:
            if x_temp>x[-1]:
                spike_times.append(time)
        x.append(x_temp)
        y.append(y_temp)
        t.append(time)
    print("D:",D)
    print(spike_times)
    D=D-.1


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
# plt.vlines(spike_times,1,2)
# plt.ylabel(r'y', fontsize=17)
# plt.xlabel(r'time',fontsize=17)

# plt.show()

