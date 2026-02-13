import random

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
          
class Table:
    def __init__(self, seats: list, capacity: int = 4):
        self.capacity=capacity
        self.seats=seats

    def has_free_spot(self):
        has_free_spot=False
        for seat in self.seats:
            if seat.free:
                has_free_spot=True
                break
        return has_free_spot
            
    def assign_seat(self, name: str):
        seats=[]
        for seat in self.seats:
            if seat.free:
                seats.append(seat)
        random.choice(seats).set_occupant(name)

    def left_capacity(self):
        for seat in self.seats:
            if not seat.free:
                self.capacity-=1
        return self.capacity

            
        
        
