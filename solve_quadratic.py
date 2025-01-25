"""
Module pour résoudre une équation du second degré de la forme ax² + bx + c = 0.
"""
import math

NO_REAL_SOLUTION = "Pas de solutions réelles."

def solve_quadratic(coeff_a, coeff_b, coeff_c):
    """
    Résout une équation quadratique de la forme ax^2 + bx + c = 0.

    Args:
        coeff_a (float): Coefficient de x^2 (doit être non nul).
        coeff_b (float): Coefficient de x.
        coeff_c (float): Terme constant.

    Returns:
        tuple: Les deux racines réelles si le discriminant est positif.
        float: La racine réelle unique si le discriminant est nul.
        str: Message indiquant qu'il n'y a pas de solutions réelles.
    """
    if coeff_a == 0:
        raise ValueError("Coefficient 'a' ne peut pas être nul pour une équation quadratique.")
    discriminant = coeff_b ** 2 - 4 * coeff_a * coeff_c
    if discriminant > 0:
        root1 = (-coeff_b + math.sqrt(discriminant)) / (2 * coeff_a)
        root2 = (-coeff_b - math.sqrt(discriminant)) / (2 * coeff_a)
        return root1, root2
    if discriminant == 0:
        root = -coeff_b / (2 * coeff_a)
        return root
    return NO_REAL_SOLUTION
# Exemple d'utilisation
COEFF_A = 1  # Renommage en UPPER_CASE
COEFF_B = -3  # Renommage en UPPER_CASE
COEFF_C = 2  # Renommage en UPPER_CASE
result = solve_quadratic(COEFF_A, COEFF_B, COEFF_C)
print("Les solutions sont :", result)
