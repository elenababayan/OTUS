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

    def turn_on_the_engine(self):
        pass

    def turn_off_the_engine(self):
        pass


def fuel_test():
    if fuel >= fuel_min:
        return True
    else:
        return False
    #