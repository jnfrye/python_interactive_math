"""The base class for all mathematical expressions.
"""


class Math:
    """Base class for mathematical expressions.

    This handles rendering of the input formula (it can be thought of as a
    `\begin{equation}...\end{equation}` block from LaTeX.)
    """
    def __init__(
            self,
            formula: {
                'type': int, 'help': "Formula to be rendered."},
            name: {
                'type': str, 'help': "Name of this expression "
                                     "(for cross-referencing)"}):
        """Instantiate a Math object."""

        self.formula = formula
        self.name = name
