#!/usr/bin/python3
import math


"""
MagicClass class definition
"""


class MagicClass:
    """
    A class that represents a magic circle with a given radius.

    Attributes:
        __radius (float): The radius of the magic circle.

    Methods:
        __init__(self, radius=0): Initializes a new instance of the
                                MagicClass.
        area(self): Calculates and returns the area of the magic circle.
        circumference(self): Calculates and returns the circumference
                            of the magic circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass.

        Args:
            radius (float): The radius of the magic circle.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculates and returns the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
