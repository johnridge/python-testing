from Player import Player
from Shaker import Shaker

class KnockOut():
    def __init__(self, names, dice, faces):
        if len(names) >= 2:
            self.players = [Player(x, dice, faces) for x in names]
        else:
            self.players = [Player(x, dice, faces) for x in names] + [Player('Placeholder', dice, faces)]
        self.theShaker = Shaker(dice, faces)
    
    def playGame(self):
        while True:
            for x in self.players:
                print(f"\n{x.name}'s turn... ")
                x.takeTurn(self.theShaker)
                if x.isDone():
                    print(f'Game over! {x.name} is the winner!')
                    return
                