from typing import List

from location import Location
from pilot import Pilot
from passenger import Passenger
from airplane import Airplane
from flight import Flight

if __name__ == "__main__":
    bielsko = Location(x=10, y=0)
    katowice = Location(x=100, y=100)

    airplane = Airplane(fuel=1000, current_location=bielsko)

    passengers = [Passenger() for _ in range(19)]

    pilot1 = Pilot()
    pilot2 = Pilot()

    flight = Flight(katowice, airplane, passengers=passengers)
    flight.delegate_pilot(pilot1)
    flight.delegate_pilot(pilot2)

    print(flight.take_off())