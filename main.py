class BasicCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        if self.y == 0:
            return "Cannot divide by zero"
        return self.x / self.y

    def print_results(self, title):
        print(f"\n=== {title} ===")
        print(f"Numbers: x = {self.x}, y = {self.y}")
        print(f"Addition: {self.x} + {self.y} = {self.add()}")
        print(f"Subtraction: {self.x} - {self.y} = {self.subtract()}")
        print(f"Multiplication: {self.x} * {self.y} = {self.multiply()}")
        print(f"Division: {self.x} / {self.y} = {self.divide()}")


# Demo usage
calc1 = BasicCalculator(10, 3)
calc1.print_results("Basic Calculator Demo")

calc2 = BasicCalculator(10, 0)
calc2.print_results("Division by Zero Demo")

calc3 = BasicCalculator(15, 4)
calc3.print_results("Additional Examples")

calc4 = BasicCalculator(7.5, 2.5)
calc4.print_results("Decimal Examples")
