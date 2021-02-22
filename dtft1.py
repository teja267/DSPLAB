from matplotlib import pyplot as plt 
import numpy as np

w=np.arange(-np.pi,np.pi,0.01*np.pi);
m=np.arange(0,500)
Fs=300
F=100

x=np.cos(2*np.pi*F/Fs*m)
y=[]
j=(-1)**0.5
for i in w:
	sum1=0
	for n in range (0,len(x)):
		sum1=sum1+x[n]*np.exp(-1*j*i*n)
	y.append(sum1)

plt.subplot(311)
plt.stem(np.abs(x));
plt.subplot(312);
plt.stem(w,np.abs(y));
plt.subplot(313);
plt.stem(w,np.angle(y));
plt.show()
