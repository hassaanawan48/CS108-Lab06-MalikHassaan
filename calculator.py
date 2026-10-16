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

def main():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /, ^ (power), % (modulus)")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, ^, %): ").strip()
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
    }

    if op not in operations:
        print(f"Invalid operator: '{op}'")
        return

    result = operations[op](num1, num2)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()