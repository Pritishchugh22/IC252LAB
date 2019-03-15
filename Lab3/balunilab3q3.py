
#%%
#import libraries
import numpy as np,matplotlib.pyplot as plt
ss=[]
number=list(np.arange(1,367,1))
#repeat 366 times
for n in range(1,367):
    #Generating n(number of people) random integers in [1,366]
    birthday=list(np.random.randint(1,366,n))
    #apply algorithm
    #take elements from set of birthday..
    #calculate no. of time it repeats..
    #subtract -1
    #multiply with string
    #filter None
    #calculate length
    #append it in list ss
    a=["$"*(birthday.count(s)-1) for s in set(birthday)]
    b=list(filter(None,a))
    ss.append(len(b))
#plot graph
plt.plot((number),(ss))
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt
ss=[]
number=list(np.arange(1,367,1))
for n in range(1,367):
    birthday=[]
    #create random list as required proabilities.
    for i in range(n):
        x=np.random.uniform(0,1)
        if x<2/3:
            birthday.append(np.random.randint(1,151))
        else:
            birthday.append(np.random.randint(151,366))
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
#%%%
import numpy as np,matplotlib.pyplot as plt
ss=[]
number=list(np.arange(1,688,1))
#repeat 366 times
for n in range(1,688):
    #Generating n(number of people) random integers in [1,366]
    birthday=list(np.random.randint(1,366,n))
    #apply algorithm
    #take elements from set of birthday..
    #calculate no. of time it repeats..
    #subtract -1
    #multiply with string
    #filter None
    #calculate length
    #append it in list ss
    a=["$"*(birthday.count(s)-1) for s in set(birthday)]
    b=list(filter(None,a))
    ss.append(len(b))
#plot graph
plt.plot((number),(ss))
plt.show()


