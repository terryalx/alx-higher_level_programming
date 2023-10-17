#!/usr/bin/python3
"""
Child class Rectangle
inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """
    A subclass of class Base
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize instances for class rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Retrive the attribute
        getter function for __width
        Returns: __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting and validating __width
        setter function for __width.
            Args:
                value (int): value to be set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrive __heigh
        getter function for __height
        Returns: __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting and validating __height
        setter function for __height
            Args:
                value (int): value to be set
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieve __x
        getter function for __x
        Return: __x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setting and validating __x
        setter funstion for __x
            Args:
                value (int): value to be set
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieve __y
        getter funstion for __y
        Return: __y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setting and validating __y
        setter funstion fro __y
            Args:
                value (int): value to be set
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Get area of the Rectangle
        width * height
        """
        return (self.__width * self.__height)

    def display(self):
        """
        print # to the stdout
        """
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            for n in range(self.__width + self.__x):
                if n < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        """"
        overriding __str__()
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

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
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        Returns dict representation of a Rectangle
        """
        return {
                "x": self.x,
                "y": self.__y,
                "id": self.id,
                "height": self.__height,
                'width': self.__width,
                }
