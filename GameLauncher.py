from KnockOut import KnockOut

def gameLauncher(names, dice, faces):
    knockOutGame = KnockOut(names, dice, faces)
    knockOutGame.playGame()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--names', '-n', nargs = '+')
    parser.add_argument('--dice', '-d', type = int, default = 2)
    parser.add_argument('--faces', '-f', type = int, default = 6)
    args = parser.parse_args()
    names = args.names
    dice = args.dice
    faces = args.faces
    gameLauncher(names, dice, faces)
    