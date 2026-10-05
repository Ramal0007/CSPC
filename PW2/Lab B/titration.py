import numpy as np
import matplotlib.pyplot as plt

# 1. CSV faylını pandas olmadan, sırf numpy ilə oxuyuruq
data = np.genfromtxt('titration.csv', delimiter=',', skip_header=1)
V = data[:, 0]   # birinici sütun: volume_base
pH = data[:, 1]  # ikinci sütun: pH

# 2. pH-ın V-yə görə dəyişmə sürətini (törəməsini) hesablayırıq: dpH / dV
slope = np.gradient(pH, V)

# 3. Ən böyük sıçrayışın (maksimum meyilliliyin) olduğu indeksi tapırıq
max_slope_index = np.argmax(slope)
v_eq = V[max_slope_index]
ph_eq = pH[max_slope_index]

print(f"Ekvivalentlik nöqtəsi: {v_eq:.2f} mL (pH = {ph_eq:.2f})")

# 4. Qrafikləri yan-yana çəkirik
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Sol qrafik: pH əyrisi
ax1.plot(V, pH, color='blue', label='pH əyrisi')
ax1.axvline(x=v_eq, color='red', linestyle='--', label=f'Ekvivalentlik ({v_eq:.1f} mL)')
ax1.set_xlabel('Həcm (mL)')
ax1.set_ylabel('pH')
ax1.set_title('Titrasiya Əyrisi')
ax1.legend()
ax1.grid(True)

# Sağ qrafik: Törəmə əyrisi (Slope)
ax2.plot(V, slope, color='green', label='dpH / dV (Törəmə)')
ax2.axvline(x=v_eq, color='red', linestyle='--', label=f'Maksimum meyil ({v_eq:.1f} mL)')
ax2.set_xlabel('Həcm (mL)')
ax2.set_ylabel('dpH / dV')
ax2.set_title('Titrasiya Törəməsi')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('titration.png')
print("Qrafik 'titration.png' olaraq yadda saxlanıldı.")
