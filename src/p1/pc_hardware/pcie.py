from dataclasses import dataclass


@dataclass
class PCIeDevice:
    gen: int = 4


class PCIeSlot:
    gen: int = 4
    device: PCIeDevice

    def insert_device(self, device: PCIeDevice):
        self.device = device

    def get_device(self) -> PCIeDevice:
        return self.device

    def remove_device(self):
        self.device = None


class GraphicsCard(PCIeDevice):
    cores: int
    frequency: int
    memory_gb: int


class NvidiaGraphicsCard(GraphicsCard):
    pass
