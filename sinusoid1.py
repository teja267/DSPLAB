# generate two sinusoids and add with different amplitude
import numpy as np
from matplotlib import pyplot as plt
n=np.arange(0,500)
f=250;
fs=10000;
s=0.5*np.sin(2*np.pi*f/fs*n+np.pi/2)
plt.subplot(3,1,1)
plt.stem(n,s);
s1=1.5*np.sin(2*np.pi*f/fs*n+np.pi/2)
plt.subplot(3,1,2)
plt.stem(n,s1);
a=s+s1
plt.subplot(3,1,3)
plt.stem(n,a);
plt.show()
