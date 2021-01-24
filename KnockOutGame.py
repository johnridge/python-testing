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
        if faces < 2 or not isinstance(faces, int):
            self.__faces = 6
        else:
            self.__faces = faces
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value

    def roll(self):
        random.seed()
        self.value = random.randint(1, self.faces)

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

class Player():
    def __init__(self, name, dice, faces):
        self.name = name
        self.myScoreCard = ScoreCard(faces * dice)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    def takeTurn(self, shaker):
        shaker.shake()
        rolls = shaker.getResults()
        rollSum = shaker.getSum()
        print(f'Rolled: {",".join(str(x) for x in rolls[:len(rolls) - 1])} and {str(rolls[-1])}')
        rolls = sorted(set(rolls))
        if all([self.myScoreCard.isKnockedOut(x) for x in rolls]) and self.myScoreCard.isKnockedOut(rollSum):
            print('Rolled values and sum already knocked out, passing to next player')
            return
        print(self.myScoreCard)
        while True:
            knockOut = int(input(f'Knock out {", ".join(str(x) for x in rolls)} or {rollSum}? '))
            if knockOut in rolls or knockOut == rollSum:
                if self.myScoreCard.isKnockedOut(knockOut):
                    print(f'{knockOut} has already been knocked out, please try again')
                else:
                    self.myScoreCard.knockOut(knockOut)
                    break
            else:
                print('Invalid input, please try again')
        print(self.myScoreCard)
        print('')

    def isDone(self):
        return self.myScoreCard.isComplete()

class KnockOut():
    def __init__(self, names, dice, faces):
        if len(names) >= 2:
            self.players = [Player(x, dice, faces) for x in names]
        elif len(names) == 1:
            self.players = [Player(x, dice, faces) for x in names] + [Player('Player 2', dice, faces)]
        else:
            self.players = [Player('Player 1', dice, faces) for x in names] + [Player('Player 2', dice, faces)]
        self.theShaker = Shaker(dice, faces)
    
    def playGame(self):
        while True:
            for x in self.players:
                print(f"\n{x.name}'s turn... ")
                x.takeTurn(self.theShaker)
                if x.isDone():
                    print(f'Game over! {x.name} is the winner!')
                    return

def launchGame(names, dice, faces):
    knockOutGame = KnockOut(names, dice, faces)
    knockOutGame.playGame()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--names', '-n', nargs = '+', type = str)
    parser.add_argument('--dice', '-d', type = int, default = 2)
    parser.add_argument('--faces', '-f', type = int, default = 6)
    args = parser.parse_args()
    names = args.names
    dice = args.dice
    faces = args.faces
    launchGame(names, dice, faces)
