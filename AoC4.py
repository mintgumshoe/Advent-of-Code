# Advent of Code D4
def myFunc(card):
    colon = card.index(":")
    pipe = card.index("|")
    gameID = card[card.index(" ")+1:colon]
    
    winHalf = card[colon+1:pipe] 
    myHalf = card[pipe+1:1000]     
    winNums = winHalf.split(" ") 
    myNums = myHalf.split(" ") 
    
    # Clean out extra spaces
    myNums = [x for x in myNums if x.strip()]
    winNums = [x for x in winNums if x.strip()]
    
    matches = 0
    # Match Checker #
    #print("Checking for Game " + gameID) 
    for num in myNums:
        for win in winNums:
            if int(num) == int(win):
                #("Match! " + num + " " + win)
                matches += 1
    
    # Convert wins to points 
    points = matches
    if matches > 2:
        points = matches * 2
    print("Game " + gameID + " adds " + str(points) + " points")
    return points


# --------------------------------------------------------- #
#             Advent of Code Day 4 - Part 1                 #
sumPts = 0
f = open("test.txt")    # AoC4 or test text files
for card in f:
    sumPts += myFunc(card)

f.close()
print("Total Points: " + str(sumPts)) # Expect Answer - not 1463
#                                                           #
# --------------------------------------------------------- #
