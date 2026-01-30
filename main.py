# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


def print_calculations(title, x, y):
    print(f"\n=== {title} ===")
    print(f"Numbers: x = {x}, y = {y}")
    print(f"Addition: {x} + {y} = {add(x, y)}")
    print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
    print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
    print(f"Division: {x} / {y} = {divide(x, y)}")


# Demo usage
print_calculations("Basic Calculator Demo", 10, 3)
print_calculations("Division by Zero Demo", 10, 0)
print_calculations("Additional Examples", 15, 4)
print_calculations("Decimal Examples", 7.5, 2.5)
