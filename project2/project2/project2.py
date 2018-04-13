import sys
import DES
import AES

# Checking user input
if len(sys.argv) < 6:
    print "You are missing arguments, check your input." 
    print "Format is: python cipher.py <CIPHER> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>"
else:
    arg1 = str(sys.argv[1])  #DES or AES
    arg2 = sys.argv[2]  #Key
    arg3 = str(sys.argv[3])  #ENC or DEC
    arg4 = sys.argv[4]  #input file
    arg5 = sys.argv[5]  #output file
    # DES Cipher
    if arg1 == 'DES':
        cipher_type = fileDES.classDES()
    # AES Cipher
    if arg1 == 'AES':
        cipher_type = fileAES.classAES()
    # Invalid Input
    else:
        print "Unrecognized cipher type, check your spelling and try again."
        exit()

    # Setting key from inputfile
    if cipher_type.setKey(arg2):
        inFile = open(arg4, "r")
        inputText = inFile.read()
        if arg3 == 'ENC':
            outputText = cipher_type.encrypt(inputText)
            outFile = open(arg5, "wb")
            outFile.write(outputText)
            outFile.close()
        elif arg3 == 'DEC':
            outputText = cipher_type.decrypt(inputText)
            outFile = open(arg5, "w")
            outFile.write(outputText)
            outFile.close()
        # Invalid user input
        else:
            print "Unrecognized coding type, did you want Encode or Decode?"
            exit()
        inFile.close()

        # Encryption and decryption messages for other cipher operations
        if arg3 == 'ENC':
            print "Encryption Complete. Stored in ", arg5
        else:
            print "Decryption Complete. Stored in ", arg5
    else:
        print "Key is incorrect check to ensure your key matches with the cipher type"