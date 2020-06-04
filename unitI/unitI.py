# create a list for user tags
userTags = []
# prompt the user to enter the tags
tags = input("Please enter one to four tags: ")

userTags = tags.split() # split the user input into a list
tagsNum = len(userTags) # the number of user tags

# if there is less than 1 or more than 4 tags - exit the program
if (tagsNum < 1 or tagsNum > 4):
    exit()
else:
    
    # create a list for games that match the user's tags
    matchinGames = []
    gameInfo = []
 
    games = open("Lab9_CatGames.txt") # open the games
    for line in games:
        matchCount = 0
        gameInfo = line.split()
    
        for value in userTags:
            if (value in gameInfo):
                matchCount+=1
            if (matchCount == tagsNum):
            # if all tags found their match add the game to a the final list
                matchinGames.append(line)
                
    
    # print the results
    if (len(matchinGames) < 1):
        print("Sorry, no games match your criteria.")
    else:
        print("\nThere are", len(matchinGames), "games matching your tags.")
        for line in matchinGames:
            word = line.split()
            print("{}".format(word))
    

'''
Test 1:
    >>> exec(open('unitI.py').read())
    Please enter one to four tags: hi mom
    Sorry, no games match your criteria.
    
Test 2:
   >>> exec(open('unitI.py').read())
    Please enter one to four tags: Action

    There are 19 games matching your tags.
    ['AttackCat', 'Adventure', 'Action']
    ['BlinkyCat', 'RPG', 'Action']
    ['BorisCat', 'Casual', 'Action', 'Horror', 'Adventure', 'Funny']
    ['CalicoCat', 'Funny', 'Racing', 'Horror', 'Action', 'RPG']
    ['CatEye', 'Funny', 'Action', 'Casual', 'Arcade', 'Racing']
    ['CatFish', 'Casual', 'Adventure', 'Strategy', 'Action']
    ['CatSoup', 'Funny', 'Action', 'Horror']
    ['CatTales', 'Action', 'Funny', 'Casual']
    ['ChesireCat', 'Action', 'RPG', 'Strategy', 'Casual', 'Adventure']
    ['ColossalCat', 'Action', 'Puzzle', 'Simulation', 'Arcade']
    ['DancingCat', 'Action', 'Puzzle', 'Funny', 'Horror', 'Simulation']
    ['EpiCat', 'Action', 'Horror', 'Arcade', 'Simulation', 'Casual']
    ['FatCats', 'Puzzle', 'Adventure', 'Action']
    ['HelloKitty', 'Funny', 'Puzzle', 'Casual', 'Simulation', 'Action']
    ['MagicCat', 'Funny', 'Action', 'Puzzle', 'Adventure', 'Simulation']
    ['PaddingtonCat', 'Strategy', 'Action']
    ['QuixoticCat', 'Indie', 'Arcade', 'Action', 'Casual', 'Strategy']
    ['SchrodingerCat', 'RPG', 'Action', 'Puzzle', 'Simulation']
    ['SleepyCat', 'Strategy', 'Simulation', 'Puzzle', 'Arcade', 'Action']
    
Test 3:
    >>> exec(open('unitI.py').read())
    Please enter one to four tags: Adventure Arcade

    There are 4 games matching your tags.
    ['CatatonicCat', 'Adventure', 'Arcade', 'Casual', 'Puzzle', 'Simulation']
    ['ElectricCat', 'Arcade', 'Horror', 'Adventure', 'Casual', 'Funny']
    ['ObtuseCat', 'Strategy', 'Adventure', 'Arcade', 'Casual']
    ['TomCat', 'Simulation', 'Arcade', 'Horror', 'Adventure', 'Funny']
    
Test 4:
   >>> exec(open('unitI.py').read())
    Please enter one to four tags: Casual Funny Horror

    There are 2 games matching your tags.
    ['BorisCat', 'Casual', 'Action', 'Horror', 'Adventure', 'Funny']
    ['ElectricCat', 'Arcade', 'Horror', 'Adventure', 'Casual', 'Funny']
    
Test 5:
    >>> exec(open('unitI.py').read())
    Please enter one to four tags: Horror Indie Puzzle
    Sorry, no games match your criteria.
    
Test 6:
    >>> exec(open('unitI.py').read())
    Please enter one to four tags: Boardgame
    Sorry, no games match your criteria.
'''
