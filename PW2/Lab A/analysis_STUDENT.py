import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: Data-nı oxu
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: Törəmə (sürət və təcil)
v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration: {np.mean(a):.2f} m/s^2")
# Təcilin standart meylini (std dev) çap edin
print(f"Acceleration std dev: {a.std():.2f} m/s^2")

# TODO 3: İntegral (sürət və mövqeyi bərpa etmək)
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

# TODO 4: Qrafik qurub saxla
fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

axs[0].plot(t, y, label="Measured position")
axs[0].plot(t, y_recovered, '--', label="Recovered position")
axs[0].set_ylabel("Position (m)")
axs[0].legend()
axs[0].grid(True)

axs[1].plot(t, v, label="Calculated velocity")
axs[1].plot(t, v_recovered, '--', label="Recovered velocity")
axs[1].set_ylabel("Velocity (m/s)")
axs[1].legend()
axs[1].grid(True)

axs[2].plot(t, a, label="Calculated acceleration")
axs[2].axhline(-9.81, color='r', linestyle='--', label="True -9.81 m/s^2")
axs[2].set_ylabel("Acceleration (m/s^2)")
axs[2].set_xlabel("Time (s)")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig("motion.png")
print("Saved figure to motion.png")