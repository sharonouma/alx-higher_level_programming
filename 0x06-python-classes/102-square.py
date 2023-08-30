#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a size.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the current area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Checks if two squares have equal areas.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        Checks if two squares have unequal areas.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Checks if the area of the current square is > the other square.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Checks if the area of the current square is >= to the other square.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Checks if the area of the current square is < the other square.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Checks if the area of the current square is <= to the other square.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
