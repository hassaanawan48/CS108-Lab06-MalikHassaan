import math

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b, handling division by zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def modulus(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

def square_root(a, b=None):
    """Return the square root of a. Second argument is ignored."""
    if a < 0:
        return "Error: Cannot take square root of a negative number"
    return math.sqrt(a)

def percentage(a, b):
    """Return what percent a is of b."""
    if b == 0:
        return "Error: Cannot compute percentage with zero base"
    return (a / b) * 100

def main():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /, ^ (power), % (modulus), sqrt, pct")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, ^, %, sqrt, pct): ").strip().lower()
        if op in ("sqrt",):
            num2 = 0  # not needed
        else:
            num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "^": power,
        "%": modulus,
        "sqrt": square_root,
        "pct": percentage,
    }

    if op not in operations:
        print(f"Invalid operator: '{op}'")
        return

    result = operations[op](num1, num2)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()