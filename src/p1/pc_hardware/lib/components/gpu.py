from lib.component import Component

class GPU(Component):
    __memory_standard: str
    __ram_gb: int
    __clock_frequency_MHz: int
    __ram_frequency_MHz: int

    def __init__(self, memory_standard: str, ram_gb: int, clock_frequency_MHz: int, ram_frequency_MHz: int):
        self.__memory_standard = memory_standard
        self.__ram_gb = ram_gb
        self.__clock_frequency_MHz = clock_frequency_MHz
        self.__ram_frequency_MHz = ram_frequency_MHz

    def __repr__(self):
        return (
            f'{type(self).__name__}(GPU: {self.__clock_frequency_MHz}MHz, RAM: {self.__memory_standard}, '
            f'{self.__ram_gb}GB {self.__ram_frequency_MHz}MHz)'
        )

    @property
    def memory_standard(self) -> str:
        return self.__memory_standard

    @property
    def ram_gb(self) -> int:
        return self.__ram_gb

    @property
    def clock_frequency_MHz(self) -> int:
        return self.__memory_standard

    @property
    def ram_frequency_MHz(self) -> int:
        return self.__ram_frequency_MHz
