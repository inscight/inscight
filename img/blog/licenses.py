import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.02, 0.15, 0.5, 0.95, 0.95, 0.85, 0.98])
y = np.array([0.02, 0.50, 0.7, 0.75, 0.85, 0.95, 0.98])

plt.scatter(x, y, 50, plt.cm.jet(np.sqrt(x**2 + y**2)))


plt.text(0.04, 0.02, "Windows EULA", va='center')
plt.text(0.17, 0.50, "Shareware", va='center')
plt.text(0.52, 0.70, "Freeware", va='center')
plt.text(0.94, 0.85, "GPL", ha='right', va='center')
plt.text(0.83, 0.95, "BSD", ha='right', va='center')
plt.text(0.93, 0.75, "FLASH", ha='right', va='center')
plt.text(0.97, 0.97, "WTFPL", ha='right', va='center')

plt.grid(True, linestyle=':')
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.xlabel("Open Source")
plt.ylabel("Free")


plt.savefig("licenses.png")
