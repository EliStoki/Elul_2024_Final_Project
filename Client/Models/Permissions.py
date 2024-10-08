class Permission:
    def __init__(self, floor_level, building):
        self.floor_level = floor_level
        self.building = building
        
    def __str__(self):
        return f"Levels: {self.floor_level}, Buildings: {self.building}"