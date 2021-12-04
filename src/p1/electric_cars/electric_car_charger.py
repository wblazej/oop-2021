class Car: 
    is_on: bool

    def __init__(self):
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print("Starting car...")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print("Stopping car...")

class ElectricCar(Car):
    __battery_charge: int
    __max_battery_charge: int

    def __init__(self, battery_charge, max_battery_charge):
        super().__init__()
        self.__battery_charge = battery_charge
        self.__max_battery_charge = max_battery_charge

    def get_battery_charge(self) -> int:
        return self.__battery_charge

    def get_max_battery_charge(self) -> int:
        return self.__max_battery_charge

    def charge(self, Ah: int) -> int:
        if not self.is_on:
            print("Charging...")

            to_charge = self.__max_battery_charge - self.__battery_charge

            if Ah > to_charge:
                Ah = to_charge
            self.__battery_charge += Ah

            return Ah
        else:
            print("You cannot charge the car while it's still working!")
            return 0

class Charger: 
    __total_Ah_charged: int

    def __init__(self):
        self.__total_Ah_charged = 0

    def charge_car(self, car: ElectricCar, Ah: int):
        Ah_used = car.charge(Ah)
        self.__total_Ah_charged += Ah_used

    def get_total_Ah_charged(self) -> int:
        return self.__total_Ah_charged

if __name__ == "__main__":
    charger = Charger()
    car = ElectricCar(100, 200)

    print(car.is_on)
    car.power_on()
    print(car.is_on)
    car.power_off()

    print(car.get_battery_charge())
    charger.charge_car(car, Ah=50)
    print(car.get_battery_charge())

    print(f"Charger total: {charger.get_total_Ah_charged()}")
    