class shapes:#primary class
    def __init__(self, height, lenght):
        self.height = height
        self.lenght = lenght

    def square(self):#secondary classes inheriting from the primary class
        print('area of a square is', self.height * self.lenght)

    def triangle(self):
        const = 0.5
        print('area of a triangle', const * self.lenght*self.height)


x = shapes(height=2, lenght=3)
x.square()
x.triangle()