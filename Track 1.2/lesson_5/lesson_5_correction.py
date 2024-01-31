class ComputerSystem:
    """
    Компьютер. Включает в себя процессор, оперативную память, жесткий диск, видеокарту, материнскую плату
    """

    def __init__(self, processor, ram, hard_drive, graphics_card, motherboard):
        self.processor = processor
        self.ram = ram
        self.hard_drive = hard_drive
        self.graphics_card = graphics_card
        self.motherboard = motherboard


class Processor:
    """
    Процессор
    """

    def __init__(self, clock_speed, number_of_cores):
        self.clock_speed = clock_speed  # тактовая частота
        self.number_of_cores = number_of_cores  # количество ядер


class RAM:
    """
    Оперативная память
    """

    def __init__(self, size, ram_type, frequency):
        self.size = size  # объем
        self.ram_type = ram_type  # тип
        self.frequency = frequency  # частота


class HardDrive:
    """
    Жесткий диск
    """

    def __init__(self, size, form_factor, read_speed, write_speed):
        self.size = size  # объем памяти
        self.form_factor = form_factor  # форм-фактор
        self.read_speed = read_speed  # скорость чтения
        self.write_speed = write_speed  # скорость записи


class GraphicsCard:
    """
    Видеокарта
    """

    def __init__(self, memory_size, card_type):
        self.memory_size = memory_size  # объем памяти
        self.card_type = card_type  # тип


class Motherboard:
    """
    Материнская плата
    """

    def __init__(self, socket_type, form_factor, port_set):
        self.socket_type = socket_type  # тип сокета
        self.form_factor = form_factor  # форм фактор
        self.port_set = port_set  # набор портов


if __name__ == '__main__':
    graphics_card = GraphicsCard(5, 'discret')
    hard_drive = HardDrive(1024, 'M2', 3500, 3000)
    ram = RAM(8, 'DDR4', 3200)
    processor = Processor(2.5, 10)
    motherboard = Motherboard('AM4', 'Standard-ATX', [{'SATA': 6, 'USB 3.0': 6, 'HDMI': 2}])
    # Собираем компьютер из комплектующих
    computer = ComputerSystem(processor, ram, hard_drive, graphics_card, motherboard)
