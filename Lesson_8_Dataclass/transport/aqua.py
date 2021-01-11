from dataclasses import dataclass

from Lesson_8_Dataclass.base_page import BaseTransport


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
class SailInf:# парус
    pass # свойства паруса