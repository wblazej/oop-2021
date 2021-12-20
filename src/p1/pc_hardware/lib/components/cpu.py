from lib.component import Component

class CPU(Component):
    __socket: str
    __cores: int
    __clock_frequency_GHz: float

    def __init__(self, socket: str, cores: int, clock_frequency_GHz: float):
        self.__socket = socket
        self.__cores = cores
        self.__clock_frequency_GHz = clock_frequency_GHz

    def __repr__(self):
        return f'{type(self).__name__}({self.__socket}, {self.__cores} cores, {self.__clock_frequency_GHz}GHz)'

    @property
    def socket(self) -> str:
        return self.__socket

    @property
    def cores(self) -> int:
        return self.__cores

    @property
    def clock_frequency_GHz(self) -> float:
        return self.__clock_frequency_GHz