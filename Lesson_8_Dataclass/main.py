from Lesson_8_Dataclass.base_page import fuel_test, turn_on_the_engine
from Lesson_8_Dataclass.transport.air import test_takeoff, test_landing

if __name__ == "__mane__":
    fuel = 26025
    speed = 220
    elevation = 5
    echelon = 10600
    landing_height = 400
    permissible_speed = 250

    fuel_test()
    turn_on_the_engine()
    test_takeoff()
    test_landing()


