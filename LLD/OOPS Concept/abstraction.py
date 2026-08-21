from abc import ABC, abstractmethod

class Bird(ABC):

    @abstractmethod
    def fly(self):
        pass


class Eagle(Bird):

    def fly(self):
        print("Eagle flies very high")


class Sparrow(Bird):

    def fly(self):
        print("Sparrow flies low")