#classes
#objects
#attributes
#class shapes-Triangle, rectange, square etc. attributes(Lenght, height)
#triangle- attributes(height, lenght, hypoteneus, constant 0.5)

class Parrot:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age

    def singing(self, sing2):
        song = 'jingle bells'
        print('it is singing..', song, 'and', sing2)
        print('its name is', self.name)#behavior accessing attribute

    def dancing(self):
        print(self.name, 'it is dancing')
        print(self.name, 'is', self.age, 'years old')


object = Parrot("Jane", 1, "Yellow-Blue")
#access the behavior
object.singing('row row row your boat')
object.dancing()

