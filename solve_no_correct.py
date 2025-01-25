import math

def solve_equation(coeff_a, coeff_b, coeff_c):
    discriminant = coeff_b**2 - 4 * coeff_a * coeff_c
    if discriminant > 0:
        x1 = (-coeff_b + math.sqrt(discriminant)) / (2 * coeff_a)
        x2 = (-coeff_b - math.sqrt(discriminant)) / (2 * coeff_a)
        return x1;x2
    elif discriminant == 0:
        x = -coeff_b / (2 * coeff_a)
        return x
    else:
        return None

# Exemple d'utilisation
coeff_a = 1
coeff_b = -3
coeff_c = 2
result = solve_equation(coeff_a, coeff_b, coeff_c)
print("Les solutions sont :", result)