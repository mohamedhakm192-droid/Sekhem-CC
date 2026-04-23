SEKHEM-TSDD

A Closed Stochastic–Variational Decision Framework Based on Triadic Interaction

⸻

🚀 Overview

SEKHEM-TSDD is a triadic decision framework based on three interacting components:
	•	Φ (Phi): Goal-driven attraction
	•	Ψ (Psi): Damping / stabilization
	•	Ω (Omega): Energy control

Together, they form a closed-loop decision system capable of stable and efficient behavior.

⸻
🧠 SEKHEM Decision Architecture
        ┌──────────────┐
        │   State (s)  │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   Φ (Phi)    │
        │ Attraction   │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   Ψ (Psi)    │
        │ Damping      │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   Ω (Omega)  │
        │ Energy Ctrl  │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │ Decision D(s)│
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │ Environment  │
        └──────┬───────┘
               │
        └──── Feedback ──▶ (loop)

⸻

📊 Experimental Results

SEKHEM-TSDD demonstrates:
	•	Faster convergence than classical RL
	•	Lower steady-state error
	•	Reduced oscillatory behavior



🔥 Comparison with RL

![Comparison](docs/paper/system/results/comparison.png)
⸻


📉 Stability Behavior

⸻
HOW to RUN

pip install numpy matplotlib
python SEKHEM-TSDD.py
⸻

🧩 Repository Structure
SEKHEM-CC/
│
├── src/
├── results/
├── docs/
└── README.md



⸻

👤 Author

Mohamed Abdelnaby
SEKHEM CC Framework
🔗 Citation

If you use this work, please cite:

Mohamed Abdelnaby,SEKHEM-TSDD: A Closed Stochastic–Variational Decision Framework Based on Triadic Interaction,Zenodo, 2026.DOI: https://doi.org/10.5281/zenodo.195


⸻

🧠 Statement

The triadic interaction (Φ, Ψ, Ω) enables stable and efficient decision dynamics, outperforming standard reinforcement learning baselines.
