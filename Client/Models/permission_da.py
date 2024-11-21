from DA.DataAccess import DataAccess
from models.permission import Permission

class PermissionDA:
    def __init__(self):
        # Initialize the DataAccess API to interact with the database
        self.api = DataAccess()

    def get_all(self):
        # Retrieve all permissions from the database and convert each to a Permission instance
        permissions = self.api.read("permission")
        return [Permission(**permission) for permission in permissions]

    def get(self, permission_id):
        # Retrieve a specific permission by ID and convert it to a Permission instance
        permission = self.api.read("permission", permission_id)
        return Permission(**permission) if permission else None

    def add(self, permission: Permission):
        # Convert the Permission object to a dictionary and add it to the database
        data = permission.__dict__
        return self.api.create("permission", data)

    def update(self, permission: Permission):
        # Convert the Permission object to a dictionary and update the entry in the database
        data = permission.__dict__
        return self.api.update("permission", permission.id, data)

    def delete(self, permission: Permission):
        # Delete the permission entry in the database using its ID
        return self.api.delete("permission", permission.id)
