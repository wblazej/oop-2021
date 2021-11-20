from os import pardir
import re

class SystemSimulation:
    @staticmethod
    def read_sensors():
        return open('log/sensors.txt').read()

    @staticmethod
    def read_cpuinfo():
        return open('log/cpuinfo.txt').read()

    @staticmethod
    def read_nvme():
        return open('log/nvme.txt').read()

class Parser:
    def get_cpu_temp(self, text_to_parse: str):
        lines = [self.__remove_spaces(x) for x in text_to_parse.split('\n')]
        temperatures = [x.split()[2] for x in list(filter(lambda x: re.search(r"(Core \d: .\d{1,2}\.\d)", x), lines))]
        return round(sum([self.__convert_to_float(x) for x in temperatures]) / len(temperatures), 1)

    def get_cpu_state(self, freq_idle: float, freq_boosted: float, text_to_parse: str):
        lines = [self.__remove_spaces(x) for x in text_to_parse.split('\n')]
        freqs = [self.__convert_to_float(x) for x in list(filter(lambda x: re.search(r'(cpu MHz : \d{1,4}.\d{1,3})', x), lines))]

        state = { 'idle': 0, 'normal': 0, 'boosted': 0 }

        for f in freqs:
            if f <= freq_idle:
                state['idle'] += 1
            elif f >= freq_boosted:
                state['boosted'] += 1
            else:
                state['normal'] += 1

        return state

    def get_drive_data(self, text_to_parse):
        lines = [self.__remove_spaces(x) for x in text_to_parse.split('\n')][1:]
        data = {}
        for l in lines:
            l = l.split(' : ')
            key = l[0].lower().replace(' ', '_')
            value = l[1]
            data[key] = self.__convert_to_float(value)
        return data
        

    def __convert_to_float(self, value):
        if ',' in value:
            return [float(''.join(list(filter(lambda x: re.match(r'[\d^\.]', x), x)))) for x in value.split(',')]
        return float(''.join(list(filter(lambda x: re.match(r'[\d^\.]', x), value))))

    def __remove_spaces(self, text):
        return ' '.join(text.split())

if __name__ == "__main__":
    parser = Parser()

    cpu_temp = parser.get_cpu_temp(SystemSimulation.read_sensors())
    print(cpu_temp)

    print('\n------------\n')
    
    cpu_state = parser.get_cpu_state(1800, 2300, SystemSimulation.read_cpuinfo())
    print(cpu_state)

    print('\n------------\n')

    drive_data = parser.get_drive_data(SystemSimulation.read_nvme())
    print(drive_data['critical_warning'])
    print(drive_data['temperature'])
    print(drive_data['data_units_written'])
    print(drive_data['percentage_used'])
    print(drive_data['power_cycles'])
    print(drive_data['temperature_sensor_1'])
    print(drive_data['temperature_sensor_2'])
    print(drive_data['thermal_management_t1_trans_count'])
    print(drive_data['thermal_management_t2_trans_count'])
    print(drive_data['thermal_management_t1_total_time'])
    print(drive_data['thermal_management_t2_total_time'])
