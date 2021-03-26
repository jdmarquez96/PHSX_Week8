import numpy as np
import matplotlib.pyplot as plt

Nmeas = 1
Nexp = 1000

muexp = 0
mutrue = 0
mutruelist = []
mubest = 0
mubestlist=[]
sigma = 5



for i in range(-100, 100):
	mutrue = i/10
	for j in range(0, Nexp):
		for h in range(0, Nmeas):
			mutruelist.append(mutrue)
			x = np.random.normal(mutrue, sigma)
			mubest = x
			mubest1 = mubest/Nmeas
			mubestlist.append(mubest1)



plt.figure()
plt.hist2d(mutruelist,mubestlist, bins = (50,50), cmap = plt.cm.jet)
plt.xlabel("$\mu_{true}$")
plt.ylabel("$\mu_{best}$")
plt.savefig("neymanconstruction.png")
plt.show()
print(len(mutruelist),len(mubestlist))
