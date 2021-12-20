from typing import List

from lib.components.memory_chip import MemoryChip
from lib.components.cpu import CPU
from lib.components.disks import Disk
from lib.components.gpu import GPU
from lib.component import Component

class Motherboard(Component):
    __ram_standard: str
    __ram_slots: int
    __ram_frequency_compatibility_MHz: List[int]
    __max_ram_gb: int
    __cpu_socket: str
    __drive_connectors: dict # connector name is the key and the value is number of connectors of this type
    __pcie: int

    __ram: List[MemoryChip]
    __cpu: CPU
    __disks: List[Disk]
    __gpu: GPU

    def __init__(self, ram_standard: str,
                ram_slots: int, 
                ram_frequency_compatibility_MHz: List[int], 
                max_ram_gb: int,
                cpu_socket: str,
                drive_connectors: dict,
                pcie: int):
        self.__ram_standard = ram_standard
        self.__ram_slots = ram_slots
        self.__ram_frequency_compatibility_MHz = ram_frequency_compatibility_MHz
        self.__max_ram_gb = max_ram_gb
        self.__cpu_socket = cpu_socket
        self.__drive_connectors = drive_connectors
        self.__pcie = pcie

        self.__ram = []
        self.__cpu = None
        self.__disks = []
        self.__gpu = None

    def __repr__(self):
        return (
            f'{type(self).__name__}(RAM: {self.__ram_standard}, {self.__ram_slots} slots, '
            f'{self.__ram_frequency_compatibility_MHz}, max {self.__max_ram_gb}gb, CPU: {self.__cpu_socket}, '
            f'Drive: {self.__drive_connectors}, PCIe: {self.__pcie})'
        )

    def insert_ram(self, new_ram: MemoryChip):
        if type(new_ram) != MemoryChip:
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

    def insert_gpu(self, new_gpu):
        if not type(new_gpu) == GPU:
            raise RuntimeError("It's not a GPU")

        self.__gpu = new_gpu.connect()
        

    @property
    def ram_stndard(self) ->  str:
        return self.__ram_standard

    @property
    def ram_slots(self) -> int:
        return self.__ram_slots

    @property
    def ram_frequency_compatibility_MHz(self) -> List[int]:
        return self.__ram_frequency_compatibility_MHz

    @property
    def max_ram_gb(self) -> int:
        return self.__max_ram_gb

    @property
    def cpu_socket(self) -> str:
        return self.__cpu_socket

    @property
    def drive_connectors(self) -> dict:
        return self.__drive_connectors

    @property
    def pcie(self) -> int:
        return self.__pcie

    @property
    def ram(self) -> List[MemoryChip]:
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

    @property
    def gpu(self) -> GPU:
        return self.__gpu
