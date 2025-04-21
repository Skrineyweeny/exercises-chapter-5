class Fib:  # NOQA D100
    """The Fibonacci class."""

    def __init__(self):
        """Initialise the Fibonacci class."""
        self.a = 1
        self.b = 1

    def __iter__(self):
        """Iterate."""
        return self

    def __next__(self):
        """Next function."""
        self.a, self.b = self.b, self.a + self.b
        return self.a
