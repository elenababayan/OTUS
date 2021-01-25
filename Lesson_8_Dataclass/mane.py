from Lesson_8_Dataclass.base_page import BaseTransport
from Lesson_8_Dataclass.transport.air import Air

if __name__ == "__main__":  # тест для самолета
    fuel = 26025
    speed = 220
    elevation = 5
    echelon = 10600
    landing_height = 400
    permissible_speed = 300

    print(Air.get_transport({}))
    BaseTransport.fuel_test()
    Air.test_takeoff()
    Air.test_landing()
