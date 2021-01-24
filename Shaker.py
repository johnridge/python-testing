from Die import Die

class Shaker():
    def __init__(self, dice, faces):
        self.dice = [Die(faces) for x in range(dice)]

    @property
    def dice(self):
        return self.__dice

    @dice.setter
    def dice(self, dice):
        self.__dice = dice
    
    def shake(self):
        for x in self.dice:
            x.roll()
    
    def getResults(self):
        return [x.value for x in self.dice]

    def getSum(self):
        return sum([x.value for x in self.dice])
