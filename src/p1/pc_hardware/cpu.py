from dataclasses import dataclass


@dataclass
class CPU:
    frequency: int = 4000
    cores: int = 16
    cache: int = 128


class AMD_CPU(CPU):
    pass


class Intel_CPU(CPU):
    pass
