from dataclasses import dataclass


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


def make_a_sound(self):
    pass


def fuel_test():
    if fuel >= fuel_min:
        return turn_on_the_engine
    else:
        return False
    #


def turn_on_the_engine(self):
    print("Двигатель включен")
