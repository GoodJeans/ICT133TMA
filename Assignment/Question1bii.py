 
def decryptPhoneNumber(theEncryptedPhoneArray, theKeyArray):
    decryptedPhoneNumberArray = [0] * (8)
    
    decryptedPhoneNumber = 0
    for idxPhone in range(0, 7 + 1, 1):
        if idxPhone > 4:
            idxKey = idxPhone % 5
        else:
            idxKey = idxPhone
        if theEncryptedPhoneArray[idxPhone] - theKeyArray[idxKey] < 0:
            decryptedPhoneNumberArray[idxPhone] = (theEncryptedPhoneArray[idxPhone] - theKeyArray[idxKey] + 10) % 10
        else:
            decryptedPhoneNumberArray[idxPhone] = (theEncryptedPhoneArray[idxPhone] - theKeyArray[idxKey]) % 10
    for idxPhone in range(0, 7 + 1, 1):
        decryptedPhoneNumber = decryptedPhoneNumberArray[idxPhone] + decryptedPhoneNumber * 10
    
    return decryptedPhoneNumber

def encryptPhoneNumber(thePhoneArray, theKeyArray):
    encryptedPhoneNumberArray = [0] * (8)
    
    encryptedPhoneNumber = 0
    for idxPhone in range(0, 7 + 1, 1):
        if idxPhone > 4:
            idxKey = idxPhone % 5
        else:
            idxKey = idxPhone
        encryptedPhoneNumberArray[idxPhone] = (thePhoneArray[idxPhone] + theKeyArray[idxKey]) % 10
    for idxPhone in range(0, 7 + 1, 1):
        encryptedPhoneNumber = encryptedPhoneNumberArray[idxPhone] + encryptedPhoneNumber * 10
    
    return encryptedPhoneNumber

def intToArray(theInteger, theIntegerArray, theLength):
    idx = theLength
    while idx > 0:
        theDigit = theInteger % 10
        theInteger = int(float(theInteger) / 10)
        theIntegerArray[idx - 1] = theDigit
        idx = idx - 1

# Main
thePhoneArray = [0] * (8)
theKeyArray = [0] * (5)
encryptedPhoneNumberArray = [0] * (8)

print("Enter the Phone Number ")
thePhoneMain = input()
print("Enter the Key ")
theKeyMain = input()
intToArray(int(thePhoneMain), thePhoneArray, 8)
intToArray(int(theKeyMain), theKeyArray, 5)
encryptedPhoneNumber = encryptPhoneNumber(thePhoneArray, theKeyArray)
print("The encrypted phone number is ", end='', flush=True)
print(encryptedPhoneNumber)
intToArray(encryptedPhoneNumber, encryptedPhoneNumberArray, 8)
decryptedPhoneNumber = decryptPhoneNumber(encryptedPhoneNumberArray, theKeyArray)
print("The decrypted phone number is ", end='', flush=True)
print(decryptedPhoneNumber)

