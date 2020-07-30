'''JB1984/Vigenere'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''Create text file'''
def createTextFile():    
    filename = input("Enter your file name (for demo purpose please enter \'encrypt' as file name:")
    key1stringenc = input("Enter first key: ")
    key1stringenc = key1stringenc.lower().replace(" ", "")
    myAlphabet = createAlphabet(key1stringenc)
    myAlphabetString = ''.join(myAlphabet)
    print("Your alphabet line is: " + myAlphabetString)
    key2stringenc = input("Enter second key: ")
    key2stringenc = key2stringenc.lower().replace(" ", "")
    myLines = createLines(key2stringenc, myAlphabet)
  
    for line in myLines:
    
        lineSting = ''.join(line)
        print("Your lines are: " + lineSting)
    
    passageInput = input("Enter text aka passage you wish to encrypt: ")
    passageInput = passageInput.lower().replace(" ", "")
    
    encryptedPassage = encryptPassage(passageInput, myAlphabet, myLines, key2stringenc)
    
    encryptedPassageString = ''.join(encryptedPassage)
    
    print("Your encrypted passage is: " + encryptedPassageString)
  
    with open(filename,"w") as file:
        file.write(encryptedPassageString)
        
    return filename

'''Read from text file and decrypt'''
def readTextFile(filename):
        with open(filename) as data:
            content = data.readline()
        
         # Decryption
        key1string = input("Enter first key: ")
        key1string = key1string.lower().replace(" ", "")

        myAlphabet = createAlphabet(key1string)

        myAlphabetString = ''.join(myAlphabet)

        print("Your alphabet line is: " + myAlphabetString)

        key2string = input("Enter second key: ")
        key2string = key2string.lower().replace(" ", "")

        myLines = createLines(key2string, myAlphabet)

        for line in myLines:
            lineSting = ''.join(line)
            print("Your lines are: " + lineSting)
        
        print("content is {}".format(content))
        encryptedPassageInput = str(content)
        encryptedPassageInput = encryptedPassageInput.lower().replace(" ", "")

        decryptedPassage = decryptPassage(encryptedPassageInput, myAlphabet, myLines, key2string)

        decryptedPassageString = ''.join(decryptedPassage)

        print("Your decrypted passage is: " + decryptedPassageString)

'''Encrypt passage entered'''
def encryptPassage(passage, myAlphabet, myLines, key2string):
  
    encryptedPassage = []
  
    counter = 0
  
    for letter in passage:
  
        index = myAlphabet.index(letter) - 1
  
        ourRow = myLines[counter]
  
        encLetter = ourRow[index]
  
        encryptedPassage.append(encLetter)
  
        if counter < len(key2string) - 1:
            counter += 1
        else:
            counter = 0
  
    return encryptedPassage

'''Decrypt passage'''
def decryptPassage(passage, myAlphabet, myLines, key2string):

    decryptedPassage = []

    counter = 0

    for letter in passage:

        ourRow = myLines[counter]

        index = ourRow.index(letter) + 1

        decLetter = myAlphabet[index]

        decryptedPassage.append(decLetter)

        if counter < len(key2string)-1:
            counter += 1
        else:
            counter = 0

    return decryptedPassage

def createAlphabet(key1string):
    topAlphabet = alphabet
    counter = 0
    for letter in key1string:
        topAlphabet.remove(letter)
        topAlphabet.insert(counter, letter)
        counter += 1
        
    return topAlphabet
  
# This function takes the second key and creates each new line "underneath" the previous one, it also modulos through
# the the alphabet created by the createAlphabet function starting with the each letter in the string.
def createLines(key2string, myAlphabet):
  
    listOfAlphabets = []
  
    for letter in key2string:
  
        index = myAlphabet.index(letter)+1
  
        counter = 0
  
        lineAlphabet = []
  
        while counter <= 25:
            lineAlphabet.append(myAlphabet[index % len(myAlphabet)])
            index += 1
            counter += 1
  
        listOfAlphabets.append(lineAlphabet)
  
    return listOfAlphabets



'''nazaninsbr/Vigenere-Cipher-Implementation'''
PLAIN_TEXT_FILE = './encrypt'
KEY = 'HUMAN'
 
def read_file(path):
    content = []
    with open(path, 'r') as f:
        for line in f:
            content.append(line)
    return content
 
def get_length(plain_text):
    l = 0
    for line in plain_text:
        for c in line:
            if not (c=='\n' or c==' '):
                l += 1
    return l
 
def create_key_of_the_same_length(l):
    key = ''
    i = 0
    while len(key)<l:
        key = key + KEY[i%len(KEY)]
        i += 1
    return key
 
def encrypt(plain_text):
    length_of_plain_text = get_length(plain_text)
    key = create_key_of_the_same_length(length_of_plain_text)
    char_index = 0
    encrypted = ''
    for line in plain_text:
        for c in line:
            if not (c=='\n' or c==' '):
                encrypted += chr((ord(key[char_index])+ord(c)))
                char_index += 1
            else:
                encrypted += c
    return encrypted
 
def decrypt(encrypted):
    length_of_encrypted_text = get_length(encrypted)
    key = create_key_of_the_same_length(length_of_encrypted_text)
    char_index = 0
    dencrypted = ''
    for line in encrypted:
        for c in line:
            if not (c=='\n' or c==' '):
                dencrypted += chr(abs((ord(key[char_index])-ord(c))))
                char_index += 1
            else:
                dencrypted += c
    return dencrypted
 
def main():
    filename = createTextFile()
    plain_text = read_file(PLAIN_TEXT_FILE)
    encrypted = encrypt(plain_text)
    print('Encrypted: ', encrypted)
    decrypted = decrypt(encrypted)
    print('Decrypted: ', decrypted)
    readTextFile(filename)
    
    
if __name__ == '__main__':
    main()