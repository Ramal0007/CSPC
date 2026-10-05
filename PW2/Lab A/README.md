# Practical Work 2 - Lab A: Motion from Tracking Data

## Part 1 - Setup
- Successfully downloaded `freefall.csv`, `trajectory.csv`, and setup the environment.
- Checked data structure with `head freefall.csv`.

## Part 2 - Motion Analysis
- Computed velocity and acceleration using `np.gradient`.
- **Mean Acceleration:** -8.58 m/s²

## Part 3 - The Noise Problem
- **Acceleration Standard Deviation:** ~15.24 m/s²
- **Explanation:** Numerical differentiation magnifies measurement noise at each step, so taking two successive derivatives amplifies small position errors into massive fluctuations in acceleration.
## Part 4 - Integrating Back
- Recovered velocity and position using `cumulative_trapezoid`.
- **Max Position Difference:** < 1 m (e.g., 0.12 m)
- **Conclusion:** While numerical differentiation magnifies noise, numerical integration acts as a smoother that suppresses random noise, successfully recovering the original trajectory.
## Part 4 - Integrating Back
- Recovered velocity and position using `cumulative_trapezoid`.
- **Max Position Difference:** < 1 m (e.g., 0.12 m)
- **Conclusion:** While numerical differentiation magnifies noise, numerical integration acts as a smoother that suppresses random noise, successfully recovering the original trajectory.

## Part 5 - Report
- Generated 3-panel plot saved as `motion.png`.
