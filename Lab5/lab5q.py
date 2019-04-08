import numpy as np
import matplotlib.pyplot as plt
a, b = [], []
for i in range(1000):
    x = np.random.random()
    if 0 <= x <= 0.5:
        a.append(0)
        y = np.random.random()
        if 0 <= y <= 0.75:
            b.append(0)
        else:
            b.append(1)
    else:
        a.append(1)
        y = np.random.random()
        if 0 <= y <= 0.65:
            b.append(1)
        else:
            b.append(0)

joint = list(zip(b, a))

px0, py0 = a.count(0)/1000 , b.count(0)/1000
px1, py1 = 1-px0, 1-py0
py0x0 = joint.count((0, 0)) / a.count(0)
py0x1 = joint.count((0, 1)) / a.count(1)
py1x0 = 1 - py0x0
py1x1 = 1 - py0x1

print(f'p(Y = 0) = {py0}')
print(f'p(Y = 0) = p(Y = 0|X = 0)p(X = 0) + p(Y = 0|X = 1)p(X = 1)\n\t = \
{py0x0}*{px0} + {py0x1}*{px1}\n\t = \
{py0x0 * px0 + py0x1 * px1}')


print(f'\n\np(Y = 1) = {py1}')
print(f'p(Y = 1) = p(Y = 1|X = 0)p(X = 0) + p(Y = 1|X = 1)p(X = 1)\n\t = \
{py1x0}*{px0} + {py1x1}*{px1}\n\t = \
{py1x0 * px0 + py1x1 * px1}')

plt.scatter([0, 1], [py0, py1])
plt.ylim(0,1)








from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

x=[1,4,5]
y=[2,6,8]
z=[1,3,5]

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(x,y,z,c='r',marker='o')
plt.show()


