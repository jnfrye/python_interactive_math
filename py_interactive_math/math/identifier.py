"""Base class for identifiers"""


class Identifier:
    """Base class for identifiers"""
    def __init__(
            self,
            name,
            symbol=name):
        self.name = name
        self.symbol = symbol
