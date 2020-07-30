import random 

def chooseOneLetter(base1, base2): 
    ratio = 10 
    seed = int(random.uniform(0, ratio * len(base1) + len(base2)))#generates a uniform number from 0 to 60
    if seed < ratio * len(base1): #if generated uniform value, 0 to 60 is less than 30
        chosenLetter = base1[int(seed / ratio)]  
        base1.remove(chosenLetter)
    else :
        chosenLetter = base2[(seed - ratio * len(base1))]  
        base2.remove(chosenLetter) 
    return chosenLetter 

def getSecretCode(base1, base2): 
    secretCode = ""
    for i in range(4): 
        chosenLetter = chooseOneLetter(base1, base2)
        secretCode += chosenLetter
    return secretCode

def checkDuplicate(elements):
    duplicates = []
    for item in elements:
        if elements.count(item) > 1:
            duplicates.append(item)
#         print(duplicates)
    return duplicates


def guessCorrect():
    playAgain = input(("Do you want to play again? Y to play again:")).lower()
    if(playAgain == 'y'):
        print("play again..")
        return True
    else:
        print("Application ends")
        exit()
        
def generateRandomness(alphabets):
    guess = ""
    character = random.choice(alphabets)
    alphabets.remove(character)
    guess += character
    
    
    return guess

def makeAGuess(uselessCharacter, computerMemory, correctAlpha, correctAlphaBol, alphabets):
    i = 0
    guess= ""
    alphabets = ['a','b','c','d','e','g','h']
    uselessList = []
    
    if(len(computerMemory)>=1):
            for k,v in computerMemory.items():
                alphabets.remove(computerMemory[k])
    
    if(len(uselessList)>=1):
        for i in range (uselessList):
            alphabets.remove(uselessList)
    
    if(len(uselessCharacter)>=1):
            for k,v in uselessCharacter.items():
                alphabets.remove(uselessCharacter[k])
                uselessList.append(uselessCharacter[k])
                for k,v in enumerate(uselessCharacter):
                    for c,b in enumerate(correctAlpha):
                        if (uselessCharacter[k] == correctAlpha[c] ):
#                             correctAlpha.remove(uselessCharacter[k])
                            correctAlpha[c](generateRandomness(alphabets))
                            
                
    
    if (correctAlphaBol == True):
        for k, v in enumerate(correctAlpha):
                if correctAlpha[k] in alphabets:
                    alphabets.remove(correctAlpha[k])
        for c, b in enumerate(correctAlpha):
            if(correctAlpha[c] == None):
                guess+= generateRandomness(alphabets)
        for f,g in enumerate(correctAlpha):
            if  correctAlpha[f] != None:
                guess += correctAlpha[f]   
        return guess, alphabets
    else:
        
        if(len(computerMemory)==3):
            while i<1:
                guess+= generateRandomness(alphabets)
                i+=1
        elif(len(computerMemory)==2):
            while i<2:
                guess+= generateRandomness(alphabets)
                i+=1
        elif(len(computerMemory)==1):
            while i<3:
                guess+= generateRandomness(alphabets)
                i+=4
        else:
            while i<4:
                guess += generateRandomness(alphabets)
                i+=1
        for k,v in computerMemory.items():
            guess+=computerMemory[k]
        print("guess is {}".format(guess))
        guess="ebcd"
    return guess, alphabets

def checkValid(uselessCharacter, computerMemory, correctAlpha, correctAlphaBol, alphabets):
    while True:

        guess, alphabets = makeAGuess(uselessCharacter, computerMemory, correctAlpha, correctAlphaBol, alphabets)
        invalidChars = ['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        outOfRangeresult = any(elem in invalidChars for elem in guess)
        resultOfDuplicate = checkDuplicate(guess)
        if(len(guess)<4 or len(guess)>4  or outOfRangeresult or len(resultOfDuplicate)>1):
            print("Please enter 4 unique letters, A to H")
        else:
            break
    return guess, alphabets
  
def inputValue(secretCode):
    correctAlphaBol = False
    computerMemory = {}
    uselessCharacter = {}
    secretCode = secretCode.lower()
    playAgainBol = True
    correctAlpha = [None, None, None, None]
    wrongPosition = {}
    secretCode = "abcd"  #for checking
    attempts = 0
    alphabets = ['a','b','c','d','e','g','h']
    while playAgainBol:
        try:
            guess, alphabets2 = checkValid(uselessCharacter, computerMemory, correctAlpha, correctAlphaBol, alphabets )
            alphabets = alphabets2
            attempts+=1
            if guess in secretCode:
                print("Your guess is correct!")
                return guessCorrect() 
                
            elif(guess==""):
                break
            else:
                for k, v in enumerate(guess):
                    if v in secretCode:
                            if v == secretCode[k]:
                                correctAlpha[k] = v
                                correctAlphaBol = True

                            else:
                                computerMemory[k] = v
                                if v in wrongPosition:
                                    wrongPosition[v] += 1
                                    
                                else:
                                    wrongPosition[v] = 1
                                    
                    if v not in secretCode:
                        uselessCharacter[k]=v  
                    
                print("The guess is not correct, attempt no. {}".format(attempts))
                print("The correct letters in correct positions: {}" .format(correctAlpha))    
                print("The correct letters and the number of times found in incorrect positions: {}".format(wrongPosition))    
                        
        except ValueError:
            print("Error has occurred, please try again.")
        
def main():
    cont = True
    while cont:
        base1 = ["A", "B", "C", "D"]
        base2 = ["E", "F", "G", "H"]
        secretCode = getSecretCode(base1, base2)
        cont = inputValue(secretCode)
        
main()   
