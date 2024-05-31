#!/usr/bin/python3
"""
The Mystical Dragon - Mastering Mixins
"""


class SwimMixin:
    """
    class for swimming.
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    class for flying.
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    representing a dragon.
    """

    def roar(self):
        print("The dragon roars!")
