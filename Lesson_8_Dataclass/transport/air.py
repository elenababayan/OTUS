from dataclasses import dataclass

from Lesson_8_Dataclass.base_page import BaseTransport


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
