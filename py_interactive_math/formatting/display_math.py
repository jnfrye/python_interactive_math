"""The base class for displaying mathematical expressions.
"""

from ..math.formula import Formula


class DisplayMath:
    """Base class for displaying mathematical expressions.

    This handles rendering of the input formula (it can be thought of as a
    `\begin{equation}...\end{equation}` block from LaTeX.)
    """
    def __init__(
            self,
            formula: {
                'type': Formula, 'help': "Formula to be rendered."},
            name: {
                'type': str, 'help': "Name of this expression "
                                     "(for cross-referencing)"}):
        """Instantiate an object of this class."""

        self.formula = formula
        self.name = name
