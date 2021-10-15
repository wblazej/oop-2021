from lib.component import Component

class RAMMemory(Component):
    __standard: str
    __frequency_MHz: int
    __memory_gb: int

    def __init__(self, standard: str, frequency_MHz: int, memory_gb: int):
        self.__standard = standard
        self.__frequency_MHz = frequency_MHz
        self.__memory_gb = memory_gb

    def __repr__(self):
        return f'{type(self).__name__}({self.__memory_gb}GB, {self.__standard}, {self.__frequency_MHz}Mhz)'

    @property
    def standard(self) -> str:
        return self.__standard
    
    @property
    def frequency_MHz(self) -> int:
        return self.__frequency_MHz

    @property
    def memory_gb(self) -> int:
        return self.__memory_gb
