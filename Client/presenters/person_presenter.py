from models.person import Person
from presenters.main_window_presenter import MainWindowPresenter
from models.person_da import PersonDA

class PersonPresenter:
    def __init__(self, model: PersonDA, list_view, add_view, edit_view, main_window_presenter: MainWindowPresenter):
        self.model = model
        self.list_view = list_view
        self.add_view = add_view
        self.edit_view = edit_view
        self.main_window_presenter = main_window_presenter

        # Set presenter for views
        self.list_view.set_presenter(self)
        self.add_view.set_presenter(self)
        self.edit_view.set_presenter(self)

        # Load initial data
        self.load_data()

    def load_data(self):
        """Load data into the list view."""
        self.list_view.clear()
        for person in self.model.get_all():
            self.list_view.add_item(person)

    def open_add_view(self):
        """Prepare and display the Add View."""
        self.add_view.name_input.clear()
        self.add_view.age_input.clear()
        self.add_view.address_input.clear()
        self.main_window_presenter.load_panel(self.add_view)

    def open_edit_view(self, person: Person):
        """Prepare and display the Edit View with the selected person's data."""
        self.edit_view.edited_person = person.id
        self.edit_view.name_input.setText(person.name)
        self.edit_view.age_input.setText(str(person.age))
        self.edit_view.address_input.setText(person.address)
        self.main_window_presenter.load_panel(self.edit_view)

    def add_person(self, id, name, age, address):
        """Add a new person."""
        try:
            person = Person(id=int(id), name=name, age=int(age), address=address)
            self.model.add(person)
        except ValueError as e:
            print(f"Error converting age to integer: {e}")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        self.load_data()
        self.main_window_presenter.load_panel(self.list_view)

    def update_person(self, id, name, age, address):
        """Update an existing person."""
        try:
            person = Person(id=int(id), name=name, age=int(age), address=address)
            self.model.update(person)
        except ValueError as e:
            print(f"Error converting age or ID to integer: {e}")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        self.load_data()
        self.main_window_presenter.load_panel(self.list_view)

    def delete_person(self, person):
        """Delete the selected person."""
        self.model.delete(person)
        self.load_data()

    def open_list_view(self):
        """Display the list view."""
        self.main_window_presenter.load_panel(self.list_view)
