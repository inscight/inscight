import matplotlib.pyplot as plt


plt.scatter([0.98, 0.02, 0.95], 
            [0.98, 0.02, 0.9], 
            50, plt.cm.jet([0.9, 0.1]))

plt.text(0.97, 0.97, "WTFPL", ha='right', va='top')
plt.text(0.03, 0.03, "Windows EULA")
plt.text(0.97, 0.97, "GPL", ha='right', va='top')

plt.grid(True, linestyle=':')
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.xlabel("Open Source")
plt.ylabel("Free")


plt.savefig("licenses.png")
