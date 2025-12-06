import random

while True:
    play = input('Roll the dice? (y/n): ')
    if play == 'y' or play == 'Y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')

    elif play == 'n' or play == 'N':
        print('Thank you for playing!')
        break

    else:
        print('Invalid input!')