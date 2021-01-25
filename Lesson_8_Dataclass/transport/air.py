from dataclasses import dataclass
from Lesson_8_Dataclass.base_page import BaseTransport


@dataclass
class Air(BaseTransport):  # самолет
    weight: dict
    carrying: int
    model: str
    brand: str
    seats: int
    length: float
    height: float
    width: float
    engine: dict
    fuel_min: float
    fuel: int

    @staticmethod
    def get_transport(data: dict):
        brand = "300-971"
        model = "Боинг"
        return brand, model

    @staticmethod
    def test_takeoff():
        def test_on_board_computer():
            return start_of_takeoff

        def take_off_run():
            if speed <= 220:
                print("Начало подьема")
            else:
                print(' '.join(list_errors.get('002')))


        def beginning_of_the_rise():
            if elevation1 == 5:
                print("Убираем шасси и отключаем механическое крыло")
            else:
                print(' '.join(list_errors.get('003')))


        def completion_of_the_rise():
            if echelon <= 10600:
                print("Завершение подъема")
            else:
                print(' '.join(list_errors.get('004')))

    @staticmethod
    def test_landing():
        def approach():
            if landing_height == 400:
                print("Выпуск шасси, предкрылок, закрылок")
            else:
                print(' '.join(list_errors.get('005')))

        def landing_speed():
            if permissible_speed == 250:
                return start_of_landing
            else:
                print(' '.join(list_errors.get('006')))

        def start_of_landing():
                print("Приземление.Завершение посадки")
