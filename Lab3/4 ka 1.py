#import libraries
import numpy as np,matplotlib.pyplot as plt
ss=[]
number=list(np.arange(1,367,1))
#repeat 366 times
for n in range(1,367):
    birthday=list(np.random.randint(1,366,n))
    #apply algorithm
    #take elements from set of birthday..
    #calculate no. of time it repeats..
    #subtract -1
    #multiply with string
    #filter None
    #calculate length
    #append it in list ss
    a=["a"*(birthday.count(s)-1) for s in set(birthday)]
    b=list(filter(None,a))
    ss.append(len(b))
#plot graph
plt.plot((number),(ss))
plt.show()



