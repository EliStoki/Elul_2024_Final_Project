# Person model class representing a generic person with basic attributes.
class Person:
    def __init__(self, name, age, address):
        """
        Initialize a person with name, age, and address.
        :param name: Name of the person
        :param age: Age of the person
        :param address: Address of the person
        """
        self.name = name
        self.age = age
        self.address = address
