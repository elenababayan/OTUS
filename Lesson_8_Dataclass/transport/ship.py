from Lesson_8_Dataclass.base_page import BaseTransport


class Ship(BaseTransport):

    def __init__(self, weight, carrying, height, seats):
        super().__init__(weight, carrying, seats)
        self.height = height
