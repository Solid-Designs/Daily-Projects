from abc import ABC, abstractmethod

# class Product:
#     def __init__(self, price):
#         self.price(price)

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError('Price cannot be lower than 0')
#         else:
#             self.__price = value


# product = Product(10)

# print(product.price)
# class Animal:
#     def __init__(self):
#         print('Animal Constructor')
#         self.age = 1

#     def eat(self):
#         print('eat')


# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print('Mammal Constructor')
#         self.weight = 2

#     def walk(self):
#         print('walk')


# class Fish(Animal):
#     def swim(self):
#         print('swim')


# class Bird(Animal):
#     def fly(self):
#         print('fly')


# class Chicken(Bird):
#     pass


# m = Mammal()
# print(m.age)


# class Flyer:
#     def fly(self):
#         print('Fly')


# class Swimmer:
#     def swim(self):
#         print('swim')


# class FlyingFish(Flyer, Swimmer):
#     pass
class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed')
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('Reading data from a file')


class NetworkStream(Stream):
    def read(self):
        print('Reading data from a network')


stream = FileStream()
stream.open()
