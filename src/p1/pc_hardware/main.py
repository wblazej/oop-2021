from lib.components.motherboard import Motherboard
from lib.components.memory_chip import MemoryChip
from lib.components.cpu import CPU
from lib.components.disks import SSD, HDD
from lib.components.gpu import GPU
from lib.computer import Computer

if __name__ == "__main__":
    motherboard = Motherboard(ram_standard="DDR4", 
                            ram_slots=4, 
                            ram_frequency_compatibility_MHz=[3200, 3466, 3600], 
                            max_ram_gb=128,
                            cpu_socket="AM4",
                            drive_connectors={"M.2": 2, "SATA3": 6},
                            pcie=2)

    rams = [MemoryChip(standard="DDR4", frequency_MHz=3200, memory_gb=16) for _ in range(4)]
    cpu = CPU(socket="AM4", cores=8, clock_frequency_GHz=3.8)
    ssd = SSD(capacity_gb=256, connector="M.2", write_speed_mbps=3100, read_speed_mbps=1050, total_bytes_written_tb=400)
    hdd = HDD(capacity_gb=256, connector="SATA3", write_speed_mbps=250, read_speed_mbps=100, rmp=7200)
    gpu = GPU(memory_standard="GDDR6", ram_gb=12, clock_frequency_MHz=1777, ram_frequency_MHz=15000)

    motherboard.insert_ram(rams[0])
    motherboard.insert_ram(rams[1])

    motherboard.insert_cpu(cpu)

    motherboard.insert_disk(ssd)
    motherboard.insert_disk(hdd)

    motherboard.insert_gpu(gpu)

    computer = Computer()
    computer.set_motherboard(motherboard)

    computer.run()
    print(computer)
