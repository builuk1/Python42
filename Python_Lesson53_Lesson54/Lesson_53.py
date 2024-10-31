# Поліморфізм

class Grinder:
    __id = 0
    name = 'none'

    def start(self, products):  # поліморфний метод
        self.products = products
        if self.products == 'meat':
            return 'mince'
        elif self.products == 'branch':
            return 'sawdust'
        else:
            return f'grinded {self.products}'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if Grinder.name == 'default':
            self.__id = id
        else:
            self.__id = 1

    @id.deleter
    def id(self):
        return self.__id


some_grinder = Grinder()
print(some_grinder.start('coffee'))
print(some_grinder.start('meat'))
print(some_grinder.start('branch'))
print(some_grinder.id)
some_grinder.id = 2
print(some_grinder.id)


class Mobile:
    __imei = "123"
    country = "China1"

    @property
    def id(self):
        return self.__imei

    @id.setter
    def id(self, id):
        if Mobile.country == "China":
            self.__imei = id
        else:
            self.__imei = 3856

    @id.deleter
    def id(self):
        return self.__imei


some_mobile = Mobile()
print(some_mobile.id)
some_mobile.id = 200
print(some_mobile.id)


class Mobile:
    __imei = '123'
    __password = "qw12"
    color = 'grey'
    os = 'Android'
    model = 'Pixel'
    name = 'default1'
    _cover = "Silver"
    sim = "Vodafone"
    __number = "0952344523"

    @property
    def imei(self):
        return self.__imei

    @imei.setter
    def imei(self, imei):
        if Mobile.name == 'default':
            self.__imei = imei
        else:
            self.__imei = 1

    @imei.deleter
    def imei(self):
        return self.__imei


some_mobile = Mobile()
print(some_mobile.imei)
some_mobile.imei = 200
print(some_mobile.imei)


class Mobile:
    __imei = '123'
    code = 'private'

    @property
    def imei(self):
        return self.__imei

    @imei.setter
    def imei(self, imei):
        if Mobile.code == 'private':
            self.__imei = imei
        else:
            self.__imei = '457'

    @imei.deleter
    def imei(self):
        return self.__imei


mob = Mobile()
print(mob.imei)
mob.imei = 458
print(mob.imei)


class Mobile:
    __imei = "987654"
    color = 'Red1'

    @property
    def id(self):
        return self.__imei

    @id.setter
    def id(self, id):
        if Mobile.color == 'Red':
            self.__imei = id
        else:
            self.__imei = 2024


some_mobile = Mobile()

print(some_mobile.id)
some_mobile.id = 987654
print(some_mobile.id)


class Mobile:
    __imei = '123'
    color = 'grey'
    os = 'Android'
    model = 'Pixel'
    name = 'default5'

    @property
    def imei(self):
        return self.__imei

    @imei.setter
    def imei(self, imei):
        if Mobile.name == 'default':
            self.__imei = imei
        else:
            self.__imei = 1

    @imei.deleter
    def imei(self):
        return self.__imei


some_mobile = Mobile()
print(some_mobile.imei)
some_mobile.imei = "235"
print(some_mobile.imei)




#
# class Table:  # Клас
#     count = 0  # Атрибут класу
#
#     def __init__(self, name):  # Магічний метод, dunder method ( double direction ), службовий метод
#         Table.count += 1  # self.count = self.count + 1
#         self.name = name # поле обʼекту класу
#
#     def change_name(self, name):
#         self.name = name
#
# wood = Table('redwood')
# print(wood.name)
# print(wood.count)
# stone = Table('redstone')
# print(stone.name)
# print(stone.count)
#
