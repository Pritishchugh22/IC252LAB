import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

norm = scipy.stats.norm(0, 1).pdf
cdf = scipy.stats.norm(0, 1).cdf

ppf = scipy.stats.norm.ppf

a = int(input())
b = int(input())
n = int(input())

def area(a, b):
    random_points = [(np.random.uniform(a, b), np.random.uniform(0, norm(0))) for i in range(n)]
    under_fx = [i for i in random_points if i[1] <= norm(i[0])]
    return len(under_fx) / len(random_points) * (b - a) * norm(0)


U = np.random.uniform(0, 1, 1000)
U = [round(u, 3) for u in U]
#X = [ppf(u) for u in U]

N = np.linspace(-3, 3, 1000)
dct = {}
for i in N:
    dct[round(0.5 + area(0, i), 3)] = i

X = []
for u in U:
    try:
        X.append(dct[u])
    except:
        pass


plt.hist(X)
