from dataclasses import dataclass
from Lesson_8_Dataclass.base_page import BaseTransport


@dataclass
class Air(BaseTransport):  # самолет
    engine: dict = {"Двигатель": CFM56-7B27, "Запас топлива, л": 26025,
                    "Удельный расход топлива, г/пасс.-км": 22.5, "Тяга, тс": '2 × 12.4'}
    weight: dict = {"Макс. взлетный вес (кг)": 85200,
                   "Макс. посадочный вес (кг)": 71400, "Макс. вес без топлива (кг)":67800}
    model: str = "737-900ER"
    brand: str = "Boeing"
    seats: int = 215
    length: float = 42.1
    height: float = 12.5
    wing_length: float = 34.3
    fuel_min: float = 26025
    takeoff_speed: int = 220
    transition_height: int = 10600
    landing_speed: int = 250

def test_takeoff():
    def test_on_board_computer():
        return start_of_takeoff

    def start_of_takeoff():
        if air traffic controller clearance:
            return take_off_run
        else:
            print(' '.join(list_errors.get('001')))
            raise

    def take_off_run():
        if speed <= takeoff_speed:
            print("Начало подьема")
        else:
            print(' '.join(list_errors.get('002')))
            raise

    def beginning_of_the_rise():
        if elevation1 == 5:
            print("Убираем шасси и отключаем механическое крыло")
        else:
            print(' '.join(list_errors.get('003')))
            raise

    def completion_of_the_rise():
        if echelon <= transition_height:
            print("Завершение подъема")
        else:
            print(' '.join(list_errors.get('004')))
            raise

def test_landing():
    def approach():
        if landing_height == 400:
            print("Выпуск шасси, предкрылок, закрылок")
        else:
            print(' '.join(list_errors.get('005')))

    def landing_speed():
        if permissible_speed == landing_speed:
            return start_of_landing
        else:
            print(' '.join(list_errors.get('006')))

    def start_of_landing():
            print("Приземление.Завершение посадки")
