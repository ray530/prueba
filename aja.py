import numpy as np
import matplotlib.pyplot as plt

c=np.linspace(-40,100,20)

def farh(x):
	f=1.8*x+32
	return f

fh=farh(c)

plt.plot(c,fh)
plt.show()

