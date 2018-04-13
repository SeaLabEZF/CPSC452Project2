from Crypto.Cipher import AES

#AES key must be either 16, 24, or 32 bytes long (Goffman's rubric specifies using 128 bit key (16 bytes) for AES)

class classAES:
  #Set Key Function
  def setKey(self, theKey):
    #write an if statement to make sure key is 128 bits (16 bytes) long
    self.key = theKey
    return True

  #Encrypt Function
  def encrypt(self, plaintext):
    obj1 = AES.new(self.key, AES.MODE_ECB)
    ciphertext = obj1.encrypt(plaintext)
    return ciphertext

  #Decrypt Function
  def decrypt(self, ciphertext):
    obj2 = AES.new(self.key, AES.MODE_ECB)
    outputBytes = obj2.decrypt(ciphertext)
    outputString = str(outputBytes)
    return outputString
