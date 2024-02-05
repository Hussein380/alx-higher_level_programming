#!/usr/bin/python3
"""Define a class MyInt that inherits fromint """


class MyInt(int):
    """invert int operators"""

    def __eq__(self, value):
        """override == operator with != behaaviour """
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == ehaviour """
        return self.real == value
