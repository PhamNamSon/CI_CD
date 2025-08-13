class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass

class Calculator:
    def __init__(self):
        self.memory = None

    def compute(self, op, a, b):
        """Perform basic binary operations."""
        try:
            a = float(a)
            b = float(b)
        except ValueError as e:
            raise CalculatorError("Operands must be numbers.") from e

        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise CalculatorError("Division by zero is not allowed.")
            return a / b
        elif op == '^':
            return a ** b
        else:
            raise CalculatorError(f"Unknown operator: {op}")

    def sqrt(self, x):
        """Square root of x."""
        try:
            x = float(x)
        except ValueError as e:
            raise CalculatorError("Operand must be a number.") from e

        if x < 0:
            raise CalculatorError("Cannot take the square root of a negative number.")
        return x ** 0.5

    def nth_root(self, a, n):
        """n-th root of a."""
        try:
            a = float(a)
            n = float(n)
        except ValueError as e:
            raise CalculatorError("Operands must be numbers.") from e

        if n == 0:
            raise CalculatorError("Root degree cannot be zero.")

        if a < 0:
            # Only allow odd integer roots of negative numbers
            if not n.is_integer() or int(n) % 2 == 0:
                raise CalculatorError("Cannot take even root of a negative number.")

        return a ** (1 / n)
