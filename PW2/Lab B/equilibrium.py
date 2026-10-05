import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

# 1. Tarazlıq sabiti
K = 50.0

# 2. k_imbalance(x) funksiyası: (2x)^2 - K * (1-x)^2 = 0
def k_imbalance(x):
    return 4 * (x**2) - K * ((1 - x)**2)

# 3. k_imbalance-in törəməsi (Newton üsulunun dəqiq və sürətli yığılması üçün)
def k_imbalance_prime(x):
    return 8 * x + 2 * K * (1 - x)

# 4. SLSQP üçün kvadratik xəta funksiyası
def error_func(x):
    return k_imbalance(x[0])**2

# --- Üsul 1: Newton üsulu (fprime ilə) ---
x_newton = newton(k_imbalance, x0=0.5, fprime=k_imbalance_prime)

# --- Üsul 2: SLSQP ilə minimize ---
res = minimize(error_func, x0=[0.5], method='SLSQP', bounds=[(0.001, 0.999)])
x_slsqp = res.x[0]

print(f"1. Newton üsulu ilə tapılan x : {x_newton:.4f}")
print(f"2. SLSQP üsulu ilə tapılan x  : {x_slsqp:.4f}")

# Tarazlıq anındakı mol miqdarları
x_eq = x_newton
nH2_eq = 1 - x_eq
nI2_eq = 1 - x_eq
nHI_eq = 2 * x_eq

print("\n--- Tarazlıq anındakı maddə miqdarları (mol) ---")
print(f"H2 : {nH2_eq:.4f} mol")
print(f"I2 : {nI2_eq:.4f} mol")
print(f"HI : {nHI_eq:.4f} mol")

# Qrafikin çəkilməsi
x_vals = np.linspace(0, 0.95, 200)
nH2_vals = 1 - x_vals
nI2_vals = 1 - x_vals
nHI_vals = 2 * x_vals

plt.figure(figsize=(8, 5))
plt.plot(x_vals, nH2_vals, label=r'$\text{H}_2$ ($1-x$)', color='blue')
plt.plot(x_vals, nI2_vals, label=r'$\text{I}_2$ ($1-x$)', color='green', linestyle='--')
plt.plot(x_vals, nHI_vals, label=r'$\text{HI}$ ($2x$)', color='red')
plt.axvline(x=x_eq, color='gray', linestyle=':', label=f'Tarazlıq (x ≈ {x_eq:.2f})')
plt.scatter([x_eq], [nHI_eq], color='red', zorder=5)

plt.xlabel('Reaksiyanın dərinliyi (x)')
plt.ylabel('Maddə miqdarı (mol)')
plt.title('Kimyəvi Tarazlıq: H2 + I2 <=> 2HI')
plt.legend()
plt.grid(True)

plt.savefig('equilibrium.png')
print("\nQrafik 'equilibrium.png' olaraq yadda saxlanıldı.")
