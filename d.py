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
    def __init__(self, l):
        self.a = l[0]
        self.b = l[1]
        self.result = None

    def __get__(self, owner, instance):
        self.result = self.a * self.b
        return f'{self.result}'

    def __set__(self, owner, l):
        self.a = l[0]
        self.b = l[1]
        self.result = self.a * self.b


class Some:
    room = Square([5, 6])
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
a.room = [5,8]
print(a.room)


a = [5,8]