class Animal:
    hungry = 100

    def __init__(self, name):
        self.name = name

    def eat(self, value):
        self.hungry += int(value)


class FruitOfEggs:
    amount_eggs = 5

    def get_eggs(self):
        if self.amount_eggs >= 0:
            self.amount_eggs -= 1
            return 1


class FruitOfMilk:
    amount_milk = 100

    def get_milk(self):
        if self.amount_milk >= 10:
            self.amount_milk -= 10
            return 10


class Goose(Animal, FruitOfEggs):

    @staticmethod
    def vote():
        return 'Goose vote'


class Cow(Animal, FruitOfMilk):

    @staticmethod
    def vote():
        return 'Cow vote'


class Sheep(Animal):
    trimmed = False

    def shave(self):
        if not self.trimmed:
            self.trimmed = True
            return 'Шерсть'

    @staticmethod
    def vote():
        return 'Sheep Vote'


class Chicken(Animal, FruitOfEggs):

    @staticmethod
    def vote():
        return 'Chicken vote!'


class Goat(Animal, FruitOfEggs, FruitOfMilk):

    @staticmethod
    def vote():
        return 'Goat vote'


class Duck(Animal, FruitOfEggs):

    @staticmethod
    def vote():
        return 'Duck vote'


goose_gray = Goose('Gray')
goose_white = Goose('White')
cow_manyka = Cow('Manyka')
sheep_barash = Sheep('Barash')
sheep_kudr = Sheep('Kudr')
chicken_koko = Chicken('Koko')
chiken_kukareku = Chicken('Kukareku')
goat_roga = Goat('Roga')
goat_kopito = Goat('Kopito')
duck_kryakva = Duck('Kryakva')

animals_farm = [goose_gray, goose_white, cow_manyka, sheep_barash, sheep_kudr, chicken_koko,
                chiken_kukareku, goat_roga, goat_kopito, duck_kryakva]

animal_milk = [cow_manyka, goat_kopito, goat_roga]
animal_wool = [sheep_kudr, sheep_barash]

animal_eggs = [chiken_kukareku, chicken_koko, duck_kryakva, goose_white, goose_gray]


def spend_day():
    for animal in animals_farm:
        animal.eat(5)

        if animal in animal_milk:
            animal.get_milk()
        if animal in animal_wool:
            animal.shave()
        if animal in animal_eggs:
            animal.get_eggs()


spend_day()