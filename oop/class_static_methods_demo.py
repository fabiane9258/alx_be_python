class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition without needing class context."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Multiplies two numbers and prints the class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
