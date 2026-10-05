## Part 2 — Three routes to a minimum

### 2A. Easy Convex Function
All three methods (Gradient Descent, Newton's method, SLSQP) starting at x0 = 0 converged directly to the global minimum at x = 3.0.

### 2B. A Harder Landscape
- **Do the methods agree?**
  - At `x0 = 0`: Gradient Descent and SLSQP converge to x ≈ -1.3008 (local minimum). Newton's method converges to x ≈ 0.1699, which is a local maximum.
  - At `x0 = 2`: SLSQP and Newton converge to the local minimum near x ≈ 1.1309.

- **Did Newton land on a minimum or another stationary point?**
  - At `x0 = 0`, Newton's method landed on a **local maximum** because $g''(0.1699) = -5.65 < 0$.
  - At `x0 = 2`, Newton's method landed on a **minimum** because $g''(1.1309) = 9.35 > 0$.

- **How did the starting point change the result?**
  - The starting point $x_0$ determines which basin of attraction the optimizer falls into. A poor starting point can cause Newton's method to converge to a maximum or non-global minimum.
## Part 3 --- Rate Constant Fitting
- **Fitted Rate Constant (k)**: 0.05 s⁻¹

## Part 4 --- Chemical Equilibrium
- **Reaction Extent (x)**: 0.7795
- **Equilibrium Amounts**:
  - H2: 0.2205 mol
  - I2: 0.2205 mol
  - HI: 1.5590 mol

## Part 5 --- Titration Equivalence Point
- **Equivalence Point Volume (V_eq)**: 50.0 mL
- **pH at Equivalence Point**: 7.00
