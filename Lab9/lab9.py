import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
sample=[np.sum(np.random.poisson(5,100)) for i in range(1000)]
sample2=[(i-100*5)/(10/np.sqrt(5)) for i in sample ]
sample3=[i/100 for i in sample]

E_X_bar=mu=np.mean(sample3)
E_X=5
Std_X_bar=sigma=np.std(sample3)
Std_X=1/np.sqrt(5)

print('E_X_bar ==>',E_X_bar)
print('E_X ==>',5)
print('-------------'*5)
print('Std_X_bar ==>',Std_X_bar)
print('Std_X ==>',np.sqrt(3)/10)
plt.hist(sample2,normed=True,ec='b')
plt.title('Yn of Poisson Distribution Converge to Gaussian Distribution',fontweight='bold')
plt.show()

#%%

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
sample=[np.sum(np.random.uniform(0,1,100)) for i in range(1000)]
sample2=[(i-100*0.5)/(10/np.sqrt(12)) for i in sample ]
sample3=[i/100 for i in sample]

E_X_bar=mu=np.mean(sample3)
E_X=0.5
Std_X_bar=sigma=np.std(sample3)
Std_X=1/12

print('E_X_bar ==>',E_X_bar)
print('E_X ==>',0.5)
print('-------------'*5)
print('Std_X_bar ==>',Std_X_bar)
print('Std_X ==>',1/np.sqrt(12))
plt.hist(sample2,normed=True,ec='b')
plt.title('Yn of Uniform Distribution Converge to Gaussian Distribution',fontweight='bold')


plt.show()


#%%
import numpy as np
import matplotlib.pyplot as plt

sample=[np.sum(np.random.exponential(1/3,100)) for i in range(1000)]
sample2=[(i-100*0.33)/(10/3) for i in sample ]
sample3=[i/100 for i in sample]

E_X_bar=np.mean(sample3)
E_X=1/3
Std_X_bar=np.std(sample3)
Std_X=1/3

print('E_X_bar ==>',E_X_bar)
print('E_X ==>',1/3)
print('-------------'*5)
print('Std_X_bar ==>',Std_X_bar)
print('Std_X ==>',1/3)
plt.hist(sample2,normed=True,ec='b')
plt.title('Yn of Exponential Distribution Converge to Gaussian Distribution',fontweight='bold')
plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt

sample=[np.sum(np.random.binomial(10,0.3,100)) for i in range(1000)]
sample2=[(i-100*3)/(10*np.sqrt(10*.3*.7)) for i in sample ]
sample3=[i/100 for i in sample]

E_X_bar=np.mean(sample3)
E_X=3
Std_X_bar=np.std(sample3)
Std_X=2.1

print('E_X_bar ==>',E_X_bar)
print('E_X ==>',3)
print('-------------'*5)
print('Std_X_bar ==>',Std_X_bar)
print('Std_X ==>',2.1)
plt.hist(sample2,normed=True,ec='b')
plt.title('Yn of Binomial Distribution Converge to Gaussian Distribution',fontweight='bold')
plt.show()
#%%
