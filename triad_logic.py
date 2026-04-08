
import time
import numpy as np

# ===============================
# SEKHEM C C CONFIG
# ===============================
ALPHA = 0.05          # Learning rate (Meta)
DELTA_SYNC = 0.003    # 3 ms sync threshold
QUALITY_TH = 0.5      # Threshold on precision
K_INIT = 0.3          # Initial Kalman gain

# ===============================
# SENSOR SIMULATION (RAW)
# X_i = x* + noise  --> (Statistical Model)
# ===============================
def sensor(true_value, noise_std):
    return true_value + np.random.normal(0, noise_std)

# ===============================
# ANALYSIS MODELS f_i(X_i)
# (Different transformations = independence)
# ===============================
def model_1(x): return x
def model_2(x): return x * 1.02
def model_3(x): return x * 0.98

# ===============================
# INVERSE VARIANCE WEIGHTS
# w_i = (1/sigma^2) / sum(1/sigma^2)
# (Derived from Lagrange optimization)
# ===============================
def compute_weights(sigmas):
    inv = 1.0 / (sigmas ** 2)
    return inv / np.sum(inv)

# ===============================
# KALMAN-LIKE FILTER
# X_hat = X + K(Z - X)
# (Control theory / estimation)
# ===============================
def kalman_update(x, z, K):
    return x + K * (z - x)

# ===============================
# TRIANGULATION
# X_hat = sum(w_i * X_i)
# (Linear estimator)
# ===============================
def triangulate(values, weights):
    return np.sum(values * weights)

# ===============================
# QUALITY (PRECISION)
# Q = 1 / Var
# ===============================
def quality(sigmas):
    return 1.0 / np.sum(sigmas**2)

# ===============================
# MAIN LOOP (REAL-TIME)
# ===============================
true_value = 100.0
sigmas = np.array([2.0, 3.0, 4.0])   # noise std لكل مستشعر
weights = compute_weights(sigmas)

K = K_INIT

for step in range(50):  # ~50 Hz
    t0 = time.time()

    # -------- RAW PERCEPTION --------
    X = np.array([
        sensor(true_value, sigmas[0]),
        sensor(true_value, sigmas[1]),
        sensor(true_value, sigmas[2])
    ])
    t1 = time.time()

    # -------- ANALYSIS (AI MODELS) --------
    A = np.array([
        model_1(X[0]),
        model_2(X[1]),
        model_3(X[2])
    ])
    t2 = time.time()

    # -------- FILTERING --------
    Z = A + np.random.normal(0, 0.5, 3)  # measurement update
    X_filt = np.array([
        kalman_update(A[i], Z[i], K) for i in range(3)
    ])
    t3 = time.time()

    # -------- TRIANGULATION --------
    X_hat = triangulate(X_filt, weights)
    t4 = time.time()

    # -------- QUALITY CHECK --------
    Q = quality(sigmas)

    if Q < QUALITY_TH:
        decision = "NO DECISION"
    else:
        decision = X_hat
    t5 = time.time()

    # -------- FEEDBACK (META UPDATE) --------
    error = abs(true_value - X_hat)

    # تحديث بسيط للأوزان
    performance = 1.0 / (sigmas + error)
    weights = weights + ALPHA * (performance / np.sum(performance))
    weights = weights / np.sum(weights)

    t6 = time.time()

    # -------- TIMING --------
    T_cycle = (t6 - t0) * 1000  # ms

    print(f"\nStep {step}")
    print(f"Estimate: {X_hat:.3f} | Error: {error:.3f}")
    print(f"Weights: {weights}")
    print(f"Decision: {decision}")
    print(f"Cycle Time: {T_cycle:.2f} ms")
