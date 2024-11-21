# Permission model class representing access rights within a building.
class Permission:
    def __init__(self, id, floorLevel, building):
        """
        Initialize a permission with floor level and building access.
        :param floor_level: Access level (floor)
        :param building: Building in which access is granted
        """
        self.id = id
        self.floorLevel = floorLevel
        self.building = building