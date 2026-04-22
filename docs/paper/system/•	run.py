import numpy as np
import matplotlib.pyplot as plt

from .core import energy
from .control import control
from .dynamics import dynamics

# initial state
X = np.random.randn(3)

dt = 0.01
steps = 500

E_hist = []

for t in range(steps):
    # simulate validation inputs
    C = np.random.rand(4) * 0.1
    I_eff = 1 - np.sum(C)

    # control
    U = control(X, I_eff)

    # dynamics
    dX = dynamics(X, U)

    # update
    X = X + dt * dX

    # track energy
    E_hist.append(energy(X))

# plot
plt.plot(E_hist)
plt.title("SEKHEM Energy Convergence")
plt.xlabel("Time Step")
plt.ylabel("E(X)")
plt.grid()
plt.show()
