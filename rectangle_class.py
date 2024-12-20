class Rectangle:
    def __init__(self, lenght: int, width: int, areas = 0, perimeters = 0):
        self.lenght = lenght
        self.width = width
        self.areas = areas
        self.perimeters = perimeters

    @property
    def lenght(self):
        return self.__lenght
    
    @lenght.setter
    def lenght(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Invalid type")
        if value < 1:
            raise ValueError("Invalid value")
        self.__lenght = value

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Invalid type")
        if value < 1:
            raise ValueError("Invalid value")
        self.__width = value

    def area(self):
        if self.lenght < 1 or self.width < 1:
            raise ValueError("Incorrect value")
        self.areas = self.lenght * self.width
        return self.areas

    def perimeter(self):
        if self.lenght < 1 or self.width < 1:
            raise ValueError("Incorrect value")
        self.perimeters = 2 * self.lenght + 2 * self.width
        return self.perimeters

rect = Rectangle(4, 5)
print(rect.area())
print(rect.perimeter()) 