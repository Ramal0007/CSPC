import numpy as np
import matplotlib.pyplot as plt

# 1. trajectory.csv faylından məlumatların oxunması
data = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
t = data[:, 0]
x = data[:, 1]
y = data[:, 2]

# 2. x və y üzrə sürət komponentlərinin hesablanması
vx = np.gradient(x, t)
vy = np.gradient(y, t)

# Tam sürətin hesablanması: v = sqrt(vx^2 + vy^2)
speed = np.sqrt(vx**2 + vy**2)

# 3. Qrafiklərin qurulması
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Sol Panel: 2D Yörünge (x vs y)
ax1.plot(x, y, 'b.-', label="Trajectory")
ax1.set_title("2D Path (x vs y)")
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")
ax1.grid(True)
ax1.legend()

# Sağ Panel: Zamanla Sürət (Speed over time)
ax2.plot(t, speed, 'r-', label="Speed")
ax2.set_title("Speed over Time")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Speed (m/s)")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig("trajectory.png")
print("Bonus analiz tamamlandı! Qrafik trajectory.png olaraq saxlanıldı.")