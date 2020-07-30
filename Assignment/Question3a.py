import random 
'''Function to choose one alphabet'''
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

'''Function to get secret code'''
def getSecretCode(base1, base2): 
    secretCode = ""
    for i in range(4): 
        chosenLetter = chooseOneLetter(base1, base2)
        secretCode += chosenLetter
    return secretCode
'''Function to check if there is a duplicate alphabet'''
def checkDuplicate(elements):
    duplicates = []
    for item in elements:
        if elements.count(item) > 1:
            duplicates.append(item)
#         print(duplicates)
    return duplicates

'''Function to check if player wants to play again '''
def guessCorrect():
    playAgain = input(("Do you want to play again? Y to play again:")).lower()
    if(playAgain == 'y'):
        print("play again..")
        return True
    else:
        print("Application ends")
        exit()
        
'''Function for player to enter guess'''
def makeAGuess():
    guess = input("Enter a guess to continue or RETURN to quit:")
    guess = guess.lower()
    return guess

'''Function to checck if player entered secret code is valid'''
def checkValid():
    while True:
        guess = makeAGuess()
        invalidChars = ['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        outOfRangeresult = any(elem in invalidChars for elem in guess)
        resultOfDuplicate = checkDuplicate(guess)
        if(len(guess)<4 or len(guess)>4  or outOfRangeresult or len(resultOfDuplicate)>1):
            print("Please enter 4 unique letters, A to H")
        else:
            break
    return guess

def inputValue(secretCode):
    secretCode = secretCode.lower()
    playAgainBol = True
    correctAlpha = [None, None, None, None]
    wrongPosition = {}
#     secretCode = "cdba"# for checking
    print(secretCode)
    attempts = 0
    while playAgainBol:
        try:
            guess = checkValid()
            attempts+=1
            if guess in secretCode:
                print("Your guess is correct!")
                return guessCorrect() 
                
            elif(guess==""):
                break
            else:
                for k, v in enumerate(guess):  #For loop to get key value pair from list
                    if v in secretCode:         #To check if value from guess is inside secret code
                        if v == secretCode[k]:  #To check if secretcode is at the same position  
                            correctAlpha[k] = v #To store value inside the correct Alphabet
                        else:
                            if v in wrongPosition:    #if alphabet is in the wrong position
                                wrongPosition[v] += 1  #Increment value by 1 if guess is in wrong position
                            else:
                                wrongPosition[v] = 1   
                            
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
        print(secretCode)
        cont = inputValue(secretCode)
        
main()   
