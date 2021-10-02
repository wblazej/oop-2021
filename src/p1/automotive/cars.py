from typing import List


class Wheel:
    healty = True


class Engine:
    healty = True


class Bodywork:
    healty = True


class Car:
    # pola klasy -- początek "kompozycji"
    wheels: List[Wheel]
    engine: Engine
    bodywork: Bodywork
    healty = True

    def __init__(self, wheels: List[Wheel], engine: Engine, bodywork: Bodywork):
        self.wheels = wheels
        self.engine = engine
        self.bodywork = bodywork
        self.healty = True


class Mechanic:
    avilable = True

    def repair_car(self, car: Car) -> bool:
        car.healty = True
        return True


class RepairShop:
    crew: List[Mechanic]

    def repair_car(self, car: Car):
        for m in self.crew:
            if m.avilable:
                m.repair_car(car)  # delegacja

    def hire(self, mechanic: Mechanic):
        self.crew.append(mechanic)


if __name__ == '__main__':
    # tworzymy instancje
    wheels = [Wheel() for i in range(4)]
    engines = [Engine() for i in range(100)]
    bodyworks = [Bodywork() for i in range(100)]
    car1 = Car(wheels, engines[0], bodyworks[0])
    m1, m2 = [Mechanic() for i in range(2)]
    warsztat = RepairShop()
    warsztat.hire(m1)

    warsztat.repair_car(car1)

