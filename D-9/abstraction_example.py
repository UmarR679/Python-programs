from abstract_class import Vehicle
class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color
    def start(self):
        print("Start with Kick")
class Scooty(Vehicle):
    def start(self):
        print("Self Start")
class Car(Vehicle):
    def __init__(self,n,x):
        super.__init__(n)
        self.no_of_gears=6
    def start(self):
        print("start with the key")