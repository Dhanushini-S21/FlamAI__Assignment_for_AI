# Parametric Curve Parameter Estimation

## Research and Development / AI Assignment

### 1. Objective

Estimate unknown parameters **θ, M, and X** from a given parametric equation of a curve using the provided `(x, y)` data points.

The estimated parameters are selected such that the predicted curve minimizes the **L1 distance** from the expected curve obtained from the provided dataset.

---

## 2. Problem Statement

Given the parametric equation:

$$
x(t)=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
$$

$$
y(t)=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
$$

The unknown parameters are:

* \(\theta\)
* \(M\)
* \(X\)

### Parameter Constraints

$$
0^\circ < \theta < 50^\circ
$$

$$
-0.05 < M < 0.05
$$

$$
0 < X < 100
$$

Parameter \(t\) satisfies:

$$
6 < t < 60
$$

---

## 3. Input Data

The provided `xy_data.csv` file contains points that lie on the expected curve.

The dataset is used as reference data for estimating the unknown parameters.

---

## 4. Approach

The parameter estimation process follows these steps:

1. Load `(x, y)` coordinates from `xy_data.csv`.
2. Define the given parametric equations.
3. Generate uniformly sampled values of \(t\) within the specified range.
4. Define the unknown parameters \(\theta\), \(M\), and \(X\).
5. Apply parameter constraints according to the assignment.
6. Generate predicted curve coordinates.
7. Compare predicted coordinates with expected data points.
8. Calculate L1 distance between expected and predicted points.
9. Apply numerical optimization to minimize L1 distance.
10. Obtain optimal values of \(\theta\), \(M\), and \(X\).
11. Plot expected data points and fitted parametric curve.
12. Report final parameter values and L1 distance.

---

## 5. Optimization Objective

The optimization objective is to minimize the L1 distance:

$$
L_1=\sum_i \left(|x_i-\hat{x}_i|+|y_i-\hat{y}_i|\right)
$$

where:

* \(x_i,y_i\) are expected data points.
* \(\hat{x}_i,\hat{y}_i\) are predicted points generated using estimated parameters.

The optimization searches for:

$$
(\theta,M,X)=\arg\min_{\theta,M,X} L_1
$$

subject to the specified parameter constraints.

---

## 6. Estimated Parameters

Final estimated values:

$$
\theta = YOUR_VALUE
$$

$$
M = YOUR_VALUE
$$

$$
X = YOUR_VALUE
$$

### Final L1 Distance

$$
L_1 = YOUR_L1_VALUE
$$

---

## 7. Final Parametric Equation

After substituting estimated parameters:

$$
\left(
t\cos(YOUR\_THETA)
-e^{YOUR\_M|t|}\sin(0.3t)\sin(YOUR\_THETA)
+YOUR\_X,
\right.
$$

$$
\left.
42+t\sin(YOUR\_THETA)
+e^{YOUR\_M|t|}\sin(0.3t)\cos(YOUR\_THETA)
\right)
$$

### Desmos Form

```text
(
t*cos(YOUR_THETA)-e^(YOUR_M*abs(t))*sin(0.3*t)*sin(YOUR_THETA)+YOUR_X,
42+t*sin(YOUR_THETA)+e^(YOUR_M*abs(t))*sin(0.3*t)*cos(YOUR_THETA)
)
```

---

## 8. Visualization

The fitted curve is compared with the provided data points.

`results/fitted_curve.png` contains the visualization of:

* Expected data points
* Predicted parametric curve
* Curve fitting quality

---

## 9. Project Structure

```text
parametric-curve-parameter-estimation/
│
├── README.md
├── xy_data.csv
├── estimate_parameters.py
├── requirements.txt
├── .gitignore
│
└── results/
    ├── fitted_curve.png
    └── parameter_results.txt
```

---

## 10. Technologies Used

* Python
* NumPy
* Pandas
* SciPy
* Matplotlib
* Numerical Optimization
* Parametric Curve Fitting
* L1 Distance Minimization

---

## 11. Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to project directory:

```bash
cd parametric-curve-parameter-estimation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 12. Execution

Run:

```bash
python estimate_parameters.py
```

The program calculates:

* Optimal \(\theta\)
* Optimal \(M\)
* Optimal \(X\)
* L1 distance
* Fitted curve visualization

---

## 13. Reproducibility

The complete parameter-estimation workflow is implemented in `estimate_parameters.py`.

Using the provided `xy_data.csv` and dependencies listed in `requirements.txt`, the estimation process can be reproduced locally.

---

## 14. Result

The optimized parameters define a parametric curve that closely fits the provided dataset while minimizing the L1 distance between expected and predicted points.

The final values of \(\theta\), \(M\), and \(X\) are reported above and can be directly substituted into the original parametric equation.

---

## 15. Reference

Desmos visualization and curve representation:

https://www.desmos.com/calculator/tfn01kghwl

---

## 16. Author

**Dhanushini**
 AI Assignment
