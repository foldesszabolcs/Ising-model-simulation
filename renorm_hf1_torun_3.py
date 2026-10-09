import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Parameters
L = 100
N = L**2

J = 1.0
H = 0.0
T = 1/0.45             # k_B = J = 1

#n_sweeps = 1000

# Energy
def E(s):  
    return -J * np.sum(s * np.roll(s, -1, axis=0) + s * np.roll(s, -1, axis=1)) - H * np.sum(s)

# Magnetization
def m(s):
    return np.mean(s)

#Blocking
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

for n_sweeps in [20000,30000,50000,70000,100000]:


    
    # Initial configuration
    s = np.ones((L, L))

    # Arrays
    magnetization = np.zeros(n_sweeps)
    energy = np.zeros(n_sweeps)

    # Metropolis
    for sweep in range(n_sweeps):

        for _ in range(N):

            x = np.random.randint(L)
            y = np.random.randint(L)

            spin = s[y, x]

            neighbours = (
                s[(y+1) % L, x]
                + s[(y-1) % L, x]
                + s[y, (x+1) % L]
                + s[y, (x-1) % L]
            )

            dE = 2 * spin * (J * neighbours + H)

            if dE <= 0 or np.random.rand() < np.exp(-dE / T):
                s[y, x] *= -1

        # Measure once per sweep
        magnetization[sweep] = abs(m(s))
        energy[sweep] = E(s) / N

    #block_size,errors=blocking(magnetization)

    filename = f"J=0.45_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open("en+magn_"+str(filename), "x") as f:
        np.savetxt(f,np.column_stack((energy,magnetization)))
        f.close()
    #with open("errors_"+str(filename), "x") as f:
    #    np.savetxt(f,np.column_stack((block_size,errors)))
    #    f.close()