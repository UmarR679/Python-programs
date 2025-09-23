class Cars:
    wheels = 4
    def __init__(self, mil, car):
        self.mil = mil
        self.car = car
    def get_mil(self):
        return self.mil
    def set_mil(self, value):
        self.mil = value
    @staticmethod
    def info():
        print("Hi, hello")
    @classmethod
    def infor(cls):
        return cls.wheels
Cars.info()
c1 = Cars(10, "BMW")
c2 = Cars(15, "Audi")
c1.wheels = 9
print(c1.mil)
print(c1.wheels)
print(c2.wheels)
print(c1.get_mil())
c1.set_mil(12)
print(c1.mil)
