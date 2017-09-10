class MorseCode:
    code = ['.-', '-..', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
            '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
            '..-', '...-', '.--', '-..-', '-.--', '--..',
            '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']

    def start(self):
        print '\nWelcome to the Morse Code cryptosystem!'

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
        encryptedStr = ''

        for letter in strToEncrypt:
            letterNumber = ord(letter) - 97;

            # If it's a space
            codeFromNumber = ''

            if letterNumber == -65:
                codeFromNumber = "    "

            elif letter.isdigit():
                letterNumber += 74
                codeFromNumber = self.code[letterNumber] + " "

            else:
                codeFromNumber = self.code[letterNumber] + " "

            encryptedStr += codeFromNumber

        return encryptedStr

    def decrypt(self):
        strToDecrypt = raw_input('\nEnter the string you\'d like to decrypt: ')
        decryptedStr = ''

        words = strToDecrypt.split("    ")

        for word in words:
            for letter in word.split():
                for index, item in enumerate(self.code):
                    if letter == item:
                        if index > 25:
                            decryptedStr += chr(index + 23)

                        else:
                            decryptedStr += chr(index + 97)

            decryptedStr += " "

        return decryptedStr
# Main
morseCode = MorseCode()
morseCode.start()