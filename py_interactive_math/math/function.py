"""Base class for mathematical functions."""


class Function:
    """Base class for mathematical functions."""
    content_mathml_tag = ""
    "Corresponding content-MathML tag text."

    def __init__(
            self,
            *args: "Arbitrary number of function arguments"):
        self.args = args
