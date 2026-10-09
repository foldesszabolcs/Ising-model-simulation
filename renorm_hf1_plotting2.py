import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

MCS_max=[20000,30000,50000,70000,100000]
uncertainties_05=[0.0002633331133764868,0.00020174608130106973,0.00014729099605166187,0.00016436081702800586,0.000110536093034109]
uncertainties_045=[0.0027851851717325743,0.00393665099667169,0.0026085836908333335,0.003960571758925273,0.001980679532619607]

def trend(N,C):
    return C/np.sqrt(N)
interval=range(19000,101000,1000)
popt05,pcov05=curve_fit(trend,MCS_max,uncertainties_05)
popt045,pcov045=curve_fit(trend,MCS_max,uncertainties_045)
print(popt05,np.sqrt(np.diag(pcov05)))
print(popt045,np.sqrt(np.diag(pcov045)))

fig2, ax2 = plt.subplots(1, 1, figsize=(8, 5))
ax2.plot(MCS_max,uncertainties_05,marker="o", label="Uncertainty values")
ax2.set_xlabel(r"MCS$_{max}$")
ax2.set_ylabel(r"$\Delta m$")
ax2.set_title(r"Error of magnetization over simulation length, $J/kT=0.5$")
ax2.plot(interval,trend(interval,*popt05), label=r"Fitted $1/\sqrt{N}$ curve")
ax2.legend()

fig3, ax3 = plt.subplots(1, 1, figsize=(8, 5))
ax3.plot(MCS_max,uncertainties_045,marker="o", label="Uncertainty values")
ax3.set_xlabel(r"MCS$_{max}$")
ax3.set_ylabel(r"$\Delta m$")
ax3.set_title(r"Error of magnetization over simulation length, $J/kT=0.45$")
ax3.plot(interval,trend(interval,*popt045), label=r"Fitted $1/\sqrt{N}$ curve")
ax3.legend()



plt.show()