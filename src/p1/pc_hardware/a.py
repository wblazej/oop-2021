from dataclasses import dataclass
from enum import Enum
from typing import List

from p1.pc_hardware.cpu import CPU, AMD_CPU
from p1.pc_hardware.pcie import PCIeSlot


class PC:
    pass


class CpuSocket(Enum):
    AM4 = 1
    TR4 = 2
    sTRX4 = 3
    Socket_1200 = 4


class Motherboard:
    cpu: CPU
    cpu_socket: CpuSocket
    pcie: List[PCIeSlot] = [None] * 3

    def __init__(self, cpu: CPU):
        print(f'tworzę MB z CPU: {cpu} typu {type(cpu)}')
        self.cpu = cpu
        self.cpu_socket = CpuSocket.Socket_1200



class AMD_Motherboard(Motherboard):
    def __init__(self, cpu: AMD_CPU):
        super().__init__(cpu)


class Intel_Motherboard(Motherboard):
    pass
