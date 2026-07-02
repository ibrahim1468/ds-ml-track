import numpy as np

def f(x):
    return np.sin(x)

def df_exact(x):
    return np.cos(x)

def df_numeric(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

x_points = np.array([0.0, 0.5, 1.0, 2.0])

h_values = [0.1, 1e-2, 1e-5]

for h in h_values:
    print(f"\n--- h = {h} ---")
    
    for x in x_points:
        num = df_numeric(x, h)
        exact = df_exact(x)
        error = abs(num - exact)

        print(f"x = {x:.2f} | numeric = {num:.6f} | exact = {exact:.6f} | error = {error:.2e}")

def f(x):
    return np.sin(x)

exact = 2.0
a, b = 0.0, np.pi

n_values = [10, 100, 10000]

print("Trapezoidal Rule Integration of sin(x) from 0 to π\n")
print(f"Exact value: {exact}\n")

for n in n_values:
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    
    error = abs(integral - exact)
    
    print(f"n = {n:5d} | h = {h:.2e} | Approx = {integral:.10f} | "
          f"Error = {error:.2e}")

print("\nVerification with np.trapezoid")
for n in n_values:
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral_np = np.trapezoid(y, x)
    error_np = abs(integral_np - exact)
    
    print(f"n = {n:5d} | np.trapz = {integral_np:.10f} | "
          f"Error = {error_np:.2e}")