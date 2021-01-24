class ScoreCard():
    def __init__(self, numbers):
        self.numbers = [0 for x in range(numbers)]

    @property
    def numbers(self):
        return self.__numbers

    @numbers.setter
    def numbers(self, numbers):
        self.__numbers = numbers
    
    def knockOut(self, value):
        self.numbers[value - 1] = 1
    
    def isKnockedOut(self, value):
        if self.numbers[value - 1] == 1:
            return True
        else:
            return False

    def isComplete(self):
        if self.numbers.count(1) == len(self.numbers):
            return True
        else:
            return False

    def __str__(self):
        s = 'Remaining: '
        for x in range(len(self.numbers)):
            if self.numbers[x] == 1:
                s = s + ' __'
            else:
                s = s + f' {x + 1}'
        return s
        