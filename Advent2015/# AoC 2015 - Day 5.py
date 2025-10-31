# AoC 2015 - Day 5

with open('AdventCode/input.txt') as file1:
    santastrings = file1.readlines()
    print("Read santa's list")
    
def naughtyniceChecker(stringlist, part):
    nicecounter = 0
    for string in stringlist: 
        if (part == 1):
            check = nicestringcheckpt1(string)
        else: # Part 2
            check = nicestringcheckpt2(string)    
        
        if check == True:
            nicecounter += 1
        else:
            pass

    return nicecounter    


#####################################################
#                       Part One                    #
#####################################################

def nicestringcheckpt1(string):

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelCt = 0 # Min 3
    
    dblltr = False
    
    banned = ["ab", "cd", "pq", "xy"]
    hasBanned = False

    ## Run the checks here ##

    # Count the vowels
    for letter in string: 
        if letter in vowels: 
            vowelCt += 1

    # Check for double letters
    i = 0
    for i, letter in enumerate(string): 
        # If a letter has the same letter after it in the string, set bool to true
        try: 
            if ({letter} == {string[i+1]}):
                dblltr = True
        except: 
            pass
            
    # Check for banned string sets
    for str in banned: 
        # if one of the banned strings is found in this string, set bool to true
        if string.find(str) != -1:
            hasBanned = True
            break   

    # Return a bool based on if all conditions are met
    if (vowelCt < 3 or dblltr == False or hasBanned == True): 
        # If any conditions arent met the string is naughty
        return False
    else: 
        return True

#testlist = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
#print(f"Test Case - Expected Count: 2 - Actual Count: {naughtyniceChecker(testlist, 1)}")
#print(f"Part 1 - Nice Count: {naughtyniceChecker(santastrings, 1)}")

#####################################################
#                       Part Two                    #
#####################################################

def nicestringcheckpt2(string): 
    rule1 = False # contains any pair of letters that appear twice w/o overlapping 
    rule2 = False # contains one letter that repeats with one between them    
    
    # Rule 1: contains any pair of letters that appear twice w/o overlapping
    i = 0
    for i, letter in enumerate(string): 
        try: 
            pair = letter + string[i + 1] # Form a pair to check for
            # Search for a pair that isnt at the current index
            if string.find(pair) != -1 and string.find(pair) != i:
                rule1 = True
                break
        except Exception as e: 
            #print(f"Rule 1 Error - index {i}: {e}")
            pass 

    # Rule 2: contains one letter that repeats with one between them    
    i = 0
    for i, letter in enumerate(string): 
        try: 
            triple = string[i : i+3]
            if (triple[0] == triple[2] and triple[0] != triple[1]):
                rule2 = True
                break
        except Exception as e: 
            #print(f"Rule 2 Error - index {i}: {e}")
            pass

    # Return a bool 
    if (rule1 == True and rule2 == True):
        #print(f"Pass: {string}")
        return True 
    else: 
        return False

testlist = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy", "aaqqvjve", "aaqqvjvaa"] 
            #       Pass         Pass         Fail                  Fail            Fail        Pass
print(f"Test Case for Pt 2 - Expect: 3 - Actual: {naughtyniceChecker(testlist, 2)}")

print(f"Part 2 - Nice Count: {naughtyniceChecker(santastrings, 2)} ")