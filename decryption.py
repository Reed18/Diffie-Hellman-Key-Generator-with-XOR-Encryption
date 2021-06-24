#Programming Activity #1 - CS Elec2 Computer Security and Cryptography
#Submitted by Reden Mar L. Bellen BSCS-3B
#Program for Decrypting XOR Encrypted message

#module for accessing and creating files
from pathlib import Path    
#scans the file where the encrypted message is
message = Path('encrypted_message.txt').read_text()
print("\nMessage to be decrypted:\n",message)
#the key will be from the file where it was stored during encryption
key = Path('key_file.txt').read_text()

#start of message decryption
decryptUni = ""
for i in range(0, len(message), 2):
    decryptUni += bytes.fromhex(message[i:i+2]).decode('utf-8')

decrypText = ""
keyItr = 0
#loop for scanning every encrypted character in the message
for i in range(len(decryptUni)):
    #The ord() function returns an integer representing the Unicode character
    #Definition from https://www.programiz.com/python-programming/methods/built-in/ord
    temp = ord(decryptUni[i]) ^ ord(key[keyItr])
    #generated value is converted back to a character via chr() function
    decrypText += chr(temp)
    keyItr += 1
    if keyItr >= len(key):
        #the key will be repeated until the whole message will be decrypted
        keyItr = 0
#the decrypted message will be stored in a file
output2=open('decrypted_message.txt','w')
print("{}".format(decrypText),file=output2)
#prints the encrypted message on the screen
print("Decrypted Message:\n",decrypText)
#closes the file acessed
output2.close()