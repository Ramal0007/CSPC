import time
from decay import simulate_loop, simulate

N0 = 200000
RATE = 0.05
T = 10

# Saf Python dövrünün icra müddəti
start_time = time.perf_counter()
simulate_loop(N0, RATE, T)
loop_time = time.perf_counter() - start_time

# NumPy versiyasının icra müddəti
start_time = time.perf_counter()
simulate(N0, RATE, T)
numpy_time = time.perf_counter() - start_time

speedup = loop_time / numpy_time

print(f"Python Loop Müddəti: {loop_time:.4f} saniyə")
print(f"NumPy Müddəti:       {numpy_time:.4f} saniyə")
print(f"NumPy versiyası {speedup:.2f} dəfə daha sürətlidir.")
