from dataclasses import dataclass

list_errors = {}
with open("/Users/bulbik/OTUS/Lesson_8_Dataclass/transport/errors.txt") as file:
    for line in file:
        key, value = line.split(":")
        list_errors[key] = value


@dataclass
class BaseTransport:
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

    @staticmethod
    def make_a_sound():
        print("Нажат клаксон")

    @staticmethod
    def fuel_test():
        if fuel >= fuel_min:
            return turn_on_the_engine
        else:
            print(' '.join(list_errors.get('009')))

    @staticmethod
    def turn_on_the_engine():
        print("Двигатель включен")
