from Crypto.Cipher import DES
import binascii

class ClassDES:

    def __init__(self):
        self.key = ''

    def setKey(self, key):
        self.key = binascii.unhexlify(key)

    def encrypt(self, plainText):
        des = DES.new(self.key, DES.MODE_ECB)

        pad = 8 - (len(plainText) % 8)
        data = plainText + chr(pad)*pad

        print(len(data))
        c1 = des.encrypt(data)
        c3 = ''
        for i in range(0, len(data), 8):
            c3 += str(des.encrypt(data[i:i+8]))

        print len(c1)
        print c1
        print len(c3)
        print c3
        return c3

    def decrypt(self, cipherText):
        des = DES.new(self.key, DES.MODE_ECB)
        plaintext = des.decrypt(cipherText)
        unpad = plaintext[:-ord(plaintext[len(plaintext) - 1:])]
        return unpad

des = ClassDES()

key = '0123456789abcdef'
print  key
des.setKey(key)
text = 'abcdefghabcdefgh'
print text
print len(text)
cipher = des.encrypt(text)
print cipher
plain = des.decrypt(cipher)
print plain
print len(plain)
