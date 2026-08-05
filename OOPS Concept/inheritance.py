class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(self.name, "can fly")


class Parrot(Bird):

    def speak(self):
        print(self.name, "can speak")


class Eagle(Bird):

    def hunt(self):
        print(self.name, "is hunting")