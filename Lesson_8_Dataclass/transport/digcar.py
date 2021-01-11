from dataclasses import dataclass
from Lesson_8_Dataclass.transport.car import Car


@dataclass
class BigCar(Car):
    equipment: str
    transmission: str
    wheels: int
    engine: dict
    weight: dict
    carrying: int
    model: str
    brand: str
    seats: int
    length: float
    height: float
    width: float


