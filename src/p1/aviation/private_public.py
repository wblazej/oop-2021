from dataclasses import dataclass


@dataclass
class Plane:
    __current_fuel: int = 10  # przykład zmiennej prywatnej
    __current_velocity_kmh: float = 900
    __max_fuel = 100

    def get_current_fuel(self):
        return self.__current_fuel

    def get_current_velocity_kmh(self):
        return self.__current_velocity_kmh

    def refuel(self, fuel_added: int):
        self.__current_fuel = min(self.__current_fuel + fuel_added, self.__max_fuel)

    engine: str = 'pratt&whitney'


def check_engine(p: Plane):
    if len(p.engine) < 3:
        raise RuntimeError('wrong engine')
    p.current_fuel = -12


p = Plane()
check_engine(p)
p.__current_fuel = 'kadabra'
print(p)
print(p.get_current_fuel())
p.refuel(100000)
print(p.get_current_fuel())
p.refuel(-100000)
print(p.get_current_fuel())

