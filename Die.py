import random

class Die():
    def __init__(self, faces):
        self.value = 0
        self.faces = faces
    
    @property
    def faces(self):
        return self.__faces

    @faces.setter
    def faces(self, faces):
        if faces >= 2:
            self.__faces = faces
        else:
            self.__faces = 6
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    def roll(self):
        random.seed()
        self.value = random.randint(1, self.faces)
