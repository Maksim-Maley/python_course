import numpy as np
import matplotlib.pyplot as plt

a = np.arange(50)
b = np.random.randint(0, 10, size=(3, a.size))
y = 1333 + a

fig, ax = plt.subplots(figsize=(5,3))
ax.stackplot(y,a+b,labels=["erik","max","art"])
ax.set_title("top guys")
ax.legend(loc="upper left")
ax.set_ylabel("total debt")
ax.set_xlim(xmin=y[0], xmax=y[-1])
fig.tight_layout()
plt.show()