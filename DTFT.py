import matplotlib.pyplot as plt
import numpy as np

w=np.arange(-np.pi,np.pi,0.01*np.pi);
size=int(input("Enter the size of sequence :"))
x=[]
for i in range(0,size+1):
	key=int(input("Enter the element:"))
	x.append(key)
y=[]
j=(-1)**0.5
for i in w:
	sum1=0
	for n in range (0,len(x)):
		sum1=sum1+x[n]*np.exp(-1*j*i*n)
	y.append(sum1)
plt.subplot(311);
plt.stem(w,np.abs(y));
plt.subplot(312);
plt.stem(w,np.angle(y));
plt.show()
