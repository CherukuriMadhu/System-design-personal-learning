class Bird:

    def __init__(self, name, color, age):
        self.name = name
        self.__color = color
        self.__age = age

    def get_color(self):
        return self.__color

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def display(self):
        print("Name :", self.name)
        print("Color:", self.__color)
        print("Age  :", self.__age)