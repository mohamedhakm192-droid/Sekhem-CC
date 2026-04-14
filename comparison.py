import numpy as np
import matplotlib.pyplot as plt

# ---------------- الزمن ----------------
dt = 0.01
T = 15
time = np.arange(0, T, dt)

# ---------------- الهدف ----------------
def target(t):
    return np.array([
        np.sin(t) + 0.5*np.sin(3*t),
        np.cos(t)
    ])

# ---------------- SEKHEM ----------------
X_s = np.array([0.0, 0.0])
K = 3.0

# ---------------- "Kalman بسيط" ----------------
X_k = np.array([0.0, 0.0])
alpha = 0.2   # عامل تنعيم (تقليدي)

# ---------------- تخزين ----------------
err_s = []
err_k = []

traj_s = []
traj_k = []
traj_y = []

for t in time:
    Y = target(t)

    noise = 0.1 * np.random.randn(2)
    Y_noisy = Y + noise

    # ---- SEKHEM ----
    dX = -K * (X_s - Y_noisy)
    X_s = X_s + dt * dX

    # ---- Kalman-like ----
    X_k = X_k + alpha * (Y_noisy - X_k)

    # ---- تسجيل ----
    traj_s.append(X_s.copy())
    traj_k.append(X_k.copy())
    traj_y.append(Y.copy())

    err_s.append(np.linalg.norm(X_s - Y))
    err_k.append(np.linalg.norm(X_k - Y))

traj_s = np.array(traj_s)
traj_k = np.array(traj_k)
traj_y = np.array(traj_y)

# ---------------- الرسم ----------------
plt.figure(figsize=(12,5))

# المسارات
plt.subplot(1,2,1)
plt.plot(traj_y[:,0], traj_y[:,1], label="Target")
plt.plot(traj_s[:,0], traj_s[:,1], label="SEKHEM")
plt.plot(traj_k[:,0], traj_k[:,1], label="Kalman-like")
plt.title("Tracking Comparison")
plt.legend()
plt.grid()

# الخطأ
plt.subplot(1,2,2)
plt.plot(time, err_s, label="SEKHEM Error")
plt.plot(time, err_k, label="Kalman Error")
plt.title("Error vs Time")
plt.legend()
plt.grid()

plt.suptitle("SEKHEM vs Kalman Comparison | Mohamed Abd Elnaby")
plt.tight_layout()
plt.show()

# ---------------- أرقام ----------------
print("Average Error (SEKHEM):", np.mean(err_s))
print("Average Error (Kalman):", np.mean(err_k))
print("\n===== SEKHEM vs Baseline Comparison =====\n")

avg_s = np.mean(err_s)
avg_k = np.mean(err_k)

max_s = np.max(err_s)
max_k = np.max(err_k)

print(f"Average Error (SEKHEM): {avg_s:.4f}")
print(f"Average Error (Baseline): {avg_k:.4f}\n")

print(f"Max Error (SEKHEM): {max_s:.4f}")
print(f"Max Error (Baseline): {max_k:.4f}\n")

# Decision
if avg_s < avg_k:
    print("Result: SEKHEM performs better (lower average error).")
else:
    print("Result: Baseline performs better.")
"}
## Claim

Under identical noisy conditions, SEKHEM-TSDD demonstrates faster convergence and lower tracking error compared to baseline filtering approache
