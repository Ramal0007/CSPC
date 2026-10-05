# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
    conda env create -f PW<n>/Lab <X>/environment.yml
    conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- Built a simulation of radioactive decay using pure Python loops and vectorized NumPy implementation.
- Implemented unit tests using pytest and set up a reproducible Conda environment with Git tracking.

**Speed comparison (loop vs NumPy):**
- loop : 0.0824 s
- numpy : 0.0012 s
- speed-up: 68.67 x faster

**Tests:** all passing? yes

**Conclusion:**
- Vectorized operations in NumPy drastically outperform standard Python loops for large dataset simulations.
- Creating isolated environments ensures code reproducibility across different machines without dependency conflicts.
- Writing unit tests guarantees that refactoring to NumPy maintains physical and mathematical correctness.
## PW1 --- Lab B

### Results
The observed data showed an exponential decay over time. The observed points closely followed the theoretical exponential decay curve, confirming that the experimental data matches the analytical law.

### Workflow Automation
The Snakemake pipeline automates the generation of the decay plot (`figure.png`) by tracking dependencies (`decay_observed.csv` and `plot.py`) and executing the Python script only when necessary.
