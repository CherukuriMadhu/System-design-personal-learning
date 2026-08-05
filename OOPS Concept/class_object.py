class Bird:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def fly(self):
        print(self.name, "is flying")

    def eat(self):
        print(self.name, "is eating")

    def details(self):
        print("Name :", self.name)
        print("Color:", self.color)