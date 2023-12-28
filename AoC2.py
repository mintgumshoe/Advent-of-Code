# Advent of Code D2

def myFunc(gameLine): 
    isPossible = 1 # Set to 0 if the game is invalid
    space = gameLine.index(" ")
    colon = gameLine.index(":")
    
    gameID = gameLine[space+1:colon] # Pick out the game ID
    game = gameLine[colon+2:5000] # Cut out "Game X:" part
    grabs = game.split("; ") # Split game into grabs

    for grab in grabs:
        colorList = grab.split(", ") # Split grab into num & colors  
        for colors in colorList:
            space = colors.index(" ")
            numColor = colors[0:space]         # Pick out num of    
            curColor = colors[space+1:space+2] # and the letter of the color
            # Only 12 red cubes, 13 green cubes, and 14 blue cubes in the bag
            if curColor == "r": 
                if (int(numColor) > 12):
                    isPossible = False
                    break
            elif curColor == "g":
                if (int(numColor) > 13):
                    isPossible = False
                    break
            elif curColor == "b":
                if (int(numColor) > 14):
                    isPossible = False
                    break
    gameID = int(gameID)
    if isPossible:
        #print("Game " + str(gameID) + ": Pass")
        return gameID
    else:
        #print("Game " + str(gameID) + ": Fail")
        gameID = 0
        return gameID   
def theLowest(gameLine): 
    space = gameLine.index(" ")
    colon = gameLine.index(":")
    
    gameID = gameLine[space+1:colon] # Pick out the game ID
    game = gameLine[colon+2:5000] # Cut out "Game X:" part
    grabs = game.split("; ") # Split game into grabs

    minRed = minGreen = minBlue = 0
    for grab in grabs:
        colorList = grab.split(", ") # Split grab into num & colors  
        for colors in colorList:
            space = colors.index(" ")
            numColor = colors[0:space]         # Pick out num of    
            curColor = colors[space+1:space+2] # and the letter of the color
            # Find smallest possible amt of cubes in a game
            if curColor == "r": 
                if (int(numColor) > minRed):
                    minRed = int(numColor)
            elif curColor == "g":
                if (int(numColor) > minGreen):
                    minGreen = int(numColor)
            elif curColor == "b":
                if (int(numColor) > minBlue):
                    minBlue = int(numColor)
    power = minRed * minGreen * minBlue
    #print("Power of Game " + gameID + ": " + str(power))
    return power                

# --------------------------------------------------------- #
#             Advent of Code Day 2 - Part 1                 #
sumGames = 0 # += gameNum that isPossible
f = open("AoC2.txt")
for game in f:
    sumGames += myFunc(game)
f.close()
print(sumGames) # Expect Answer - 2563
#                                                           #
# --------------------------------------------------------- #

# --------------------------------------------------------- #
#             Advent of Code Day 2 - Part 2                 #
powa = 0
f = open("AoC2.txt")
for game in f:
    powa += theLowest(game)
f.close()
print(powa) # Expect Answer - 70768
#                                                           #
# --------------------------------------------------------- #