from location import Location

class Airplane:
    fuel: int
    current_location: Location
    max_seats: int
    fuel_consumption: int
    
    def __init__(self, fuel: int, current_location: Location, max_seats: int = 20, fuel_consumption: int = 5):
        self.fuel = fuel
        self.current_location = current_location
        self.max_seats = max_seats
        self.fuel_consumption = fuel_consumption

    def __repr__(self):
        return f'| Fuel: {self.fuel}; Current location: {self.current_location}; Max seats: {self.max_seats} |'