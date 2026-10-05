import numpy as np
from scipy.optimize import newton, minimize

# ==========================================
# 2A. Sadə funksiya: f(x) = (x - 3)^2 + 1
# ==========================================
def f(x):
    return (x - 3)**2 + 1

def df(x):
    return 2 * (x - 3)

def d2f(x):
    return 2

def gradient_descent(f_prime, x0, alpha=0.1, num_iters=100):
    x = x0
    for _ in range(num_iters):
        x = x - alpha * f_prime(x)
    return x

# 2A-nı hesablayaq (x0 = 0-dan başlayaraq)
x0_a = 0.0
print("--- 2A Nəticələri ---")
print("Gradient Descent :", gradient_descent(df, x0_a))
print("Newton's Method  :", newton(df, x0_a, fprime=d2f))
print("SLSQP            :", minimize(f, x0_a, method="SLSQP").x[0])


# ==========================================
# 2B. Çətin funksiya: g(x) = x^4 - 3x^2 + x + 5
# ==========================================
def g(x):
    return x**4 - 3*x**2 + x + 5

def dg(x):
    return 4*x**3 - 6*x + 1

def d2g(x):
    return 12*x**2 - 6

def test_2b(x0):
    print(f"\n=== 2B Nəticələri (x0 = {x0} olduqda) ===")
    
    # 1. Gradient Descent
    gd_res = gradient_descent(dg, x0)
    print("Gradient Descent :", gd_res)
    
    # 2. Newton üsulu
    newton_res = newton(dg, x0, fprime=d2g)
    second_deriv = d2g(newton_res)
    is_min = "MINIMUM" if second_deriv > 0 else "MAKSIMUM"
    print(f"Newton üsulu     : {newton_res} (g'' = {second_deriv:.2f} -> {is_min})")
    
    # 3. SLSQP
    slsqp_res = minimize(g, x0, method="SLSQP").x[0]
    print("SLSQP            :", slsqp_res)

test_2b(x0=0.0)
test_2b(x0=2.0)