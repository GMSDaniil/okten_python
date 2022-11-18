####
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x*self.y + other.x*other.y

    def __sub__(self, other):
        return self.x*self.y - other.x*other.y

    def __eq__(self, other):
        return self.x*self.y == other.x*other.y

    def __ne__(self, other):
        return self.x*self.y != other.x*other.y

    def __lt__(self, other):
        return self.x*self.y < other.x*other.y

    def __gt__(self, other):
        return self.x*self.y > other.x*other.y
# rect1 = Rectangle(1, 2)
# rect2 = Rectangle(3, 4)
# print(rect1 < rect2)

#######


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    count = 0


    @classmethod
    def add_counter(cls):
        cls.count+=1


    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        self.add_counter()


    @classmethod
    def get_count(cls):
        return cls.count

class Prince(Human):

    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find(self, cinderellas:list[Cinderella]):
        for i in cinderellas:
            if i.foot_size == self.shoe_size:
                print(f'Cinderella {i.name} would be perfect for {self.name}')
                return i
        print(f'There is no cinderella for {self.name}')

cinderella1 = Cinderella('Alisa', 22, 36)
cinderella2 = Cinderella('Alena', 21, 37)
cinderella3 = Cinderella('Zhenya', 23, 38)
cinderellas:list[Cinderella] = [cinderella1, cinderella2, cinderella3]
prince = Prince('Max', 25, 37)

#########

from abc import ABC, abstractmethod

class Printable:
    @abstractmethod
    def print(self):
        print(self)


class Book(Printable):
    def __init__(self, name):
        self.name = name


class Magazine(Printable):
    def __init__(self, name):
        self.name = name


class Main(Printable):
    printable_list = []
    @classmethod
    def add(cls, other):
        if isinstance(other, Book) or isinstance(other, Magazine):
            cls.printable_list.append(other)
    @classmethod
    def show_all_magazines(cls):
        for i in cls.printable_list:
            if isinstance(i, Magazine):
                print(i.name, end=' ')
    @classmethod
    def show_all_books(cls):
        for i in cls.printable_list:
            if isinstance(i, Book):
                print(i.name, end=' ')

magazine1 = Magazine('magazine1')
magazine2 = Magazine('magazine2')
book1 = Book('AC')
book2 = Book('Red')
Main.add(magazine1)
Main.add(magazine2)
Main.add(book1)
Main.add(book2)
# Main.show_all_magazines()
# Main.show_all_books()