# Успадкування

class Human:
    name = 'John'
    surname = 'Doe'
    age = 30

    def eat(self):
        return 'I am eating!'

    def speak(self):
        return 'I am speaking!'


class Builder(Human):
    name = 'Default'

    def speak(self):
        return 'I am a builder!'

    def builder(self):
        return 'Build!'


class Sailor(Human):
    name = 'Jack'

    def speak(self):
        return 'I am a sailor!'

    def smoking(self):
        return 'Bad idea!'


class SeaBuilder(Builder, Sailor):
    pass


john = Human()
print(john.name)
print(john.eat())

bender = Builder()
print(bender.name)
print(bender.speak())
print(bender.builder())

papay = Sailor()
print(papay.name)
print(papay.speak())
print(papay.smoking())

# Ще одну професію з 2 методами та 2 полями

# На основі цієї професії зробити 2 суміжні ( з Builder  Sailor)

seal = SeaBuilder()
print(seal.name)
seal.builder()


class Human:
    name = "Snoop"
    surname = "Dog"
    age = 30

    def eat(self):
        return "eatening burger"

    def speak(self):
        return "speaking with friend"


class Builder(Human):
    def speak(self):
        return "speaking with friend"

    def builder(self):
        return "building house"


class Sailor(Human):
    name = "JAck"
    age = 25

    def smoke(self):
        return "smoking cuigar"

    def coffe_time(self):
        return "drink coffe"


class Racer(Human):
    def drive(self):
        return "driving car"

    def checking_car(self):
        return "checking car"


class SeaBuilder(Builder, Sailor):
    pass


class RaceBuilder(Builder, Racer):
    pass


class RaceSailor(Sailor, Racer):
    pass


snoop = Human()
print(snoop.name)
print(snoop.age)
print(snoop.eat())

bender = Builder()
print(bender.builder())

seal = SeaBuilder()
print(seal.name)
seal.builder()

racer_onbuilding = RaceBuilder()
racer_onship = RaceSailor()

print(racer_onbuilding.drive())
print(racer_onship.checking_car())


class Football_player(Human):
    club = 'Chornomorets'
    position = 'The attacker'

    def years(self):
        return 25

    def city(self):
        return 'Odesa'


class Manager(Builder, Football_player):
    pass


class BeachGuard(Sailor, Football_player):
    pass


football = Football_player()
print(football.name)
print(football.years())
print(football.city())
print(football.speak())


class Designer(Human):
    position = 'Designer'
    workPlace = 'Office'

    def to_design(self):
        return 'general design'

    def to_description_education(self):
        return 'general design'


class VesselDesigner(Sailor, Designer):
    position = 'Vessel Designer'
    workPlace = 'Sea dock'

    def to_design(self):
        return 'vessel design'

    def to_description_education(self):
        return 'sea design'


class BuildDesigner(Builder, Designer):
    position = 'Building Designer'
    workPlace = 'building site'

    def to_design(self):
        return 'design of building'

    def to_description_education(self):
        return 'Constraction of building'


class SeaBuilder(Builder, Sailor):
    pass


jack_D = Designer()
print(jack_D.name)
print(jack_D.position)
print(jack_D.workPlace)
print(jack_D.to_design())
print(jack_D.to_description_education())

jack_VD = VesselDesigner()
print(jack_VD.name)
print(jack_VD.position)
print(jack_VD.workPlace)
print(jack_VD.to_design())
print(jack_VD.to_description_education())

jack_BD = VesselDesigner()
print(jack_BD.name)
print(jack_BD.position)
print(jack_BD.workPlace)
print(jack_BD.to_design())
print(jack_BD.to_description_education())


class Trucker(Human):

    def drive(self):
        return "I am driving"

    def buyOil(self):
        return "I buy oil"


class firstTrucker(Trucker, Sailor):
    pass


class secondTrucker(Trucker, Builder):
    pass


first = firstTrucker()

second = secondTrucker()

print(first.drive())

print(second.buyOil())


class Human:
    name = 'John'
    surname = 'Doe'
    age = 30

    def eat(self):
        return 'I am eating!'

    def speak(self):
        return 'I am speaking!'


class Builder(Human):
    name = 'Default'

    def speak(self):
        return 'I am a builder!'

    def builder(self):
        return 'Build!'


