from dataclasses import dataclass

from Lesson_8_Dataclass.base_page import BaseTransport


@dataclass
class Air(BaseTransport):  # летательный аппарат
    equipment: str
    transmission: str
    engine: dict
    weight: dict
    carrying: int
    model: str
    brand: str
    seats: int
    length: float
    height: float
    width: float
    fuel_min: float
    height_vpp: int
    takeoff_speed: int
    transition_height: int
    landing_speed: int

def test_takeoff():
    def test_on_board_computer():
        return start_of_takeoff

    def start_of_takeoff():
        if air traffic controller clearance:
            return take_off_run
        else:
            return False

    def take_off_run():
        if speed <= takeoff_speed:
            print("Начало подьема")
        else:
            return False

    def beginning_of_the_rise():
        if elevation == 5:
            print("Убираем шасси и отключаем механическое крыло")
        else:
            return False

    def completion_of_the_rise():
        if elevation <= transition_height:
            print("Завершение подъема")
        else:
            return False

def test_landing():
    def approach():
        if elevation == 400:
            print("Выпуск шасси, предкрылок, закрылок")
        else:
            return False

    def landing_speed():
        if speed == landing_speed:
            return decrease_in_altitude
        else:
            return False

    def decrease_in_altitude():
        if elevation == height_vpp:
            return start_of_landing
        else:
            return False

    def start_of_landing():
        if elevation == 0:
            print("Завершение посадки")
        else:
            return False