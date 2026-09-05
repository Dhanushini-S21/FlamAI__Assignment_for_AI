# R&D / AI Parametric Curve Assignment

## Folder structure

```text
RD_Curve_Assignment/
│
├── data/
│   └── xy_data.csv
│
├── src/
│   └── solve.py
│
├── results/
│   └── generated files appear here after running
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Important

Run commands from project root:

```powershell
cd "C:\Users\dhanu\Downloads\RD_Curve_Assignment"
```

Do NOT run from `src` folder.

## Install

```powershell
pip install -r requirements.txt
```

## Run

```powershell
python src\solve.py
```

## Assignment

Find unknown parameters:

```text
theta
M
X
```

Constraints:

```text
0 < theta < 50 degrees
-0.05 < M < 0.05
0 < X < 100
6 < t < 60
```

## Parametric equation

```text
x = t*cos(theta) - exp(M*|t|)*sin(0.3t)*sin(theta) + X

y = 42 + t*sin(theta) + exp(M*|t|)*sin(0.3t)*cos(theta)
```

## Mathematical transformation

Define:

```text
u = (x-X)*cos(theta) + (y-42)*sin(theta)

v = -(x-X)*sin(theta) + (y-42)*cos(theta)
```

Then:

```text
u = t

v = exp(M*|t|)*sin(0.3t)
```

Therefore:

```text
v = exp(M*|u|)*sin(0.3u)
```

This allows theta, M, X to be optimized without treating every t value as separate unknown.

## Optimization

Global optimization:

```text
scipy.optimize.differential_evolution
```

Local refinement:

```text
scipy.optimize.minimize
```

## Expected fitted values

Approximately:

```text
theta = 30 degrees
M = 0.03
X = 55
```

Run code to obtain exact floating-point values.

## Final equation

```text
(t*cos(0.5235987756)
 - exp(0.03*|t|)*sin(0.3t)*sin(0.5235987756) + 55,

 42 + t*sin(0.5235987756)
 + exp(0.03*|t|)*sin(0.3t)*cos(0.5235987756))
```

## Output

After execution:

```text
results/
├── results.txt
├── predicted_points.csv
└── curve_fit.png
```

## GitHub

```powershell
git init
git add .
git commit -m "Parametric curve parameter estimation"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