class Sailor(Human):
    name = 'Jack'

    def speak(self):
        return 'I am a sailor!'

    def smoking(self):
        return 'Bad idea!'


class SeaBuilder(Builder, Sailor):
    pass


class Welder(Human):
    name = 'Slavik'
    age = 45

    def speak(self):
        return 'I am a welder!'

    def working(self):
        return 'I weld pipes on deck'


class Mechanic(Welder, Sailor):
    def repairing(self):
        return 'I am repairing a lift'


class Electron(Builder, Welder):
    def work(self):
        return 'I am soldering the wiring'


john = Human()
print(john.name)
print(john.eat())

bender = Builder()
print(bender.name)
print(bender.speak())
print(bender.builder())

papay = Sailor()
print(papay.name)
print(papay.speak())
print(papay.smoking())

slv = Welder()
print(slv.name)
print(slv.speak())
print(slv.working())

mex = Mechanic()
print(mex.repairing())
print(mex.speak())
print(mex.working())
el = Electron()
print(el.work())
print(el.speak())

# Ще одну професію з 2 методами та 2 полями

# На основі цієї професії зробити 2 суміжні ( з Builder  Sailor)

seal = SeaBuilder()
print(seal.name)
seal.builder()


class Human:
    name = 'John'
    surbname = 'Doe'
    age = 30

    def eat(self):
        return 'I am eating'

    def speak(self):
        return 'I am speaking'


class Builder(Human):
    def builder(self):
        return 'I am builder'


class Sailor(Human):
    name = 'Jack'

    def speak(self):
        return ('I am sailor')

    def smoking(self):
        return 'Bad idea!'


class SeaBuilder(Builder, Sailor):
    pass


class Football_player(Human):
    club = 'Chornomorets'
    position = 'The attacker'

    def years(self):
        return 25

    def city(self):
        return 'Odesa'


class Manager(Builder, Football_player):
    pass


class Coach(Sailor, Football_player):
    pass


john = Human()
print(john.name)
print(john.eat())

bender = Builder()
print(bender.name)
print(bender.speak())
print(bender.builder())

papay = Sailor()
print(papay.name)
print(papay.speak())
print(papay.smoking())

seal = SeaBuilder()
print(seal.name)
seal.builder()

football = Football_player()
print(football.name)
print(football.years())
print(football.city())
print(football.speak())


class Chef(Human):
    def speak(self):
        return 'I am a сhef.'

    def cooking(self):
        return 'Сooking.'


class SeaBuilder(Builder, Sailor):
    pass


class ChefSea(Chef, Sailor):
    pass


class BuilderChef(Builder, Chef):
    pass


john = Human()
print(john.name)
print(john.eat())

bender = Builder()
print(bender.name)
print(bender.speak())
print(bender.builder())

papay = Sailor()
print(papay.name)
print(papay.speak())
print(papay.smoking())

seal = SeaBuilder()
print(seal.name)
seal.builder()

chef1 = ChefSea()
print(chef1.name)
chef1.cooking()

chef2 = BuilderChef()
chef1.speak()

print(ord('С'))  # 1057
print(ord('C'))  # 67


class Builder(Human):
    name = "Default"

    def speak(self):
        return "I am a builder"

    def builder(self):
        return "I am a builder"


class Sailor(Human):
    name = "Jack"

    def speak(self):
        return "I am a sailor"

    def smoking(self):
        return "Bad idea"


class Trucker(Human):
    def drive(self):
        return "I am driving"

    def buyOil(self):
        return "I buy oil"


class firstTrucker(Builder, Trucker):
    pass


class secondTrucker(Sailor, Trucker):
    pass


first = firstTrucker()
second = secondTrucker()

print(first.drive())
print(second.buyOil())
print(second.smoking())
print(first.name)


# DRY

# DON'T
# REPEATE
# YOURSELF

# KISS

# KEEP
# IT
# SIMPLE
# STUPIED


class Money:
    currency = 'default'
    banknotes = 'paper'
    coins = 'copper'
    change_rate = ''
    count = 10.5


class USADollar(Money):
    currency = 'USD'
    banknotes = 'bucks'
    coins = 'nickel'


class Product(Money):
    price = 10

    def discount(self, add_discount):
        self.price -= add_discount
