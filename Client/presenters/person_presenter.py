from models.person import Person
from presenters.main_window_presenter import MainWindowPresenter
from models.person_da import PersonDA
class PersonPresenter:
    def __init__(self, model : PersonDA, list_view, add_edit_view, main_window_presenter : MainWindowPresenter):
        self.model = model
        self.list_view = list_view
        self.add_edit_view = add_edit_view
        self.main_window_presenter = main_window_presenter
        
        # Set presenter for views
        self.list_view.set_presenter(self)
        self.add_edit_view.set_presenter(self)
        
        # Load initial data
        self.load_data()

    def load_data(self):
        self.list_view.clear()
        for person in self.model.get_all():
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
        
        self.main_window_presenter.load_panel(self.add_edit_view)

    def save_person(self, id, name, age, address):
        try:
            person = Person(id=int(id), name=name, age=int(age), address=address)
        except ValueError as e:
            print(f"Error converting age or id to integer: {e}")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        self.model.add(person)
        self.load_data()
        self.main_window_presenter.load_panel(self.list_view)

    def delete_person(self, person):
        self.model.remove(person)
        self.load_data()
