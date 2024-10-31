class Table:  # Клас
    count = 0  # Атрибут класу

    def __init__(self, name):  # Магічний метод, dunder method ( double direction ), службовий метод
        Table.count += 1  # self.count = self.count + 1
        self.name = name  # поле обʼекту класу

    def __str__(self):
        return self.name

    def change_name(self, name):
        self.name = name


wood = Table('redwood')
print(wood.name)
print(wood.count)
stone = Table('redstone')
print(stone.name)
print(stone.count)
print(wood)
print(stone)


# import tkinter
# print(tkinter)

class OrwellMath:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __add__(self, other):
        return self.number + other.number + 1

    def __eq__(self, other):
        if self.number == other.number:
            return "Hello"
        else:
            return "Not"


print(int(2) + int(2))
print(OrwellMath(2) + OrwellMath(2))

print(int(2) == int(2))
print(OrwellMath(2) == OrwellMath(3))

print(bool("False"))
print(bool(""))

'''Завдання 1
Створіть (або використайте раніше створений) клас
«Число». Клас «Число» зберігає всередині одне значення.
Використовуючи перевантаження операторів, реалізуйте для нього арифметичні 
операції для роботи з числом (операції +, -, *, /).'''

print('Завдання 1')


class Number:
    value = 10

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        return self.value / other


print(int(2) + int(2))
print(Number.value + int(2))
print(Number.value * int(3))
print(Number.value / int(2))
print(Number.value - int(2))

print(Number(2) + int(2))
print(Number(3) * int(3))
print(Number(10) / int(2))
print(Number(8) - int(2))


class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value


print(Number(3) + Number(2))
print(Number(3) - Number(2))
print(Number(3) * Number(2))
print(Number(3) / Number(2))


class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num / other.num


print(Number(3) + Number(2))
print(Number(3) - Number(2))
print(Number(3) * Number(2))
print(Number(3) / Number(2))


class NumberM:
    value = 10
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __add__(self, other):
        if hasattr(other, 'value'):
            return self.value + other.value
        else:
            return self.value + other

    def __sub__(self, other):
        if hasattr(other, 'value'):
            return self.value - other.value
        else:
            return self.value - other

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value


print(NumberM(3) + NumberM(2))
print(NumberM(3) + int(4))
print(NumberM(3) - float(4.5))
