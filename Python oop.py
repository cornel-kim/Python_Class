#mammalia-warm blooded, mammary glands, fur
#man - walks upright, intelligent, omnivorous
#cow - herbivorous, walks on four legs, Has four mammary glands
#the process of acquiring charestics from the upper or top class(mammalia) is through inheritance

# Example2
#shapes - square, rectangle, triangle- calculate area and perimeter- Lenght
#square - lenght squared- area, perimeter lenght x 4
#rectangle- area= lenght time heigh, perimter= lenght x2 plus height x 2
import math


class Shapes:
    def __init__(self, lenght):
        self.length = lenght

    def square(self):
        area = (self.length * self.length)
        perimeter = self.length * 4
        print("The area of a square is", area, "The perimeter is", perimeter)

    def rectangle(self):
        width = 3
        area = (self.length * width)
        perimeter = (self.length * 2) + (width * 2)
        print("The area of a rectangle is", area, "The perimeter is", perimeter)

    def triangle(self):
        height = 5
        area = 0.5 * (self.length * height)
        perimeter = math.sqrt((height * height) + (self.length * self.length)) + self.length + height
        print("The area of a triangle is", area, "The perimeter is", perimeter)


x = Shapes(lenght=4)
x.square()
x.rectangle()
x.triangle()
