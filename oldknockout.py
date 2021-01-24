import argparse
import random

def displayValues(playerValue):
    print('Remaining: ', end = ' ')
    for x in playerValue:
        if x == 0:
            print('__', end = ' ')
        else:
           print(x, end = ' ')
    print('')

def isWinner(playerValue, dice, faces):
    score = [x for x in playerValue if x == 0]
    if len(score) == faces * dice:
        return True

def takeTurn(playerValue, dice, faces):
    random.seed()
    rolls = [random.randint(1, faces) for x in range(dice)]
    print(f'Rolled: {rolls}')
    knockedOut = [x for x in rolls if x != playerValue[x - 1]] + [sum(rolls) if sum(rolls) != playerValue[sum(rolls) - 1] else '']
    knockedOut = [x for x in knockedOut if x != '']
    if knockedOut == dice + 1:
        print(f'{rolls} and {sum(rolls)} have already been knocked out, passing to next player')
        return
    displayValues(playerValue)
    while True:
        while True:
            knockOut = input(f'Knock out {rolls} or {sum(rolls)}: ')
            if knockOut.isdigit(): 
                knockOut = int(knockOut)
                break
            else:
                print('Please enter a valid integer input')
        if knockOut in rolls or knockOut == sum(rolls):
            if playerValue[knockOut - 1] == 0:
                print(f'{knockOut} has already been knocked out, please try again')
            else:
                playerValue[knockOut - 1] = 0
                break
        else:
            print('Invalid input, please try again')
    displayValues(playerValue)
    print('')

def main(playerNames, dice, faces):
    playerValues = [[n for n in range(1, dice * faces + 1)] for x in playerNames]
    gameOver = False
    while not gameOver:
        for x in range(len(playerNames)):
            print(f"{playerNames[x]}'s turn")
            takeTurn(playerValues[x], dice, faces)
            if isWinner(playerValues[x], dice, faces):
                gameOver = True
                print(f'{playerNames[x]} is the winner!')

parser = argparse.ArgumentParser()
parser.add_argument('--players', '-p', nargs = '+', required = True)
parser.add_argument('--dice', '-d', type = int, default = 2)
parser.add_argument('--faces', '-f', type = int, default = 6)
args = parser.parse_args()
dice = args.dice
faces = args.faces
playerNames = args.players
main(playerNames, dice, faces)
