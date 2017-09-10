# Logan O'Connell
from math import sqrt

class RSA:
    p = 0
    q = 0
    N = 0
    oN = 0
    E = 0
    Ek = []
    Dk = []

    def start(self):
        print '\nWelcome to the RSA cryptosystem!'
        print 'Please enter two prime integers for the system.\n'

        self.p = input('P = ')
        self.q = input('Q = ')

        self.N = self.p * self.q
        print 'N = ' + str(self.N)

        self.E = self.findPrimeE()
        print 'E = ' + str(self.E)

        self.Ek.append(self.N)
        self.Ek.append(self.E)

        self.oN = (self.p - 1) * (self.q - 1)

        self.Dk.append(self.N)
        self.Dk.append(self.inverse(self.E, self.oN))

        print 'Encryption key = (' + str(self.Ek[0]) + ', ' + str(self.Ek[1]) + ")"

        wantsToEncrypt = True
        wantsToEncrypt = self.getInput()

        if wantsToEncrypt:
            encryptedStr = self.encrypt()
            print '\nEncrypted string: ' + encryptedStr

        else:
            decryptedStr = self.decrypt()
            print '\nDecrypted string: ' + decryptedStr

    def findPrimeE(self):
        counter = 5

        while True:
            foundPrime = True

            for x in range(2, int(sqrt(counter) + 1)):
                if counter % x == 0:
                    foundPrime = False
                    break

                elif counter == self.p or counter == self.p:
                    foundPrime = False
                    break

            if foundPrime:
                return counter

            counter += 1

    def getInput(self):
        answer = raw_input('\nEnter E/e if you\'d like to encrypt a string or D/d to decrypt a string: ')

        if answer == 'E' or answer == 'e':
            return True

        elif answer == 'D' or answer == 'd':
            return False

    def encrypt(self):
        strToEncrypt = raw_input('Enter the string you\'d like to encrypt: ')
        encryptedStr = ''

        for letter in strToEncrypt:
            letterNumber = ord(letter) - 97;
            newLetterNumber = (letterNumber ** self.Ek[1]) % self.Ek[0]
            encryptedStr += chr(newLetterNumber + 97)

        return encryptedStr

    def decrypt(self):
        strToDecrypt = raw_input('Enter the string you\'d like to decrypt')
        decryptedStr = ''

        for letter in strToDecrypt:
            letterNumber = ord(letter) - 97;
            newLetterNumber = (letterNumber ** self.Dk[1]) % self.Dk[0]
            decryptedStr += chr(newLetterNumber + 97)

        return decryptedStr

    def inverse(self, x, m):
        a, b, u = 0, m, 1

        while x > 0:
            q = b // x
            x, a, b, u = b % x, u, x, a - q * u

        if b == 1:
            return a % m

# Main
rsa = RSA()
rsa.start()