#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a size and position.
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Returns the current area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        output = ""
        if self.size == 0:
            return output

        for _ in range(self.position[1]):
            output += "\n"

        for _ in range(self.size):
            output += " " * self.position[0] + "#" * self.size + "\n"

        return output.rstrip()
