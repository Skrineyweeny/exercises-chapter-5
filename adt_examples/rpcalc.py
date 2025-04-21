from math import sin, cos
from numbers import Number


class RPCalc:
    """Define the Reverse Polish Calculator."""

    def __init__(self):
        """Initialise."""
        self.arguments = []

    def push(self, other):
        """Set up push."""
        a = self.arguments
        if isinstance(other, Number):
            a.append(other)
        else:
            if other == "+":
                i = a.pop()
                j = a.pop()
                a.append(i + j)
            elif other == "-":
                i = a.pop()
                j = a.pop()
                a.append(j - i)
            elif other == "*":
                i = a.pop()
                j = a.pop()
                a.append(i*j)
            elif other == "/":
                i = a.pop()
                j = a.pop()
                a.append(j/i)
            elif other == "sin":
                i = a.pop()
                a.append(sin(i))
            elif other == "cos":
                i = a.pop()
                a.append(cos(i))
            else:
                return NotImplemented

    def pop(self):
        """Get rid of the first element."""
        a = self.arguments
        i = self.arguments[-1]
        a.pop()
        return i

    def peek(self):
        """Check the first element."""
        return self.arguments[-1]

    def __len__(self):
        """Return the length of the list."""
        return len(self.arguments)
