import scipy.io
from matplotlib import pyplot as plt
from scipy.io import wavfile
import numpy as np
import sounddevice as sd
t=3
fs=8000
m=sd.rec(int(t*fs),fs,dtype='float32',channels=1)
sd.wait()
n=np.max(m)*np.random.rand(len(m),1)
y=m+(n)
z=np.zeros(len(y))
for i in range(0,len(y)-10):
	s=np.sum(y[i:i+10])
	z[i]=s/10.0
wavfile.write('original.wav',fs,m)
wavfile.write('noised.wav',fs,y)
wavfile.write('processed.wav',fs,z)
m=m[11200:12400]
y=y[11200:12400]
n=n[11200:12400]
z=z[11200:12400]
plt.subplot(2,2,1)
plt.plot(m)
plt.subplot(2,2,2)
plt.plot(n)
plt.subplot(2,2,3)
plt.plot(y)
plt.subplot(2,2,4)
plt.plot(z)
plt.show()
