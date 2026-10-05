import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3

# TODO 1: CSV faylından t və observed massivlərini oxumaq
t, observed = np.loadtxt('decay_observed.csv', delimiter=',', skiprows=1, unpack=True)

# TODO 2: N0 dəyərini təyin etmək və analitik hesablama funksiyasını qurmaq
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: 1x2 ölçülü yan-yana qrafiklər yaratmaq (x və y oxları ortaqdır)
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

# Sol qrafik: Müşahidə olunan məlumatlar (mavi nöqtələr)
ax1.scatter(t, observed, color='blue', label='Observed Data')
ax1.set_title('Observed Data')
ax1.set_xlabel('Time (t)')
ax1.set_ylabel('Count')
ax1.grid(True)

# Sağ qrafik: Analitik qanun (qırmızı xətt)
ax2.plot(t, analytical, color='red', label='Analytical Law')
ax2.set_title('Analytical Decay Law')
ax2.set_xlabel('Time (t)')
ax2.grid(True)

plt.tight_layout()

# TODO 4: Qrafiki figure.png kimi yaddaşda saxlamaq
plt.savefig('figure.png')
print("Qrafik başarıyla 'figure.png' olaraq saxlanıldı!")
