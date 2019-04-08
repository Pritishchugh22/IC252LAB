import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
A={0,1}
B=[]
for i in range(10000):
    B.append(random.randint(0,1))
C=[]
for i in range(10000):
    if(B[i]==0):
        x=random.random()
        if(x>=0 and x<=0.75):
            C.append(0)
        else:
            C.append(1)
    if(B[i]==1):
        x=random.random()
        if(x>=0 and x<=0.35):
            C.append(0)
        else:
            C.append(1)
p00=0
p01=0
p10=0
p11=0
for i in range(10000):
    if(B[i]==0 and C[i]==0):
        p00=p00+1
    if(B[i]==0 and C[i]==1):
        p10=p10+1
    if(B[i]==1 and C[i]==0):
        p01=p01+1
    if(B[i]==1 and C[i]==1):
        p11=p11+1
p00=p00/10000
p01=p01/10000
p10=p10/10000
p11=p11/10000
print(p00,p01,p10,p11)
print(0.75/2,0.35/2,0.25/2,0.65/2)
ax=plt.axes(projection='3d') 

ax.scatter3D([0,0,1,1],[0,1,0,1],[0.375,0.125,0.175,0.325])

ax.plot3D([0]*100,[0]*100,np.linspace(0,0.375,100),color='b')

ax.plot3D([0]*100,[1]*100,np.linspace(0,0.125,100),color='b')

ax.plot3D([1]*100,[0]*100,np.linspace(0,0.175,100),color='b') 

ax.plot3D([1]*100,[1]*100,np.linspace(0,0.325,100),color='b') 

ax.set_xlabel('x-axis')
