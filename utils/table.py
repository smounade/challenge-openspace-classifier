class Seat:
    def __init__(self, free: bool, occupant: str = None):
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name: str) -> None:
        if self.free:
            self.occupant = name
            self.free = False
        else:
            raise Exception("Someone is already sitting here")

    def remove_occupant(self) -> str:
        if not self.free:
            return_value=self.occupant
            self.occupant = None
            self.free = True
            return return_value
        else:
            raise Exception("This seat is free")
          
