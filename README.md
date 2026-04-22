SEKHEM-TSDD

A Validated Energy-Based Triadic Decision Framework

⸻

Overview

SEKHEM-TSDD is a unified decision–control framework in which decision-making is not computed, but emerges as a stable equilibrium of a validated energy-driven dynamical system.

The framework operates over a triadic state space:

X = (R, C, P)

where:
	•	R: Reality (perception)
	•	C: Cognition (internal representation)
	•	P: Prediction (future estimation)

⸻

Core Principle

Decision is not computed—it emerges from validated energy dynamics.

⸻

Mathematical Model

Energy Function

E(X) = (R - C)^2 + (C - P)^2 + (R - P)^2

System Dynamics

\dot{X} = -2LX + U_{eff}

PAC Transformation

\Phi_{PAC}(X) = X + \eta(\bar{X} - X)

Control Law

U_{eff} = \gamma \cdot \alpha(Q) \cdot (1 - N) \cdot K \cdot \Phi_{PAC}(X)

Validation Gate

\gamma =
\begin{cases}
1 & I_{eff} \ge \theta \\
0 & \text{otherwise}
\end{cases}

⸻

Key Properties
	•	Global stability (Lyapunov-based)
	•	Exponential convergence
	•	Noise robustness
	•	Energy-constrained control
	•	Built-in safety via validation gating

⸻

Repository Structure
src/            # Core mathematical model
simulation/     # Numerical experiments
results/        # Output plots and logs
figures/        # Architecture diagrams
paper/          # PDF paper

⸻

Running the Simulation
pip install -r requirements.txt
python simulation/run_simulation.py

⸻

Results

SEKHEM-TSDD demonstrates:
	•	Faster convergence than RL
	•	Lower oscillation
	•	Reduced energy usage
	•	No unsafe actions (validation-gated)

⸻

Paper

Full paper available in:
paper/SEKHEM_TSDD.pdf
Author

Mohamed Abdelnaby
SEKHEM CC Framework


