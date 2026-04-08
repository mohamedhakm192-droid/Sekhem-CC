import time
import numpy as np

# =========================================
# SEKHEM C C — CONFIG
# =========================================
SEKHEM_CC_NUM_TARGETS = 100
SEKHEM_CC_DT_TARGET = 0.02   # 20 ms → 50 Hz
SEKHEM_CC_ALPHA = 0.02

SEKHEM_CC_TRUE_VALUES = np.random.uniform(80, 120, SEKHEM_CC_NUM_TARGETS)
SEKHEM_CC_SIGMAS = np.array([2.0, 3.0, 4.0])

# =========================================
# SEKHEM C C — LAYER 1: PERCEPTION
# =========================================
def SEKHEM_CC_LAYER_PERCEPTION():
    noise = np.random.normal(0, SEKHEM_CC_SIGMAS.reshape(3,1),
                             (3, SEKHEM_CC_NUM_TARGETS))
    X = SEKHEM_CC_TRUE_VALUES + noise
    print("[SEKHEM C C][PERCEPTION] Shape:", X.shape)
    return X

# =========================================
# SEKHEM C C — LAYER 2: ANALYSIS
# =========================================
def SEKHEM_CC_LAYER_ANALYSIS(X):
    A = np.zeros_like(X)
    A[0] = X[0]
    A[1] = X[1] * 1.02
    A[2] = X[2] * 0.98
    print("[SEKHEM C C][ANALYSIS] Done")
    return A

# =========================================
# SEKHEM C C — LAYER 3: STRUCTURED
# =========================================
def SEKHEM_CC_LAYER_STRUCTURED(A):
    mean = np.mean(A, axis=0)
    std = np.std(A, axis=0) + 1e-6
    P = (A - mean) / std
    print("[SEKHEM C C][STRUCTURED] Normalized")
    return P

# =========================================
# SEKHEM C C — LAYER 4: FILTER
# =========================================
SEKHEM_CC_K = 0.3

def SEKHEM_CC_LAYER_FILTER(P):
    Z = P + np.random.normal(0, 0.3, P.shape)
    F = P + SEKHEM_CC_K * (Z - P)
    print("[SEKHEM C C][FILTER] Applied")
    return F

# =========================================
# SEKHEM C C — LAYER 5: TRIANGULATION
# =========================================
def SEKHEM_CC_COMPUTE_WEIGHTS(sigmas):
    inv = 1.0 / (sigmas**2)
    return inv / np.sum(inv)

SEKHEM_CC_WEIGHTS = SEKHEM_CC_COMPUTE_WEIGHTS(SEKHEM_CC_SIGMAS)

def SEKHEM_CC_LAYER_TRIANGULATION(F):
    global SEKHEM_CC_WEIGHTS
    x_hat = np.sum(F * SEKHEM_CC_WEIGHTS.reshape(3,1), axis=0)
    print("[SEKHEM C C][TRIANGULATION] Computed")
    return x_hat

# =========================================
# SEKHEM C C — LAYER 6: DECISION
# =========================================
def SEKHEM_CC_LAYER_DECISION(x_hat):
    confidence = 1 / np.sum(SEKHEM_CC_SIGMAS)
    decisions = np.where(confidence > 0.2, x_hat, np.nan)
    print("[SEKHEM C C][DECISION] Confidence:", round(confidence,3))
    return decisions, confidence

# =========================================
# SEKHEM C C — LAYER 7: FEEDBACK
# =========================================
def SEKHEM_CC_LAYER_FEEDBACK(x_hat):
    global SEKHEM_CC_WEIGHTS
    error = np.abs(SEKHEM_CC_TRUE_VALUES - x_hat)

    performance = 1 / (SEKHEM_CC_SIGMAS.reshape(3,1) + np.mean(error))

    SEKHEM_CC_WEIGHTS = SEKHEM_CC_WEIGHTS + SEKHEM_CC_ALPHA * np.mean(performance, axis=1)
    SEKHEM_CC_WEIGHTS = SEKHEM_CC_WEIGHTS / np.sum(SEKHEM_CC_WEIGHTS)

    print("[SEKHEM C C][FEEDBACK] Mean Error:", round(np.mean(error),3))
    print("[SEKHEM C C][FEEDBACK] Updated Weights:", SEKHEM_CC_WEIGHTS)

    return np.mean(error)

# =========================================
# SEKHEM C C — MAIN LOOP
# =========================================
for step in range(10):
    t0 = time.time()

    X = SEKHEM_CC_LAYER_PERCEPTION()
    A = SEKHEM_CC_LAYER_ANALYSIS(X)
    P = SEKHEM_CC_LAYER_STRUCTURED(A)
    F = SEKHEM_CC_LAYER_FILTER(P)
    x_hat = SEKHEM_CC_LAYER_TRIANGULATION(F)
    decisions, conf = SEKHEM_CC_LAYER_DECISION(x_hat)
    error = SEKHEM_CC_LAYER_FEEDBACK(x_hat)

    t1 = time.time()

    cycle_time = (t1 - t0)
    sleep_time = max(0, SEKHEM_CC_DT_TARGET - cycle_time)
    time.sleep(sleep_time)

    total_time = (cycle_time + sleep_time) * 1000

    print(f"\n[SEKHEM C C][CYCLE {step}]")
    print(f"Targets: {SEKHEM_CC_NUM_TARGETS}")
    print(f"Cycle Time: {total_time:.2f} ms\n")
