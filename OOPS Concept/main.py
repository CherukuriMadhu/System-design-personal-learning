from class_object import Bird as Bird1
from encapsulation import Bird as Bird2
from inheritance import Parrot, Eagle
from polymorphism import Parrot as PolyParrot
from polymorphism import Crow
from polymorphism import Peacock
from abstraction import Eagle as AbsEagle
from abstraction import Sparrow

print("===== CLASS & OBJECT =====")

bird = Bird1("Parrot", "Green")
bird.details()
bird.fly()
bird.eat()

print("\n===== ENCAPSULATION =====")

bird2 = Bird2("Parrot", "Green", 3)
bird2.display()

bird2.set_age(5)
print("Updated Age:", bird2.get_age())

print("\n===== INHERITANCE =====")

p = Parrot("Parrot")
p.fly()
p.speak()

e = Eagle("Eagle")
e.fly()
e.hunt()

print("\n===== POLYMORPHISM =====")

birds = [PolyParrot(), Crow(), Peacock()]

for b in birds:
    b.sound()

print("\n===== ABSTRACTION =====")

e1 = AbsEagle()
e1.fly()

s = Sparrow()
s.fly()