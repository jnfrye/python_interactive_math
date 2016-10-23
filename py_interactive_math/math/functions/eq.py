"""Equality function."""

from ..function import Function


class Eq(Function):
    """Equality (=) function."""
    content_mathml_tag = "eq"

    def __init__(self, *args):
        super().__init__(*args)
