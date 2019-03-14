import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

ntrials = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]


def computeProb(n):
    df = pd.DataFrame(columns = ['T', 'C'])
    df.T = np.random.randint(1,7,n, dtype=np.int64)
    df.C = np.random.randint(1,7,n, dtype=np.int64)
    nr = df['C'][df['C'] + df['T'] >= 9][df['T'] >= 4].count()
    dr = df['C'][df['C'] + df['T'] >= 9].count()
    return nr / dr

lst = []
for n in ntrials:
    lst.append(computeProb(n))
scaleddowntrials=list(map(math.log10,ntrials))
print('-----------------------------')
print('Hand Calculated Value is 0.9')
print('------------------------------')
plt.plot(scaleddowntrials,lst)
plt.grid()
plt.xlabel('log(numberoftrials) ==>')
plt.ylabel('Cond. Probab. for particular number of trials==>')
plt.axhline(0.9,linestyle='dashed',alpha=0.5)
plt.text(3.3, 0.9, '0.9', fontsize=10, va='center', ha='center')
plt.title('Experiment',fontsize=20)