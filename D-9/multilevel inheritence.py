class Animal:
    def species(self):
        return "This is an Animal"
class Mammal(Animal):
    def category(self):
        return "This is a mammal"
class Human(Mammal):
    def speak(self):
        return "humans can speak"
h=Human()
print(h.species())
print(h.category())
print(h.speak())