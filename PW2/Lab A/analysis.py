import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# 1. Data-nın oxunması
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# 2. Törəmə: Sürət və Təcil (Part 2 & 3)
v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration: {np.mean(a):.2f} m/s^2")
print(f"Acceleration std dev: {a.std():.2f} m/s^2")

# 3. İnteqrasiya: Sürət və Mövqeyin bərpası (Part 4)
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_rec))
print(f"Max difference in position: {max_diff:.2f} m")

# 4. 3 Panelli Qrafikin yaradılması (Part 5)
fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# 1-ci Panel: Konum (Position)
axs[0].plot(t, y, label="Measured position")
axs[0].plot(t, y_rec, '--', label="Recovered position")
axs[0].set_ylabel("Position (m)")
axs[0].legend()
axs[0].grid(True)

# 2-ci Panel: Hız (Velocity)
axs[1].plot(t, v, label="Calculated velocity")
axs[1].plot(t, v_rec, '--', label="Recovered velocity")
axs[1].set_ylabel("Velocity (m/s)")
axs[1].legend()
axs[1].grid(True)

# 3-cü Panel: İvme (Acceleration)
axs[2].plot(t, a, label="Calculated acceleration")
axs[2].axhline(-9.81, color='r', linestyle='--', label="True -9.81 m/s^2")
axs[2].set_ylabel("Acceleration (m/s^2)")
axs[2].set_xlabel("Time (s)")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig("motion.png")
print("Saved figure to motion.png")