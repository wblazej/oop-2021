from typing import List

from lib.components.ram_memory import RAMMemory
from lib.components.cpu import CPU
from lib.components.disks import Disk
from lib.component import Component

class Motherboard(Component):
    __ram_standard: str
    __ram_slots: int
    __ram_frequency_compatibility_MHz: List[int]
    __max_ram_gb: int
    __cpu_socket: str

    """
    connector name is the key and the value is number of connectors of this type
    """
    __drive_connectors: dict

    __ram: List[RAMMemory]
    __cpu: CPU
    __disks: List[Disk]

    def __init__(self, ram_standard: str,
                ram_slots: int, 
                ram_frequency_compatibility_MHz: List[int], 
                max_ram_gb: int,
                cpu_socket: str,
                drive_connectors: dict):
        self.__ram_standard = ram_standard
        self.__ram_slots = ram_slots
        self.__ram_frequency_compatibility_MHz = ram_frequency_compatibility_MHz
        self.__max_ram_gb = max_ram_gb
        self.__cpu_socket = cpu_socket
        self.__drive_connectors = drive_connectors

        self.__ram = []
        self.__cpu = None
        self.__disks = []

    def insert_ram(self, new_ram: RAMMemory):
        if type(new_ram) != RAMMemory:
            raise RuntimeError("It's not a RAM memory")

        if new_ram.standard != self.__ram_standard:
            raise RuntimeError("This RAM standard is incompatible with motherboard")

        if new_ram.frequency_MHz not in self.__ram_frequency_compatibility_MHz:
            raise RuntimeError("This RAM frequency is incompatible with motherboard")

        if len(self.__ram) + 1 > self.__ram_slots:
            raise RuntimeError("RAM slots count exceeded")

        if self.ram_gb + new_ram.memory_gb > self.__max_ram_gb:
            raise RuntimeError("Motherboard RAM memory limit exceeded")

        self.__ram.append(new_ram.connect())

    def insert_cpu(self, new_cpu):
        if type(new_cpu) != CPU:
            raise RuntimeError("It's not a CPU")

        if new_cpu.socket != self.__cpu_socket:
            raise RuntimeError("This CPU socket is incompatible with motherboard")

        self.__cpu = new_cpu.connect()

    def insert_disk(self, new_disk):
        if not issubclass(type(new_disk), Disk):
            raise RuntimeError("It's not a disk")

        conn = new_disk.connector
        if self.__drive_connectors[conn] < sum([1 if x.connector == conn else 0 for x in self.__disks]) + 1:
            raise RuntimeError("There is not free slot for this disk")

        self.__disks.append(new_disk.connect())
        

    @property
    def ram(self) -> List[RAMMemory]:
        return self.__ram

    @property
    def ram_gb(self) -> int:
        return sum([ram.memory_gb for ram in self.__ram])

    @property
    def cpu(self) -> CPU:
        return self.__cpu

    @property
    def disks(self) -> List[Disk]:
        return self.__disks
