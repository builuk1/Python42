# Інкапсуляція
# Успадкування
# Поліморфізм


# Інкапсуляція

# public - публічний рівень доступу             name
# protected - захищенний рівень доступу         _cover
# private   - приватний рівень доступу          __password


class Mobile:
    __imei = '123'
    __password = 'qw12'
    _color = 'grey'
    _cover = 'silver'
    os = 'Android'
    model = 'Pixel'
    name = 'default'

    def change_imei(self, new_imei):
        self.__imei = new_imei

    def show_imei(self):
        return self.__imei

    def change_color(self, new_color):
        self._color = new_color

    def show_color(self):
        return self._color

    def __change_battery(self, new_battery):
        return f'Battery changed {new_battery}'

    def service_center(self, new_battery):
        return self.__change_battery(new_battery)

    def change_name(self, new_name):
        self.name = new_name

    def show_name(self):
        return self.name


pixel7 = Mobile()
print(pixel7.show_color())
print(pixel7.show_imei())
print(pixel7.show_name())
pixel7.color = 'green'
pixel7.imei = '456'
pixel7.name = 'qwerty'
print(pixel7.show_color())
print(pixel7.show_imei())
print(pixel7.show_name())
print(pixel7._cover)
pixel7._cover = 'black'
print(pixel7._cover)

# Приватний рівень, на пряму не доступний
# print(pixel7.__password)
# pixel7._cover = 'black'
# print(pixel7.__password)

samsung = Mobile()
samsung.change_imei('tyip')
print(samsung.show_imei())

# Приватний рівень, на пряму не доступний
# samsung.__change_battery('123')
print(samsung.service_center('123'))


# Написати 2 методи з методами доступу до них ( один приватний і один захищений)
# Написати 2 поля з методами доступу до них ( один приватний і один захищений)

class Smart_phone:
    __imei = "1234567890"
    __password = "qw12"
    _colour = "grey"
    os = "Androind"
    model = "Pixel"
    _cover = "silver"
    _date = "20.05.2024"
    __designer = "Ivan"
    __change_battery = "1234"

    def change_imei(self, new_imei):
        self.__imei = new_imei

    def show_imei(self):
        return self.__imei

    def change_colour(self, new_colour):
        self._colour = new_colour

    def show_colour(self):
        return self._colour

    def change_model(self, new_model):
        self.model = new_model

    def show_model(self):
        return self.model

    def __change_battery(self, new_battery):
        return f"battery changed {new_battery}"

    def service_centre(self, new_battery):
        return self.__change_battery(new_battery)

    def designer_name(self, new_name):
        self.__designer = new_name

    def show_designer_name(self):
        return self.__designer

    def date_date(self, new_date):
        self._date = new_date

    def show_date(self):
        return self._date

    def _change_camera(self, new_camera):
        return f"camera changed {new_camera}"

    def service_centre2(self, new_camera):
        return self._change_camera(new_camera)

    def __sell_phone(self, new_phone):
        return f"phone changed {new_phone}"

    def seller(self, new_phone):
        return self.__sell_phone(new_phone)


class Kniga:
    __autor = 'Shevchenko'
    _nazva = 'Kobzar'

    def change_autor(self, new_autor):
        self.__autor = new_autor

    def show_autor(self):
        return self.__autor

    def change_nazva(self, new_nazva):
        self._nazva = new_nazva

    def show_nazva(self):
        return self._nazva


biblioteka = Kniga()
biblioteka.__autor = 'Jadan'
biblioteka._nazva = 'Malvi'

print(biblioteka.show_autor())
print(biblioteka.show_nazva())


# Ctrl + Alt + L   Windows    Cmd + Option + L   MacOS

class Mobile:
    imei = '123'
    color = 'grey'
    os = 'Android'
    model = 'Pixel'
    name = 'default'
    _settings = 'installed'
    __photo = 'personal'

    def change_imei(self, new_imei):
        self.imei = new_imei

    def show_imei(self):
        return self.imei

    def change_color(self, new_color):
        self.color = new_color

    def show_color(self):
        return self.color

    def change_name(self, new_name):
        self.name = new_name

    def show_name(self):
        return self.name

    def change_settings(self, new_settings):
        self._settings = new_settings

    def show_settings(self):
        return self._settings

    def change__photo(self, new__photo):
        self.__photo = new__photo

    def show__photo(self):
        return self.__photo


pixel7 = Mobile()
xiaomi = Mobile()
print(pixel7.show_color())
print(pixel7.show_imei())
print(pixel7.show_name())
pixel7.color = 'green'
pixel7.imei = '456'
pixel7.name = 'qwerty'
print(pixel7.show_color())
print(pixel7.show_imei())
print(pixel7.show_name())
print(xiaomi.show_settings())
xiaomi._settings = 'factory setting'
print(xiaomi.show_settings())
print(xiaomi.show__photo)
xiaomi.__photo = 'close'
print(xiaomi.show__photo)


class Mobille:
    __sim = "Vodafone"
    _number = "0952344523"

    def change_number(self, new_number):
        self._number = new_number

    def show_number(self):
        return self._number

    def change_sim(self, new_sim):
        self.__sim = new_sim

    def show_sim(self):
        return self.__sim


samsung = Mobille()
samsung._number = "999999"
samsung.__sim = "Lifesell"
print(samsung.show_number())
print(samsung.show_sim())

class Car:
    __brand = 'Mercedes'
    _model = 'Vito'

    def change_brand(self, new_brand):
        self.__brand = new_brand

    def show_brand(self):
        return self.__brand

    def change_model(self, new_model):
        self._model = new_model

    def show_model(self):
        return self._model


car_showroom = Car()
car_showroom.__brand = 'Ford'
car_showroom._model = 'Transit'

print(car_showroom.show_brand())
print(car_showroom.show_model())