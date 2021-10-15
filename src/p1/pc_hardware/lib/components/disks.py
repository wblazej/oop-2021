from lib.component import Component

class Disk(Component):
    __capacity_gb: int
    __connector: str
    __write_speed_mbps: int
    __read_speed_mbps: int

    def __init__(self, capacity_gb: int, connector: str, write_speed_mbps: int, read_speed_mbps: int):
        self.__capacity_gb = capacity_gb
        self.__connector = connector
        self.__write_speed_mbps = write_speed_mbps
        self.__read_speed_mbps = read_speed_mbps

    @property
    def capacity_gb(self) -> int:
        return self.__capacity_gb

    @property
    def connector(self) -> str:
        return self.__connector

    @property
    def write_speed_mbps(self) -> int:
        return self.__write_speed_mbps

    @property
    def read_speed_mbps(self) -> int:
        return self.__read_speed_mbps


class SSD(Disk):
    __total_bytes_written_tb: int

    def __init__(self, total_bytes_written_tb, **kwargs):
        self.__total_bytes_written_tb = total_bytes_written_tb
        super().__init__(**kwargs)

    def __repr__(self):
        return (
            f'{type(self).__name__}({self.capacity_gb}GB {self.connector} Read: {self.read_speed_mbps},' 
            f'Write: {self.write_speed_mbps}, TBW: {self.__total_bytes_written_tb}TB)'
        )

class HDD(Disk):
    __rmp: int

    def __init__(self, rmp, **kwargs):
        self.__rmp = rmp
        super().__init__(**kwargs)

    def __repr__(self):
        return (
            f'{type(self).__name__}({self.capacity_gb}GB {self.connector} Read: {self.read_speed_mbps},' 
            f'Write: {self.write_speed_mbps}, RMP: {self.__rmp}rmp)'
        )
