def main(useSimple):
    def simple():
        length = 0
        while length <= 0 or not isinstance(length, int):   
            length = int(input("Enter list length: "))
            if length <= 0 or not isinstance(length, int):
                print("Length must be a positive nonzero integer")
        intList = [int(input("Enter an integer: ")) for x in range(length)]
        print(f"The smallest list entry is {min(intList)}")
    def complicated():
        length = 0
        while length <= 0 or not isinstance(length, int):   
            length = int(input('Enter list length: '))
            if length <= 0 or not isinstance(length, int):
                print('Length must be a positive nonzero integer')
        currentInt = 0
        for x in range(length):
            intInput = int(input('Enter an integer: '))
            if x == 0:
                currentInt = intInput
            elif currentInt > intInput:
                currentInt = intInput
            else:
                continue
        print(f'The smallest list entry is {currentInt}')
    if not useSimple:
        complicated()
    else:
        simple()
useSimple = input('Use simple algorithm? ')
if useSimple == 'false' or useSimple == 'False' or useSimple == 'no' or useSimple == 'No':
    useSimple = False
if useSimple == 'true' or useSimple == 'True' or useSimple == 'yes' or useSimple == 'Yes':
    useSimple = True
main(useSimple)
