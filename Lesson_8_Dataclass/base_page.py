from abc import abstractmethod, ABCMeta
from dataclasses import dataclass

list_errors = {}
with open("/Users/bulbik/OTUS/Lesson_8_Dataclass/transport/errors.txt") as file:
    for line in file:
        key, value = line.split(":")
        list_errors[key] = value


@dataclass
class BaseTransport:
    __metaclass__ = ABCMeta
    weight: dict
    carrying: int
    model: str
    brand: str
    seats: int
    length: float
    height: float
    width: float
    engine: dict
    fuel: float
    fuel_min: float

    @staticmethod
    def make_a_sound():
        print("Нажат клаксон")

    @staticmethod
    @abstractmethod
    def fuel_test():
        if fuel_min <= fuel:
            print("Двигатель включен")
        else:
            print(' '.join(list_errors.get('009')))
