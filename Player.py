from ScoreCard import ScoreCard

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
