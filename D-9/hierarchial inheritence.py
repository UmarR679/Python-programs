class vehicle:
    def fuel_type(self):
        return "vehicle can use petrol, diesel and LPG"
class car(vehicle):
    def type(self):
        return "car is a 4-wheeler"
class bike(vehicle):
    def type(self):
        return "bike is a 2-wheeler"
c=car()
b=bike()
print(c.fuel_type())
print(c.type())
print(b.type())