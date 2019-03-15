#import libraries...
import numpy as np,pandas as pd,matplotlib.pyplot as plt
ss=[]
number=list(np.arange(1,688,1))# list of (1,687)
for n in range(1,688):
    birthday=list(np.random.randint(1,688,n))
    #applying algorithm to get c ...
     #take elements from set of birthday..
    #calculate no. of time it repeats..
    #subtract -1
    #multiply with string
    #filter None
    #calculate length
    #append it in list ss
    a=["a"*(birthday.count(s)-1) for s in set(birthday)]
    b=list(filter(None,a))
    #append value of c in new list a...
    ss.append(len(b))
#plot graph...
plt.plot((number),(ss))
plt.show()