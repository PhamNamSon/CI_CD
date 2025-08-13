import sys
from calculator.core import Calculator, CalculatorError

class CalculatorCLI:
    def __init__(self):
        self.calc = Calculator()

    def start_repl(self):
        print("Basic Calculator. Type 'help' for commands, 'exit' to quit.")
        while True:
            try:
                expr = input("> ").strip()
                if not expr:
                    continue
                if expr.lower() in ("exit", "quit"):
                    print("Goodbye!")
                    break
                if expr.lower() == "help":
                    self.show_help()
                    continue
                self.run_once(expr)  # Run one expression
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break

    def run_once(self, expr):
        try:
            op_type, args = self.parse(expr)
            if op_type == "binary":
                result = self.calc.compute(args[1], args[0], args[2])
            elif op_type == "sqrt":
                result = self.calc.sqrt(args[0])
            elif op_type == "nth_root":
                result = self.calc.nth_root(args[0], args[1])
            else:
                raise CalculatorError("Unknown operation.")
            print(result)
        except CalculatorError as e:
            print(f"error: {e}")
        except ValueError:
            print("error: Invalid number format.")

    def parse(self, expr):
        expr = expr.strip()
        if expr.startswith("root"):
            if not expr.endswith(")"):
                raise CalculatorError("Invalid root syntax.")
            inside = expr[5:-1]  # remove 'root(' and ')'
            parts = [p.strip() for p in inside.split(",")]
            if len(parts) == 1:
                return "sqrt", [parts[0]]
            elif len(parts) == 2:
                return "nth_root", [parts[0], parts[1]]
            else:
                raise CalculatorError("Root takes 1 or 2 arguments.")
        else:
            for op in ["+", "-", "*", "/", "^"]:
                if op in expr:
                    a, b = expr.split(op, 1)
                    return "binary", [a.strip(), op, b.strip()]
            raise CalculatorError("Invalid expression.")

    def show_help(self):
        print("""Available commands:
NUMBER OP NUMBER      e.g. 3 + 9, 5 * 2, 2 ^ 10
root(X)               square root of X, e.g. root(4)
root(X, N)            N-th root of X, e.g. root(27, 3)
help                  show this message
exit / quit           quit the calculator""")

if __name__ == "__main__":
    cli = CalculatorCLI()
    if len(sys.argv) > 1:
        cli.run_once(sys.argv[1])
    else:
        cli.start_repl()
