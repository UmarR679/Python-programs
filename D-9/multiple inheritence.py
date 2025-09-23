class engine:
    def engine_info(self):
        return "This is an engine"
class wheels:
    def wheels_info(self):
        return "Car has 4 wheels"
class car(engine,wheels):
    def car_info(self):
        return "This is a car"
c=car()
print(c.engine_info())
print(c.wheels_info())
print(c.car_info())