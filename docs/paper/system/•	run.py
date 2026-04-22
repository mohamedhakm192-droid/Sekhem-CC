import numpy as np
import matplotlib.pyplot as plt

# =========================
# Environment
# =========================
class Environment:
    def __init__(self):
        self.state = np.random.rand(3)
        self.target = np.array([1.0, 1.0, 1.0])

    def step(self, action):
        noise = np.random.randn(3) * 0.05
        self.state = self.state + action + noise

        # Distance to target (Error)
        error = np.linalg.norm(self.state - self.target)

        # Energy usage
        energy = np.linalg.norm(action)

        # Stability (variance)
        stability = -np.var(self.state)

        return self.state, error, energy, stability


# =========================
# SEKHEM-TSDD Agent
# =========================
class SEKHEM_TSDD:
    def phi(self, state, target):
        # Goal attraction
        return -np.linalg.norm(state - target)

    def psi(self, state):
        # Stability term
        return -np.var(state)

    def omega(self, action):
        # Energy penalty
        return -np.linalg.norm(action)

    def decide(self, state, target):
        direction = target - state
        action = 0.1 * direction  # controlled movement

        score = self.phi(state, target) + self.psi(state) + self.omega(action)
        return action, score


# =========================
# Simulation
# =========================
def run_simulation(steps=200):
    env = Environment()
    agent = SEKHEM_TSDD()

    errors = []
    energies = []
    stabilities = []

    for t in range(steps):
        action, score = agent.decide(env.state, env.target)
        state, error, energy, stability = env.step(action)

        errors.append(error)
        energies.append(energy)
        stabilities.append(stability)

    return errors, energies, stabilities


# =========================
# Plot Results
# =========================
def plot_results(errors, energies, stabilities):
    plt.figure()
    plt.plot(errors)
    plt.title("Convergence (Error vs Time)")
    plt.xlabel("Time Step")
    plt.ylabel("Error")

    plt.figure()
    plt.plot(energies)
    plt.title("Energy Usage")

    plt.figure()
    plt.plot(stabilities)
    plt.title("System Stability")

    plt.show()


# =========================
# Main
# =========================
if __name__ == "__main__":
    errors, energies, stabilities = run_simulation()
    plot_results(errors, energies, stabilities)

    print("✅ Simulation finished successfully.")
