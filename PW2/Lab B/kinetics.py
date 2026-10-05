import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# 1. CSV faylını oxuyuruq (birinci sətri başlanğıc (header) sayaraq atlayır)
data = np.genfromtxt('kinetics.csv', delimiter=',', skip_header=1)
t_data = data[:, 0]  # birinici sütun: time
C_data = data[:, 1]  # ikinci sütun: concentration

# 2. C0 dəyəri (t=0 anındakı ilk ölçüm)
C0 = C_data[0]

# 3. Xəta funksiyası (Total Error)
def total_error(k):
    C_pred = C0 * np.exp(-k * t_data)
    return np.sum((C_data - C_pred)**2)

# 4. Optimallaşdırma (k-nı tapırıq)
initial_k = 0.5
res = minimize(total_error, initial_k, method='SLSQP', bounds=[(0, 5)])
fitted_k = res.x[0]

print(f"Fitted k: {fitted_k:.4f}")

# 5. Qrafikin çəkilməsi
t_dense = np.linspace(min(t_data), max(t_data), 200)
C_dense = C0 * np.exp(-fitted_k * t_dense)

plt.figure(figsize=(8, 5))
plt.scatter(t_data, C_data, color='red', label='Data')
plt.plot(t_dense, C_dense, color='blue', label=f'Fit (k ≈ {fitted_k:.2f})')
plt.xlabel('time')
plt.ylabel('concentration')
plt.legend()
plt.grid(True)
plt.savefig('kinetics.png')
print("Qrafik 'kinetics.png' olaraq yadda saxlanıldı.")
