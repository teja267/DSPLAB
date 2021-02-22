# moving average of the system
import numpy as np
from matplotlib import pyplot as plt
m=int(input("enter  the moving average of system : "))
p=np.arange(0,500)
f=250;
fs=10000;
x=2*np.sin(2*np.pi*f/fs*p+np.pi/2)
plt.subplot(211);
plt.plot(p,x)
a=len(x)
y=[]
for n in range(0,a):
	s=0
	for k in range(0,m):
		if((n-k)>=0):
			s=s+x[n-k]
	y[n]=s/m
plt.subplot(212);
plt.plot(n,y[n])
