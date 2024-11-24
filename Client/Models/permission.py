# Permission model class representing access rights within a building.
class Permission:
    def __init__(self, id, floorLevel, building):
        self.id = id
        self.floorLevel = floorLevel
        self.building = building

    def to_dict(self):
        return {
            "id": self.id,
            "floorLevel": self.floorLevel,
            "building": self.building
        }