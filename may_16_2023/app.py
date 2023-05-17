# Contact Book:
# Create a contact book application that
# allows users to store and manage their contacts.
# Each contact can have attributes like:
# name, phone number, email, and address.

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f'Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}'


person_1 = Contact('Chris', '315-443-2243',
                   'chris@gmail.com', '123 sesame street')
print(person_1.name)
print(person_1)


# Try to make a decorator
def my_decorator(func):
    def wrapper(*args):
        print('Yup')
        func(*args)
        print('Execution complete')
    return wrapper


@my_decorator
def say_hello(message):
    print(message)


say_hello('Hello world')
