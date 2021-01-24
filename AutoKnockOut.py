import random
import time
import matplotlib.pyplot as plt

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
    def __init__(self, name, dice, faces, auto, pause, verbose):
        self.name = name
        self.myScoreCard = ScoreCard(faces * dice)
        self.auto = auto
        self.pause = pause
        self.verbose = verbose
    
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
        if self.verbose:
            print(f'Rolled: {",".join(str(x) for x in rolls[:len(rolls) - 1])} and {str(rolls[-1])}')
        rolls = sorted(set(rolls))
        if all([self.myScoreCard.isKnockedOut(x) for x in rolls]) and self.myScoreCard.isKnockedOut(rollSum):
            if self.verbose:
                print('Rolled values and sum already knocked out, passing to next player')
            return
        if self.verbose:
            print(self.myScoreCard)
        if self.auto:
            random.seed()
            if self.verbose:
                print(f'Knock out {", ".join(str(x) for x in rolls)} or {rollSum}?')
            knockOutChoices = [x for x in rolls if not self.myScoreCard.isKnockedOut(x)]
            if not self.myScoreCard.isKnockedOut(rollSum):
                knockOutChoices.append(rollSum)
            knockOut = knockOutChoices[random.randint(1, len(knockOutChoices)) - 1]
            if self.verbose:
                print(f'Knocking out {knockOut}...')
            self.myScoreCard.knockOut(knockOut)
            if self.pause != 0:
                time.sleep(self.pause)
        else:
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
        if self.verbose:
            print(self.myScoreCard)
            print('')

    def isDone(self):
        return self.myScoreCard.isComplete()

class KnockOut():
    def __init__(self, names, dice, faces, auto, pause, verbose):
        if len(names) >= 2:
            self.players = [Player(x, dice, faces, auto, pause, verbose) for x in names]
        elif len(names) == 1:
            self.players = [Player(x, dice, faces, auto, pause, verbose) for x in names] + [Player('Player 2', dice, faces, auto, pause, verbose)]
        else:
            self.players = [Player('Player 1', dice, faces, auto, pause, verbose) for x in names] + [Player('Player 2', dice, faces, auto, pause, verbose)]
        self.theShaker = Shaker(dice, faces)
        self.verbose = verbose
    
    def playGame(self):
        while True:
            for x in self.players:
                if self.verbose:
                    print(f"\n{x.name}'s turn... ")
                x.takeTurn(self.theShaker)
                if x.isDone():
                    if self.verbose:
                        print(f'Game over! {x.name} is the winner!')
                    return x.name

def launchGame(names, dice, faces, auto, pause, verbose):
    knockOutGame = KnockOut(names, dice, faces, auto, pause, verbose)
    return knockOutGame.playGame()

def analyzeGame(names, dice, faces, runs):
    namesIndices = [x for x in range(len(names))]
    wins = [0 for x in names]
    for x in range(runs):
        wins[launchGame(namesIndices, dice, faces, True, False, False)] += 1
    plt.bar(names, wins)
    plt.xlabel = 'Players'
    plt.ylabel = 'Victories'
    plt.title(f'Knock Out Victory Distribution\nRuns: {runs}')

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--names', '-n', nargs = '+', type = str)
    parser.add_argument('--dice', '-d', type = int, default = 2)
    parser.add_argument('--faces', '-f', type = int, default = 6)
    parser.add_argument('--auto', '-a', default = False)
    parser.add_argument('--pause', '-p', type = float, default = 0)
    parser.add_argument('--runs', '-r', type = int, default = 0)
    parser.add_argument('--verbose', '-v', default = True)
    args = parser.parse_args()
    names = args.names
    dice = args.dice
    faces = args.faces
    auto = args.auto
    if auto:
        auto = True
    pause = args.pause
    runs = args.runs
    verbose = args.verbose
    if verbose != True:
        verbose = False
    if runs > 0:
        analyzeGame(names, dice, faces, runs)
        plt.show()
    else:
        launchGame(names, dice, faces, auto, pause, verbose)
