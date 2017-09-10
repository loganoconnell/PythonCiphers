# Logan O'Connell
class Caesar:
    def start(self):
        print '\nWelcome to the Caesar cryptosystem!'

        wantsToEncrypt = True
        wantsToEncrypt = self.getInput()

        if wantsToEncrypt:
            encryptedStr = self.encrypt()
            print '\nEncrypted string: ' + encryptedStr

        else:
            decryptedStr = self.decrypt()
            print '\nDecrypted string: ' + decryptedStr

    def getInput(self):
        answer = raw_input('\nEnter E/e if you\'d like to encrypt a string or D/d to decrypt a string: ')

        if answer == 'E' or answer == 'e':
            return True

        elif answer == 'D' or answer == 'd':
            return False

    def encrypt(self):
        strToEncrypt = raw_input('\nEnter the string you\'d like to encrypt: ')
        shift = input('Enter the shift you\'d like to encrypt with: ')
        encryptedStr = ''

        for letter in strToEncrypt:
            letterNumber = ord(letter) - 97;
            newLetterNumber = (letterNumber + shift) % 25
            encryptedStr += chr(newLetterNumber + 97)

        return encryptedStr

    def decrypt(self):
        strToDecrypt = raw_input('\nEnter the string you\'d like to decrypt: ')
        shift = input('Enter the shift you\'d like to decrypt with: ')
        decryptedStr = ''

        for letter in strToDecrypt:
            letterNumber = ord(letter) - 97;
            newLetterNumber = (letterNumber - shift) % 25
            decryptedStr += chr(newLetterNumber + 97)

        return decryptedStr

# Main
caesar = Caesar()
caesar.start()