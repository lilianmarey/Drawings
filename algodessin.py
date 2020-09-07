import numpy as np
from matplotlib import pyplot as plt
from random import random
from time import time

#plt.plot([i for i in range(100)],[np.sin(i*0.1)*(random()**0.09) for i in range(100)],'ro',markersize=20)


def f():
    for i in range(3000):
        plt.plot([random()],[random()],'o',markersize=8*random())
    plt.savefig('image_'+str((time()))+'.pdf',format='pdf')

    #plt.plot()
    
#f()

def rsign():
    if random()>0.5:
        return 1
    else:
        return -1

def g():
    a,b=0.5,0.5
    z=0.01
    for i in range(1000):
        c,d=a+z*rsign()*np.exp(-i*0.0002)*random()**2,b+z*rsign()*np.exp(-i*0.00002)*random()**2
        plt.plot([c],[d],'o',linestyle='dashed',markersize=4*random()/(1+0.0015*i),color=[0.96*np.exp(-i*0.0002)*random()**1,0.01*np.exp(-i*0.0002)*random()**1,0.39*np.exp(-i*0.0002)*random()**1])
        a,b=c,d
    for i in range(1000):
        c,d=a+z*rsign()*np.exp(-i*0.0002)*random()**2,b+z*rsign()*np.exp(-i*0.00002)*random()**2
        plt.plot([c],[d],'o',linestyle='dashed',markersize=4*random()/(1+0.0015*i),color=[0.01*np.exp(-i*0.0002)*random()**1,0.95*np.exp(-i*0.0002)*random()**1,0.39*np.exp(-i*0.0002)*random()**1])
        a,b=c,d
    for i in range(1000):
        c,d=a+z*rsign()*np.exp(-i*0.0002)*random()**2,b+z*rsign()*np.exp(-i*0.00002)*random()**2
        plt.plot([c],[d],'o',linestyle='dashed',markersize=4*random()/(1+0.0015*i),color=[0.5*np.exp(-i*0.0002)*random()**1,0.01*np.exp(-i*0.0002)*random()**1,0.95*np.exp(-i*0.0002)*random()**1])
        a,b=c,d
    plt.savefig('image_'+str((time()))+'.pdf',format='pdf')

    
g()
    