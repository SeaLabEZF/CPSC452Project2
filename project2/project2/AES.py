from Crypto.Cipher import AES

#AES key must be either 16, 24, or 32 bytes long (Goffman's rubric specifies using 128 bit key (16 bytes) for AES)

class classAES:
  #Set Key Function
  def setKey(self, key):
    #write an if statement to make sure key is 128 bits (16 bytes) long
    self.key = key
    return (len(key) == 16)

  #Encrypt Function
  def encrypt(self, plaintext):
    pad = 16 - (len(plaintext) % 16)
    data = plaintext + chr(pad)*pad
    aes = AES.new(self.key, AES.MODE_ECB)
    ciphertext = ''
    for i in range(0, len(data), 16):
        ciphertext += aes.encrypt(data[i:i+16])
    return ciphertext

  #Decrypt Function
  def decrypt(self, ciphertext):
    aes = AES.new(self.key, AES.MODE_ECB)
    plaintext = ''
    for i in range(0, len(ciphertext), 16):
        plaintext += aes.decrypt(ciphertext[i:i+16])
    return plaintext[:-ord(plaintext[len(plaintext) - 1])]
