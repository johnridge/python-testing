import math
def displayVolume(volume, prism):
    print(f'\nThe volume of the {prism} prism is {volume} cm^3')

stop = False
print('Welcome to the prisms volume calculator')
while not stop:
    print('\nWhich type of prism would you like to calculate the volume of? Choose from the following menu: ')
    print('1) Triangular\n2) Hexagonal\n3) Rectangular\n4) Pentagonal\n9) Exit')
    option = int(input('Option: '))
    if option == 1:
        print('\nOption 1: Triangular Prism')
        print('Enter the following values in centimeters –')
        base = float(input('Base of the triangle: '))
        height = float(input('Base of the triangle: '))
        length = float(input('Length of the prism: '))
        volume = 1 / 2 *  base * height * length
        displayVolume(volume, 'triangular')
    elif option == 2:
        print('\nOption 2: Hexagonal Prism')
        print('Enter the following values in centimeters –')
        edge = float(input('Edge of the hexagon: '))
        length = float(input('Length of the prism: '))
        volume = 3 / 2 * math.sqrt(3) * edge ** 2 * length
        displayVolume(volume, 'hexagonal')
    elif option == 3:
        print('\nOption 3: Rectangular Prism')
        print('Enter the following values in centimeters –')
        width = float(input('Width of the rectangle: '))
        length = float(input('Length of the rectangle: '))
        height = float(input('Base of the rectangle: '))
        volume = width * height * length
        displayVolume(volume, 'rectangular')
    elif option == 4:
        print('\nOption 4: Pentagonal Prism')
        print('Enter the following values in centimeters –')
        edge = float(input('Edge of the pentagon: '))
        length = float(input('Length of the prism: '))
        volume = 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) ** edge * length
        displayVolume(volume, 'pentagonal')
    elif option == 9:
        print('\nThank you for using our volume calculator. Good-bye!')
        stop = True
    else:
        print('\nPlease try again with a valid input')
        