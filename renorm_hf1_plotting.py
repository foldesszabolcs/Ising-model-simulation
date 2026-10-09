import numpy as np
import matplotlib.pyplot as plt

data1=np.loadtxt("en+magn_J=0.45_2026-10-06_02-02-15.txt")
energy=data1[:,0]
magnetization=data1[:,1]
#data2=np.loadtxt("data/errors_J=0.5_2026-10-05_16-49-35.txt")
#block_size=data2[:,0]
#errors=data2[:,1]

fig1, ax1 = plt.subplots(1, 2, figsize=(16,5))
ax1[0].plot(energy)
ax1[0].set_xlabel("MCS")
ax1[0].set_ylabel(r"$E/N$")
ax1[0].set_title(r"Energy over MCS, $J/kT=0.45$")

ax1[1].plot(magnetization)
ax1[1].set_xlabel("MCS")
ax1[1].set_ylabel(r"$m$")
ax1[1].set_title(r"Magnetization over MCS, $J/kT=0.45$")


#fig2, ax2 = plt.subplots(1, 1, figsize=(8, 5))
#ax2.loglog(block_size,errors,marker="o")
#ax2.set_xlabel("Block size")
#ax2.set_ylabel(r"$\Delta m$")
#ax2.set_title(r"Error of magnetization, $J/kT=0.5$")
fig1.tight_layout()
plt.show()