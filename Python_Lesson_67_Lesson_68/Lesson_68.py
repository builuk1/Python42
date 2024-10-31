# GitHub


# class Some:
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return str(self.value)
#
# a = Some('Hello')
# print(a)

############
class Adder:
    def __init__(self, value):
        self.value = value

    def __get__(self, owner, instance):
        return f'{self.value}'

    def __set__(self, owner, value):
        self.value = value

    def something(self):
        print(self.value)


class Square:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def __get__(self, owner, instance):
        self.result = self.a + self.b
        return f'{self.result}'

    def __set__(self, owner, a, b):
        self.a = a
        self.b = b
        self.result = self.a * self.b


class Some:
    room = Square(5, 5)
    sad = Adder('Hello')

    def __init__(self, value):
        self.value = value
        self.add = Adder(self.value)

    def __str__(self):
        return str(self.value)

    def show(self):
        return self.add


a = Some('Hello')
print(a)
# print(a.add)
print(a.sad)
a.sad = 'World'
print(a.sad)
print(a.room)

s = Adder('abc')
s.something()

'''Завдання 1: Дескриптор для кешування результату методу
Створіть дескриптор, який кешує результат виклику методу
класу. Кеш має бути валідним тільки під час одного запуску
інстанції класу і має очищатися
при кожному новому створенні інстанції класу.'''


class CachedMethodDescriptor:
    def __init__(self, method):
        self.method = method
        self.cache = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self.method
        # Якщо результат ще не кешовано для цієї інстанції, викликаємо метод і кешуємо результат
        if instance not in self.cache:
            self.cache[instance] = self.method(instance)
        return self.cache[instance]

    def clear_cache(self, instance):
        # Видаляє кеш для певної інстанції
        if instance in self.cache:
            del self.cache[instance]


class MyClass:
    def __init__(self, value):
        self.value = value
        # Очищаємо кеш кожного разу, коли створюється нова інстанція
        if hasattr(self.__class__.compute_square, 'clear_cache'):
            self.__class__.compute_square.clear_cache(self)

    # Створюємо атрибут, який використовує наш дескриптор
    compute_square = CachedMethodDescriptor(lambda self: self.value ** 2)


# Приклад використання
obj1 = MyClass(3)
print(obj1.compute_square)  # Викликає метод і кешує результат
print(obj1.compute_square)  # Використовує кешований результат

obj2 = MyClass(4)
print(obj2.compute_square)  # Викликає метод і кешує результат для нової інстанції
