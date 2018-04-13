from Crypto.Cipher import DES
import binascii

class classDES:

    def setKey(self, key):
        check = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']
        for i in key:
            if i not in check:
                return False
        self.key = binascii.unhexlify(key)
        return (len(key) == 16)

    def encrypt(self, plainText):
        des = DES.new(self.key, DES.MODE_ECB)

        pad = 8 - (len(plainText) % 8)
        data = plainText + chr(pad)*pad

        cipherText = ''
        for i in range(0, len(data), 8):
            cipherText += des.encrypt(data[i:i+8])
        return cipherText

    def decrypt(self, cipherText):
        des = DES.new(self.key, DES.MODE_ECB)
        plaintext = ''
        for i in range(0, len(cipherText), 8):
            plaintext += des.decrypt(cipherText[i:i+8])
        return plaintext[:-ord(plaintext[len(plaintext) - 1:])]


