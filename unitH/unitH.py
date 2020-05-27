import random

min = 1
max = 6

playerA = open("Player_A.txt", "w")
for i in range(0, 3):
    rollA = random.randint(min, max)
    playerA.write(str(rollA))
    playerA.write("\n")

playerB = open("Player_B.txt", "w")
for i in range(0, 3):
    rollB = random.randint(min, max)
    playerB.write(str(rollB))
    playerB.write("\n")

# Player A's score
playerA = open("Player_A.txt")
linesA = playerA.read()
res = [int(x) for x in linesA.split()] # Convert strings to ints
# Player A's total score
sB = sum(res)

# Player B's score
playerB = open("Player_B.txt")
linesB = playerB.read()
res2 = [int(x) for x in linesB.split()] # Convert strings to ints
# Player B's total score
sA = sum(res2)

print("Player A's score: {}, Player B's score: {}".format(sA, sB))
if (sA > sB):
    print("Player A is a winner.")
if (sB > sA):
    print("Player B is a winner.")
if (sA == sB):
    print("It's a tie!")


'''
    >>> exec(open('unitH.py').read())
    Player A's score: 9, Player B's score: 14
    Player B is a winner.
    >>> exec(open('unitH.py').read())
    Player A's score: 9, Player B's score: 9
    It's a tie!
    >>> exec(open('unitH.py').read())
    Player A's score: 11, Player B's score: 14
    Player B is a winner.
    >>> exec(open('unitH.py').read())
    Player A's score: 11, Player B's score: 11
    It's a tie!
'''
