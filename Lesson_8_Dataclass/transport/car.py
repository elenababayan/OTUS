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


@dataclass
class Air(BaseTransport):  # самолет
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


@dataclass
class Aqua(BaseTransport):  # корабль
    equipment: str
    engine: dict
    sail: dict
    weight: dict
    carrying: int
    model: str
    brand: str
    seats: int
    length: float
    height: float
    width: float


@dataclass
class SailInf:  # парус
    pass  # свойства паруса


@dataclass
class EngineInf:  # двигатель
    fuel: float
    capacity: float
    power: int
