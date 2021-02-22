# DTFT implementation
import numpy as np
from matplotlib import pyplot as plt
x=[1,2,3,-1,4]
y=[]
w=np.arange(-1*np.pi,np.pi,0.01*np.pi)
for i in range(0,len(w)):
	s=0
	for n in range(0,len(x)):
		s=s+x[n]*np.exp(-1*1j*w[i]*n)
	y.append(s)
plt.subplot(211)
plt.stem(w,np.abs(y))
plt.subplot(212)
plt.stem(w,np.angle(y))
plt.show()
