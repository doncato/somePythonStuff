# Author: doncato
# Description: Mastermind Game
# mastermind.py
import random, time
# Variables
# 0 - none, 1 - 1 Player, 2 - 2 Players
playMode = 0
check = (1, 2, 3, 4, 5, 6)
guesses = 0
checkInput = True
# 0 - running, 1 - Out of guesses, 2 - Guessed correctly
gameStatus = 0
C1 = C2 = C3 = C4 = C5 = C6 = 0
fullCode = [C1, C2, C3, C4]

# Game
# -Welcome
print('Welcome to Mastermind\nThis is a python game just like Mastermind, you can either play alone or against a random generated code.\nInstead of colors this code is using the Numbers 1, 2, 3, 4, 5 and 6')
# -Set Playermode
while playMode == 0:
 playModeInput = input('Do you want to play against the Script?\n >')
 if playModeInput.lower() == 'y' or playModeInput.lower() == 'yes':
     playMode = 1
 if playModeInput.lower() == 'n' or playModeInput.lower() == 'no':
     playMode = 2
# -Create Code
if playMode == 1:
    C1 = random.randint(1, 6)
    C2 = random.randint(1, 6)
    C3 = random.randint(1, 6)
    C4 = random.randint(1, 6)
if playMode == 2:
    print('Player 1, please enter your code. Please make sure to hide it from Player 2')
    while True:
        C1, C2, C3, C4 = input('Enter 4 numbers from 1 to 6 separated by a space.\n >').split()
        C1 = int(C1)
        C2 = int(C2)
        C3 = int(C3)
        C4 = int(C4)
        if C1 in check and C2 in check and C3 in check and C4 in check:
            break
        else:
            print('Numbers are not valid')
    print('The code you entered was: ', C1, C2, C3, C4)
    time.sleep(5)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 1, please resize the window, to avoid that Player 2 could see the code\nIf you are done, tell Player 2, she/he can start')
    time.sleep(5)

print('Let the game begin!')
while gameStatus == 0:
    correctCounter = 0
    valueCounter = 0
    guesses = guesses + 1
    print('This is your ', guesses, '. guess out of 7 guesses.')
    C1G, C2G, C3G, C4G = input('Try a combination (enter 4 numbers seperated by a space)\n >').split()
    C1G = int(C1G)
    C2G = int(C2G)
    C3G = int(C3G)
    C4G = int(C4G)
    tempCode = [C1, C2, C3, C4]
    # Count correct Position
    if C1G in tempCode:
        valueCounter = valueCounter + 1
        tempCode.remove(C1G)
    if C2G in tempCode:
        valueCounter = valueCounter + 1
        tempCode.remove(C2G)
    if C3G in tempCode:
        valueCounter = valueCounter + 1
        tempCode.remove(C3G)
    if C4G  in tempCode:
        valueCounter = valueCounter + 1
        tempCode.remove(C4G)
    del tempCode
    # Count exact correct Numbers
    if C1G == C1:
        correctCounter = correctCounter + 1
    if C2G == C2:
        correctCounter = correctCounter + 1
    if C3G == C3:
        correctCounter = correctCounter + 1
    if C4G == C4:
        correctCounter = correctCounter + 1
    # If all is correct...
    if correctCounter == 4:
        print('The combination you entered is equal to the code, congrats!')
        gameStatus = 2
    elif guesses == 7:
        print('Out of guesses')
        gameStatus = 1
    else:
        # Tell the number of 'correctness'
        valueCounterCalc = valueCounter - correctCounter
        print('You guessed the right Numbers', valueCounterCalc, 'times.')
        print('Your guessed the Numbers within their right Positions ', correctCounter, ' times.')


if gameStatus == 1:
    print('The game is over, you ran out of guesses.\nThe code was', C1, C2, C3, C4)
if gameStatus == 2:
    print('The game is over, you guessed the code.\nThe code was', C1, C2, C3, C4)
time.sleep(5)
print('Bye')
quit()
