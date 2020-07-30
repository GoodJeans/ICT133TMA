import random

'''Function for choosing one letter '''
def chooseOneLetter (base1, base2):
    ratio = 10
    seed = int(random.uniform (0, ratio*len(base1)+len(base2)))
    if seed < ratio*len(base1):
        chosenLetter = base1[int(seed/ratio)]
        base1.remove(chosenLetter)
    else:
        chosenLetter = base2[(seed - ratio*len(base1))]
        base2.remove(chosenLetter)
    return chosenLetter

'''Function  for getting secretcode'''
def getSecretCode(base1, base2):
    secretCode = ""
    for i in range(4):
        chosenLetter = chooseOneLetter (base1, base2)
        secretCode += chosenLetter
#         print(secretCode)
    return secretCode

'''Main function'''
def main():
    secretCode = ""
    sum = 0
    count = 0 
    while count<1000:  #if count is less than 1000 continue looping
        base1 = ["A", "B", "C", "D"]
        base2 = ["E", "F", "G", "H"]
        secretCode += getSecretCode(base1, base2)   #get the secretcode by inputing base 1 and base 2 inside the function
        count +=1
    letters ="ABCDEFGH"
#     print(secretCode)
#     print(base1+base2)
    for c in letters:                   
        print("{}   {}".format(c, secretCode.count(c))) #print out the individual letters and the no of times they appeared
        sum+=int(secretCode.count(c))           #calculate the total sum of the letters
    print("Total of ABCDEFGH is {}".format(sum))
    
main()