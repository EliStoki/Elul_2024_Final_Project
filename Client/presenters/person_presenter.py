from models.person import Person

class PersonPresenter:
    def __init__(self, model, list_view, add_edit_view):
        self.model = model
        self.list_view = list_view
        self.add_edit_view = add_edit_view
        
        # Set presenter for views
        self.list_view.set_presenter(self)
        self.add_edit_view.set_presenter(self)
        
        # Load initial data
        self.load_data()

    def load_data(self):
        self.list_view.person_list.clear()
        for person in self.model:
            self.list_view.add_item(person)

    def open_add_edit_view(self, person=None):
        if person:
            self.add_edit_view.name_input.setText(person.name)
            self.add_edit_view.age_input.setText(str(person.age))
            self.add_edit_view.address_input.setText(person.address)
        else:
            self.add_edit_view.name_input.clear()
            self.add_edit_view.age_input.clear()
            self.add_edit_view.address_input.clear()
        self.add_edit_view.show()

    def save_person(self, name, age, address):
        try:
            person = Person(name=name, age=int(age), address=address)
        except ValueError as e:
            print(f"Error converting age to integer: {e}")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        self.model.append(person)
        self.load_data()
        self.add_edit_view.hide()

    def delete_person(self, person):
        self.model.remove(person)
        self.load_data()
