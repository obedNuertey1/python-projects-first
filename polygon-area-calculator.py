class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'
    
