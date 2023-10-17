#!/usr/bin/python3
"""
Write a child class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A subclass of class Rectangle
    args:
        size: size
        x: position
        y: position
        id: id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Returns a string representation of a square instance
        Prints [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Retrieve attribute from class Rectangle
        getter function for width
        Returns: width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        validation from class Rectangle
        width and the height - with the same value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns key/value argument to attributes
        kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        Returns dict representation of a Rectangle
        """
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y,
                }
