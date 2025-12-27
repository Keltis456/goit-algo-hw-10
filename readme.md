# Homework 10: Optimization and Integration

## Task 1: Production Optimization

Using PuLP library to maximize beverage production with resource constraints.

**Optimal Solution:**
- Lemonade: 30 units
- Fruit Juice: 20 units
- Total: 50 units

## Task 2: Definite Integral Calculation

Computing the integral of f(x) = x² from 0 to 2 using Monte Carlo method.

### Results Comparison

| Method | Result | Error |
|--------|--------|-------|
| Monte Carlo (100,000 points) | ~2.6786 | ~0.45% |
| SciPy quad | 2.666667 | ~10⁻¹⁴ |
| Analytical (x³/3) | 2.666667 | exact |

### Conclusions

1. **Monte Carlo Method Accuracy**: The Monte Carlo method produces results very close to the exact value (8/3 ≈ 2.6667). With 100,000 random points, the error is typically less than 1%, which confirms the method works correctly for numerical integration.

2. **Comparison with quad**: The SciPy `quad` function provides extremely precise results with an error of approximately 10⁻¹⁴, which is essentially machine precision. This numerical integration method is significantly more accurate than Monte Carlo for smooth, well-behaved functions.

3. **Analytical Verification**: The analytical solution ∫x²dx = x³/3 evaluated from 0 to 2 gives exactly 8/3 ≈ 2.666667. Both numerical methods converge to this value, confirming their correctness.

4. **Monte Carlo Characteristics**:
   - Accuracy improves with more random points (proportional to 1/√n)
   - Simple to implement and understand
   - Particularly useful for high-dimensional integrals where traditional methods struggle
   - Has inherent randomness, so results vary slightly between runs

5. **Practical Application**: For simple one-dimensional integrals like this, `quad` is preferred due to its speed and precision. Monte Carlo becomes advantageous for complex, multi-dimensional integration problems.

