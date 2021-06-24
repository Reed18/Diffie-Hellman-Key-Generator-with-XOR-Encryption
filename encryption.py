#Programming Activity #1 - CS Elec2 Computer Security and Cryptography
#Submitted by Reden Mar L. Bellen BSCS-3B
#Program applying Diffie-Hellman for Key Generation and applying the generated key in XOR Encryption
def main():
    #module for accessing and creating files
    from pathlib import Path
    #function for checking if input is int not a string or character
    def isNum(user_Input):
        #this loop will continually ask the user for input unless the condition is satisfied
        while True:
            try:
                input_value = int(input(user_Input))
            except ValueError:
                #will show if input is a character
                print("Please enter a valid number! ")
                continue
            if input_value < 0:
                #will show if input is float or negative
                print("Please enter a valid number! ")
                continue
            else:
                break
        return input_value
    #function for checking if the given number "p" is a prime or not 
    def isPrime(prime_num):
        if prime_num>1:
            #will proceed to for loop if the input was greater than 1
            for i in range(2,prime_num): #value of i starts from 2 to the value inputted by the user
                if (prime_num%i)==0: #searches for its factors
                    print(prime_num,"is not a prime number")
                    #displaying the factors found if number is not a prime
                    print(i, "times",prime_num//i,"is",prime_num)
                    main() #will be called to ask new input from user since the number isn't prime
            else:
                #if number is prime, the value will be stored as the value of p
                print(prime_num,"is chosen")

    #isNum function will be called to ask input p from user
    p=isNum("Please enter a number for p: ")
    #is called to check if the value of p is prime since p needs to be prime
    isPrime(p)

    #isNum function will be called to ask input g from user
    g=isNum("Please enter a number for g: ")
    #this loop checks if g is a root of p
    if g>p:
        print("Invalid! Please pick a lower number")
        #is called to restart asking user for input
        main()
    else:
        print(g, "is chosen")

    #isNum function will be called to ask input a from user
    a=isNum("Please enter a number for a: ")
    print(a, "is chosen")

    #isNum function will be called to ask input b from user
    b=isNum("Please enter a number for b: ")
    print(b, "is chosen")

    #prints the chosen values
    print("p = ", p)
    print("g = ", g)
    print("a = ", a)
    print("b = " ,b)

    #computes for public key of user 1
    P1=(g^a)%p
    print("Public Key of Person 1 is: " ,P1)

    #computes for public key of user 2
    P2=(g^b)%p
    print("Public Key of Person 2 is: " ,P2)

    #computes for public key of user 1 given the private key of user 2 
    P1_key=(P2^a)%p
    #computes for public key of user 2 given the private key of user 1 
    P2_key=(P1^b)%p

    #checks if user 1 and user 2 key matches
    if P1_key==P2_key:
        print("\nKey Agreement Sucess!")
    else:
        #if not will start asking for new inputs
        main()

    #scans the input file where the message is
    message = Path('input_file.txt').read_text()
    print("\nMessage to be encrypted:\n",message)

    #the key will be stored in a file to access for decryption
    key = Path('key_file.txt').read_text()

    #start of message encryption
    encryptHex = ""
    keyItr = 0
    #loop for scanning every character in the message and encrypting them with the key
    for i in range(len(message)):
        #The ord() function returns an integer representing the Unicode character
        #Definition from https://www.programiz.com/python-programming/methods/built-in/ord
        temp = ord(message[i]) ^ ord(key[keyItr])
        #zfill will add a 0 to every single letter making it a two letter pair
        encryptHex += hex(temp)[2:].zfill(2)
        keyItr += 1
        if keyItr >= len(key):
        #the key will be repeated until the whole message will be encrypted
            keyItr = 0
    #the encrypted message will be stored in a file
    output=open('encrypted_message.txt','w')
    print("{}".format(encryptHex),file=output)
    #prints the encrypted message on the screen
    print("\nEncrypted message:\n",encryptHex)
    #closes the file acessed
    output.close()
    #end of encryption
    exit()    
main()