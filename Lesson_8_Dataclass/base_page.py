from dataclasses import dataclass

list_errors = {}
with open("/Users/bulbik/OTUS/Lesson_8_Dataclass/transport/errors.txt") as file:
    for line in file:
        key, value = line.split()
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
    fuel_min: float


def make_a_sound(self):
    print("Нажат клаксон")


def fuel_test():
    if fuel >= fuel_min:
        return turn_on_the_engine
    else:
        return False


def turn_on_the_engine():
    print("Двигатель включен")
