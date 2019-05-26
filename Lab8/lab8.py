#importing the required libraries
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


norm = scipy.stats.norm(0, 1).pdf #pdf function of Gaussian distribution
cdf = scipy.stats.norm(0, 1).cdf

ppf = scipy.stats.norm.ppf#inverse function of gaussian distribution

a,b=map(int,input("Enter the boundaries of interval(a&b):\n").split())

n = int(input("Enter the number of data points:"))#no. of points randomly generated in a region

#norm(0) is the maximum value of gaussian function having mean 0 and std 1.
"""Monte Carlo Sampling over n data points."""

def area(a, b):#area from x=a to x=b 
    random_points = [(np.random.uniform(a, b), np.random.uniform(0, norm(0))) for i in range(n)]# generating points (x,y) in region from a to b.
    under_fx = len([i for i in random_points if i[1] <= norm(i[0])])# checking which r points under the curve of function
    return ((under_fx) / n )* (b - a) * norm(0)# area calculated by multiplying proportion of points under curve with area of rectange from a to b.

#Generate a random number u from U (0, 1)  :[Probability values lie between 0 and 1 as we all know]
U = np.random.uniform(0, 1, 1000)#values of cdf

U = [round(u, 3) for u in U]# uniform random numbers (values of probability) rounded to 3 decimals

N = np.linspace(-3, 3, 1000)


def cdfo(i):
    return round(0.5+area(0,i),3)

dct = {}

for i in N:
    dct[cdfo(i)] = i

X = []

for u in U:
    try:
        X.append(dct[u])
    except:
        pass


plt.hist(X,width=0.53,normed=True)

plt.yticks([])
