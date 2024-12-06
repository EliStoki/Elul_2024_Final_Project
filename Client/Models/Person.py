# Person model class representing a generic person with basic attributes.
class Person:
    def __init__(self, id, name, age, address):
        """
        Initialize a person with name, age, and address.
        :param id: Unique ID for the person
        :param name: Name of the person
        :param age: Age of the person
        :param address: Address of the person
        """
        self.id = id
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f"Person(id={self.id}, name='{self.name}', age={self.age}, address='{self.address}')"
    
    def to_dict(self):
        """
        Convert the person object to a dictionary.
        :return: A dictionary containing the person's attributes
        """
        return {
            "Name": self.name,
            "Age": self.age,
            "Address": self.address
        }
    
    def update_to_dict(self):
        """
        Convert the person object to a dictionary.
        :return: A dictionary containing the person's attributes
        """
        return {
            "ID": self.id,
            "Name": self.name,
            "Age": self.age,
            "Address": self.address
        }
