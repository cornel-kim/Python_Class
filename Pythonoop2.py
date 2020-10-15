class Parrot:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age

    def Singing(self, song2):
        song = "Jingle bells"
        print('it is singing', song, 'and', song2)
        print('Its name is', self.name)

    def Dances(self):
        print(self.name, 'is dancing')
        print(self.name, 'is', self.age, 'years old')


object = Parrot("Woo", 1.5, "black and yellow")
object.Singing("row row row your bot")
object.Dances()