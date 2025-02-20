class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        area = self.height * self.width
        return area
    
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** 0.5)
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or (self.height > 50):
            return 'Too big for picture.'

        line = ('*' * self.width) + '\n'
        shape = ''
        for i in range(0, self.height):
            shape += line
        return shape
    
    def get_amount_inside(self, shape):
        if isinstance(shape, Rectangle) != isinstance(self, Rectangle):
            return NotImplemented
        
        return self.get_area() // shape.get_area()
      


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
    
    def __str__(self):
        return f'{self.__class__.__name__}(side={self.side})'
    
    def set_side(self, side):
            self.side, self.height, self.width = [side]*3
        
    def set_height(self, height):
        self.side, self.height, self.width  = [height] * 3
    
    def set_width(self, width):
        self.side, self.height, self.width = [width] * 3
    