import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate


def f(x):
    return x ** 2


a = 0
b = 2


def monte_carlo_integrate(func, a, b, num_points=100000):
    x_random = np.random.uniform(a, b, num_points)
    y_max = func(b)
    y_random = np.random.uniform(0, y_max, num_points)

    under_curve = y_random <= func(x_random)
    points_under = np.sum(under_curve)

    rectangle_area = (b - a) * y_max
    integral = rectangle_area * (points_under / num_points)

    return integral, x_random, y_random, under_curve


mc_result, x_rand, y_rand, under = monte_carlo_integrate(
    f, a, b, num_points=100000
)

quad_result, quad_error = integrate.quad(f, a, b)

analytical_result = (b ** 3) / 3 - (a ** 3) / 3

print("=" * 60)
print("Definite Integral Calculation: f(x) = x² from 0 to 2")
print("=" * 60)
print(f"\n1. Monte Carlo Method (100,000 points): {mc_result:.6f}")
print(f"2. SciPy quad function:                 {quad_result:.6f}")
print(f"3. Analytical solution (x³/3):          {analytical_result:.6f}")

print("\n" + "-" * 60)
print("Comparison and Accuracy:")
print("-" * 60)
mc_error = abs(mc_result - analytical_result)
mc_error_percent = (mc_error / analytical_result) * 100
print(f"Monte Carlo error:      {mc_error:.6f} ({mc_error_percent:.4f}%)")
print(f"SciPy quad error:       {quad_error:.2e}")

print("\n" + "-" * 60)
print("Conclusions:")
print("-" * 60)
print("1. All three methods produce very close results (~2.6667)")
print("2. Monte Carlo method provides a good approximation with")
print("   accuracy improving as the number of random points increases")
print("3. SciPy's quad function gives the most precise result")
print("4. The analytical solution confirms: ∫x²dx = x³/3 = 8/3 ≈ 2.6667")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax1.fill_between(ix, iy, color='gray', alpha=0.3)
ax1.set_xlim([x[0], x[-1]])
ax1.set_ylim([0, max(y) + 0.1])
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.axvline(x=a, color='gray', linestyle='--')
ax1.axvline(x=b, color='gray', linestyle='--')
ax1.set_title(f'Integration of f(x) = x² from {a} to {b}')
ax1.grid()

sample_size = 5000
indices = np.random.choice(len(x_rand), sample_size, replace=False)
ax2.scatter(x_rand[indices][under[indices]], y_rand[indices][under[indices]],
            c='green', s=1, alpha=0.5, label='Under curve')
ax2.scatter(x_rand[indices][~under[indices]], y_rand[indices][~under[indices]],
            c='red', s=1, alpha=0.5, label='Above curve')
ax2.plot(x, y, 'b', linewidth=2)
ax2.set_xlim([a - 0.1, b + 0.1])
ax2.set_ylim([0, f(b) + 0.2])
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title(f'Monte Carlo Method (Result: {mc_result:.4f})')
ax2.legend()
ax2.grid()

plt.tight_layout()
plt.savefig('task2_plot.png', dpi=150)
plt.show()
