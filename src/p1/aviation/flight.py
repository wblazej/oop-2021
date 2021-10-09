from typing import List
from math import sqrt

from location import Location
from airplane import Airplane
from pilot import Pilot
from passenger import Passenger

class Flight:
    destination: Location
    airplane: Airplane
    pilots: List[Pilot]
    passengers: List[Passenger]

    def __init__(self, destination: Location, airplane: Airplane, 
                pilots: List[Pilot] = [], passengers: List[Passenger] = []):
        self.airplane = airplane
        self.destination = destination
        self.pilots = pilots
        self.passengers = passengers

    def delegate_pilot(self, pilot: Pilot):
        self.pilots.append(pilot)

    def add_passenger(self, passenger: Passenger):
        self.passengers.append(passenger)

    def take_off(self):
        if self.airplane.max_seats < len(self.passengers):
            return "Max seats exceeded"

        if [passenger.ticket for passenger in self.passengers].count(False):
            return "One of passengers doesn't have a ticket"

        if self.airplane.fuel < self.__needed_fuel():
            return "There is not enought fuel"

        for pilot in self.pilots:
            if not pilot.avaliable:
                return "One of delefated pilots is not avaliable"
            pilot.avaliable = False
            pilot.airplane = self.airplane

        return "fiuuu"

    def __needed_fuel(self):
        return self.__distance() * self.airplane.fuel_consumption

    def __distance(self):
        movement_x = abs(self.airplane.current_location.x_location - self.destination.x_location)
        movement_y = abs(self.airplane.current_location.y_location - self.destination.y_location)
        return sqrt(movement_x ** 2 + movement_y ** 2)

    def __repr__(self):
        return f'| Airplane: {self.airplane}; Destination: {self.destination}; Pilots: {self.pilots} |'
