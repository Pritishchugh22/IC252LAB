import random
import matplotlib.pyplot as plt
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
print("P(Y=0)",C.count(0)/10000)
print("P(Y=1)",C.count(1)/10000)
print(0.75/2+0.35/2)
print(0.25/2+0.65/2)
plt.scatter([0,1],[C.count(0)/10000,C.count(1)/10000])
plt.show()
            
    
