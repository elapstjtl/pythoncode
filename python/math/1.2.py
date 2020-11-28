import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
 
fig = plt.figure()
ax = Axes3D(fig)
r = np.arange(0,14,0.1)
a = np.arange(0,15,0.1)
r,a = np.meshgrid(r,a)
S =  ((r**2)-a*r)*np.arcsin(a/(2*r)+(7.5-0.5*((r**2)-(a**2)/4)**0.5))*a-(a**2)/2

ax.plot_surface(r,a,S,rstride = 1,cstride = 1)#,cmap="rainbow")
plt.show()
