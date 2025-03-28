from DA.DataAccess import DataAccess
from models.person import Person

class PersonDA:
    def __init__(self):
        self.api = DataAccess()

    def get_all(self):
        persons = self.api.read("person")
        return [Person(**person) for person in persons]
    
    def get(self, person_id):
        person = self.api.read("person", person_id)
        return Person(**person) if person else None

    def add(self, person : Person):
        data = person.to_dict()
        return self.api.create("person", data)

    def update(self, person : Person):
        data = person.update_to_dict()
        return self.api.update("person", person.id, data)

    def delete(self, person : Person):
        return self.api.delete("person", person.id)