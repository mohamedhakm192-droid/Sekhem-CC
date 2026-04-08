import time
import numpy as np

# ===============================
# SEKHEM C C — CONFIG
# ===============================
DT_TARGET = 0.02
ALPHA = 0.03

true_value = 100.0
sigmas = np.array([2.0, 3.0, 4.0])

# ===============================
# SEKHEM C C — LAYER 1: PERCEPTION
# ===============================
def SEKHEM_CC_PERCEPTION():
    X = np.array([
        true_value + np.random.normal(0, sigmas[0]),
        true_value + np.random.normal(0, sigmas[1]),
        true_value + np.random.normal(0, sigmas[2]),
    ])
    print("[SEKHEM C C][PERCEPTION] X:", X)
    return X

# ===============================
# SEKHEM C C — LAYER 2: ANALYSIS
# ===============================
def SEKHEM_CC_ANALYSIS(X):
    A = np.array([
        X[0],
        X[1] * 1.02,
        X[2] * 0.98
    ])
    print("[SEKHEM C C][ANALYSIS] A:", A)
    return A

# ===============================
# SEKHEM C C — LAYER 3: STRUCTURED
# ===============================
def SEKHEM_CC_STRUCTURED(A):
    P = (A - np.mean(A)) / (np.std(A) + 1e-6)
    print("[SEKHEM C C][STRUCTURED] P:", P)
    return P

# ===============================
# SEKHEM C C — LAYER 4: FILTER
# ===============================
K = 0.3

def SEKHEM_CC_FILTER(P):
    Z = P + np.random.normal(0, 0.3, 3)
    F = P + K * (Z - P)
    print("[SEKHEM C C][FILTER] F:", F)
    return F

# ===============================
# SEKHEM C C — LAYER 5: TRIANGULATION
# ===============================
def SEKHEM_CC_WEIGHTS(sigmas):
    inv = 1.0 / (sigmas**2)
    return inv / np.sum(inv)

weights = SEKHEM_CC_WEIGHTS(sigmas)

def SEKHEM_CC_TRIANGULATION(F):
    global weights
    x_hat = np.sum(F * weights)
    print("[SEKHEM C C][TRIANGULATION] x_hat:", x_hat)
    return x_hat

# ===============================
# SEKHEM C C — LAYER 6: DECISION
# ===============================
def SEKHEM_CC_DECISION(x_hat):
    confidence = 1 / np.sum(sigmas)
    decision = x_hat if confidence > 0.2 else "NO DECISION"
    print("[SEKHEM C C][DECISION]", decision)
    return decision, confidence

# ===============================
# SEKHEM C C — LAYER 7: FEEDBACK
# ===============================
def SEKHEM_CC_FEEDBACK(x_hat):
    global weights
    error = abs(true_value - x_hat)
    performance = 1 / (sigmas + error)

    weights = weights + ALPHA * (performance / np.sum(performance))
    weights = weights / np.sum(weights)

    print("[SEKHEM C C][FEEDBACK] Error:", error)
    print("[SEKHEM C C][FEEDBACK] Updated Weights:", weights)

    return error

# ===============================
# SEKHEM C C — MAIN LOOP
# ===============================
for step in range(10):
    t0 = time.time()

    X = SEKHEM_CC_PERCEPTION()
    A = SEKHEM_CC_ANALYSIS(X)
    P = SEKHEM_CC_STRUCTURED(A)
    F = SEKHEM_CC_FILTER(P)
    x_hat = SEKHEM_CC_TRIANGULATION(F)
    decision, conf = SEKHEM_CC_DECISION(x_hat)
    error = SEKHEM_CC_FEEDBACK(x_hat)

    t1 = time.time()
    cycle_time = (t1 - t0) * 1000

    print(f"\n[SEKHEM C C][CYCLE {step}] Time: {cycle_time:.2f} ms\n")

    time.sleep(max(0, DT_TARGET - (t1 - t0)))
