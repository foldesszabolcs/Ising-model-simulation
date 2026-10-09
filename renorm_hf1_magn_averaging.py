import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("en+magn_J=0.45_2026-10-06_02-02-15.txt")
magnetization=data[:,1]

magn_avg=np.mean(magnetization[1000:])
print(magn_avg)

def blocking(m):
    m_block = np.asarray(m, dtype=float)

    block_sizes = []
    errors = []
    block_size = 1

    while len(m_block) >= 2:
        # error estimate for current blocking level
        length=len(m_block)
        error = np.std(m_block, ddof=1)/np.sqrt(length)
        block_sizes.append(block_size)
        errors.append(error)
        if len(m_block) % 2 == 1:
            m_block = m_block[:-1]
        # block neighboring pairs
        m_block = 0.5 * (m_block[0::2] + m_block[1::2])
        block_size*=2
    return np.array(block_sizes), np.array(errors)

block_size,errors=blocking(magnetization[1000:])

fig2, ax2 = plt.subplots(1, 1, figsize=(8, 5))
ax2.loglog(block_size,errors,marker="o")
ax2.set_xlabel("Block size")
ax2.set_ylabel(r"$\Delta m$")
ax2.set_title(r"Error of magnetization, $J/kT=0.45$")


print(np.mean(errors[-6:-2]))
#print(errors[-1])

plt.show()

