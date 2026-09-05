import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution, minimize
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "xy_data.csv"
RESULTS_DIR = ROOT / "results"
RESULTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)
x = df["x"].to_numpy(dtype=float)
y = df["y"].to_numpy(dtype=float)

print("Number of points:", len(df))


def transformed_residual(params):
    theta, M, X = params

    c = np.cos(theta)
    s = np.sin(theta)

    # From coordinate rotation:
    # t = (x-X)cos(theta) + (y-42)sin(theta)
    t = (x - X) * c + (y - 42) * s

    # Perpendicular coordinate
    v = -(x - X) * s + (y - 42) * c

    expected_v = np.exp(M * np.abs(t)) * np.sin(0.3 * t)

    return v - expected_v


def objective(params):
    residuals = transformed_residual(params)
    return np.mean(residuals ** 2)


# Assignment constraints:
# 0 < theta < 50 degrees
# -0.05 < M < 0.05
# 0 < X < 100
bounds = [
    (0.0, np.deg2rad(50.0)),
    (-0.05, 0.05),
    (0.0, 100.0),
]

print("\nRunning global optimization...")

result = differential_evolution(
    objective,
    bounds=bounds,
    seed=42,
    tol=1e-10,
    polish=True,
)

print("Running local refinement...")

refined = minimize(
    objective,
    result.x,
    method="Nelder-Mead",
    options={
        "xatol": 1e-12,
        "fatol": 1e-14,
        "maxiter": 10000,
    },
)

theta, M, X = refined.x
theta_degrees = np.rad2deg(theta)

c = np.cos(theta)
s = np.sin(theta)

# Recover t
t = (x - X) * c + (y - 42) * s

# Reconstruct original curve
x_pred = (
    t * np.cos(theta)
    - np.exp(M * np.abs(t))
    * np.sin(0.3 * t)
    * np.sin(theta)
    + X
)

y_pred = (
    42
    + t * np.sin(theta)
    + np.exp(M * np.abs(t))
    * np.sin(0.3 * t)
    * np.cos(theta)
)

# L1 distance
l1_per_point = np.abs(x - x_pred) + np.abs(y - y_pred)
total_l1 = np.sum(l1_per_point)
mean_l1 = np.mean(l1_per_point)

print("\n========== FINAL RESULTS ==========")
print(f"theta = {theta_degrees:.10f} degrees")
print(f"M     = {M:.10f}")
print(f"X     = {X:.10f}")

print("\nRecovered t range:")
print(f"min(t) = {t.min():.10f}")
print(f"max(t) = {t.max():.10f}")

print("\nL1 Error:")
print(f"Total L1 = {total_l1:.10f}")
print(f"Mean L1  = {mean_l1:.10f}")

# Save results
with open(RESULTS_DIR / "results.txt", "w", encoding="utf-8") as f:
    f.write("Parametric Curve Parameter Estimation\n")
    f.write("====================================\n\n")
    f.write(f"theta = {theta_degrees:.10f} degrees\n")
    f.write(f"M = {M:.10f}\n")
    f.write(f"X = {X:.10f}\n")
    f.write(f"Minimum t = {t.min():.10f}\n")
    f.write(f"Maximum t = {t.max():.10f}\n")
    f.write(f"Total L1 = {total_l1:.10f}\n")
    f.write(f"Mean L1 = {mean_l1:.10f}\n")

predicted = pd.DataFrame({
    "x": x,
    "y": y,
    "x_pred": x_pred,
    "y_pred": y_pred,
    "t": t,
    "l1_error": l1_per_point,
})
predicted.to_csv(RESULTS_DIR / "predicted_points.csv", index=False)

# Plot
order = np.argsort(t)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=8, label="Observed points")
plt.plot(
    x_pred[order],
    y_pred[order],
    linewidth=2,
    label="Predicted curve",
)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Parametric Curve Fitting")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "curve_fit.png", dpi=300)
plt.show()
