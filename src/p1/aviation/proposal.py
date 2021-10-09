import collections
from typing import List
from abc import abstractmethod, ABC


# almosta a "marker interface"


class Flyable(ABC):
    km_flown: int


class Location(Flyable):
    lon: float
    lat: float


class AirEngine(Flyable):
    pass


class Airplane(Flyable):
    id: int
    type: int
    km_flown: int
    pilot1: 'Pilot'
    pilot2: 'Pilot'
    passengers: List['Passenger']  # collections.Iterable
    __fuel: float
    engine: AirEngine

    __location: Location

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, loc: Location):
        print('setting location')
        self.__location = loc

    def __init__(self):
        self.__fux = 0

    # embark pilot (must have proper training, https://ame.aircharterservices.com/)
    # embark passengers (airplane capacity)
    # disembark certain passenger (by id)
    # ATC for flights (ATC shifts airplane position, not sb. else; or pilot? or Airline? or AirspaceSimulator?)
    # Airport (airport provides fuel to Airplane); plane.refuel_by(airport), or airport.refuel(plane)
    #
    # actions that can destroy guaranteed correctness of program (simulator)
    # plane.location = (0,90) ... yeah... teleport, no change of fuel
    #
    # Validators: else can set location.lon = 999999.11111, or None
    #

    def fly_to(self, new_location: Location):
        print(f'flying to... {new_location}')
        pass


class Passenger(Flyable):
    name: str
    id: int
    km_flown: int

class Boeing737Certified:
    pass


class AirbusA380Certified:
    # certification in code; could be via "certified aircraft types"... (dynamic)
    pass


class Pilot(Flyable, Boeing737Certified):
    location: Location
    piloted_plane: Airplane
    km_flown: int

if __name__ == '__main__':
    a = Airplane()
    a.passengers = set()
    a.__fuel = 10
    print(a.__fuel)  # will work, but get a warning
    print(a.__dict__)  # show all variables
    a.pilot1 = None
    a.pilot2 = None
