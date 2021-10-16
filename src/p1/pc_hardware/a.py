from dataclasses import dataclass
from typing import List

from p1.pc_hardware.cpu import CPU, AMD_CPU
from p1.pc_hardware.pcie import PCIeSlot


class PC:
    pass


class Motherboard:
    cpu: CPU
    pcie: List[PCIeSlot] = [None] * 3

    def __init__(self, cpu: CPU):
        print(f'tworzę MB z CPU: {cpu} typu {type(cpu)}')
        self.cpu = cpu


class AMD_Motherboard(Motherboard):
    def __init__(self, cpu: AMD_CPU):
        super().__init__(cpu)


class Intel_Motherboard(Motherboard):
    pass
