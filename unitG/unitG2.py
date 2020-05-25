import random
# generate random number from 1 to 100
secretNum = random.randint(1,100)
# counter for attempts
guess = 0
w = False

print("Welcome to my guessing game!")
while (w == False):
    # ask user to guess the number
    userNum = input("Please enter a number between 1-100: ")
    guess+=1

    if (secretNum == int(userNum)):
        print("Congratulations, you guessed right!")
        print("Number of guesses you took: {}".format(guess))
        w = True
        break
    else:
        if(int(userNum) < secretNum):
            print("Too low, try again!")
        else:
            print("Too high, try again!")

'''
    Welcome to my guessing game!
    Please enter a number between 1-100: 34
    Too low, try again!
    Please enter a number between 1-100: 42
    Too low, try again!
    Please enter a number between 1-100: 55
    Too high, try again!
    Please enter a number between 1-100: 54
    Too high, try again!
    Please enter a number between 1-100: 53
    Too high, try again!
    Please enter a number between 1-100: 52
    Too high, try again!
    Please enter a number between 1-100: 51
    Too high, try again!
    Please enter a number between 1-100: 50
    Too high, try again!
    Please enter a number between 1-100: 49
    Too high, try again!
    Please enter a number between 1-100: 48
    Too high, try again!
    Please enter a number between 1-100: 47
    Too high, try again!
    Please enter a number between 1-100: 46
    Too high, try again!
    Please enter a number between 1-100: 45
    Congratulations, you guessed right!
    Number of guesses you took: 13
'''
