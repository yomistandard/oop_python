
class Vehicle:
    def __init__(self,type,movement):
        self.type = type
        self.movement = movement
    
    def move(self):
        return f"{self.type} is {self.movement}"

        