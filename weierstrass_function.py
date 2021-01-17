import numpy as np
import matplotlib.pyplot as plt

def f(x,a,b,n):
	fx = 0
	for i in range(n):
		fx = fx + (a**i)*np.cos((b**i)*np.pi*x)
	return fx

X = np.linspace(-2,2,1000)
a = 0.5
b = 5
n = 100
y = []
for x in X:
	y.append(f(x,a,b,n))
	
plt.plot(X,y)
plt.show()
