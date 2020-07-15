import matplotlib.pyplot as plt
import numpy as np
import arknight
import GenshinImpact

a=np.zeros(999)
b=np.zeros(999)
c=np.zeros(999)
d=np.full((999),0.01)
for i in range(1,1000):
    a[i-1] = arknight.arknight(i)
    b[i-1] = GenshinImpact.GenshinImpact(0.006,89,i)
    c[i-1] = GenshinImpact.GenshinImpact(0.003,179,i)
x = np.arange(1,1000)
fig = plt.figure(figsize=(4,6))
ax = plt.subplot(111)
plt.plot(x,a,color='b',label='Arknights')
plt.plot(x,b,color='r',label='GI any 5*')
plt.plot(x,c,color='g',label='GI 5* character')
plt.plot(x,d,color='orange',label='FGO')
plt.ylabel('Rate')
plt.xlabel('Pulls')
ax.legend(loc='upper center', bbox_to_anchor=(0.7, 0.9), shadow=True, ncol=1)
fig.savefig('graph.png',dpi=128)
plt.show()