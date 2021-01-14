from Lesson_8_Dataclass.base_page import BaseTransport
from dataclasses import dataclass


@dataclass
class Car(BaseTransport):
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
    fuel_min: float


@dataclass
class EngineInf:  # двигатель
    fuel: float
    capacity: float
    power: int

