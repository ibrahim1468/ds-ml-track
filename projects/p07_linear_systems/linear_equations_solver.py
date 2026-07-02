import re
import numpy as np

max_eqs = 4

while True:
    try:
        n = int(input(f"Enter number of equations (2-{max_eqs}): "))
        if 2 <= n <= max_eqs:
            break
        else:
            print(f"Please enter a number between 2 and {max_eqs}.")
    except ValueError:
        print("Invalid input. Enter an integer only.")

def is_valid_variable(var):
    return re.match(r'^[A-Za-z_]\w*$', var) is not None

def parse_equation(eq):
    eq = eq.replace(" ", "")
    if "=" not in eq:
        raise ValueError("Equation must contain '=' sign.")

    left, right = eq.split("=", 1)
    term_pattern = r'([+-]?\s*\d*\.?\d*)\s*([A-Za-z_]\w*)'
    
    terms = re.findall(term_pattern, left)
    
    coeffs = {}
    for coeff_str, var in terms:
        if not var:
            continue
        if not is_valid_variable(var):
            raise ValueError(f"Invalid variable name: {var}")

        coeff_str = coeff_str.strip()
        if coeff_str in ("", "+", "+ "):
            coeff = 1.0
        elif coeff_str in ("-", "- "):
            coeff = -1.0
        else:
            try:
                coeff = float(coeff_str)
            except ValueError:
                raise ValueError(f"Invalid coefficient: {coeff_str}")

        coeffs[var] = coeffs.get(var, 0.0) + coeff
        
    if not coeffs and left:
        left = re.sub(r'([+-])', r' \1', left)
        terms = re.findall(term_pattern, left)
        for coeff_str, var in terms:
            if var:
                coeff_str = coeff_str.strip()
                coeff = 1.0 if coeff_str in ("", "+") else -1.0 if coeff_str == "-" else float(coeff_str)
                coeffs[var] = coeffs.get(var, 0.0) + coeff

    try:
        rhs_value = float(right)
    except ValueError:
        raise ValueError("Right-hand side must be a number.")

    return coeffs, rhs_value

equations = []
all_variables = set()

print("\nEnter equations one by one (e.g., 2x + 3y = 8):")

for i in range(n):
    while True:
        eq_input = input(f"Equation #{i+1}: ").strip()
        try:
            coeff_dict, rhs = parse_equation(eq_input)
            equations.append((coeff_dict, rhs))
            all_variables.update(coeff_dict.keys())
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Please re-enter the equation.\n")

all_variables = sorted(list(all_variables))

A_list = []
for coeff_dict, rhs in equations:
    row = [coeff_dict.get(var, 0.0) for var in all_variables]
    A_list.append(row)

A = np.array(A_list, dtype=float)
B = np.array([rhs for _, rhs in equations], dtype=float).reshape(-1, 1)

try:
    if np.abs(np.linalg.det(A)) < 1e-10:
        print("\nThe system is singular (no unique solution).")
        print("Determinant is zero.")
        
        rank_A = np.linalg.matrix_rank(A)
        rank_aug = np.linalg.matrix_rank(np.hstack((A, B)))
        print(f"Rank of A: {rank_A}")
        print(f"Rank of [A|B]: {rank_aug}")
        
        if rank_A == rank_aug:
            print("The system has infinitely many solutions.")
        else:
            print("The system is inconsistent (no solution).")
            
    else:
        solution = np.linalg.solve(A, B)
        test = A @ solution
        
        if np.allclose(test, B, atol=1e-8):
            print("\nSolution found successfully!\n")
            for var, val in zip(all_variables, solution.flatten()):
                print(f"{var} = {val:.6f}")
        else:
            print("Sorry! Solution verification failed.")
            
except np.linalg.LinAlgError as e:
    print(f"\nError during solving: {e}")