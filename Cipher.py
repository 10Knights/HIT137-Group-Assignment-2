"HIT137 Assignment 2 - Question 2 - Cipher Script"
"This script is able to read a text file, encrypt the text, then decrypt it ensuring the decrypted text matches the original."

# First Shift integer is requested
shift1 = 0 # Defining shift so that it can be used in the while loop below.
while shift1 <= 0: # If the integer is less than or equal to zero it will reask for a value higher than zero
    shift1 = int(input("Enter First Cypher Number: ")) 
    if shift1 <= 0:
        print ("First cypher number must be greater than 0")
        
# Second integer value which works with the same input ideal.
shift2 = 0 # Defining shift so that it can be used in the while loop below.
while shift2 <= 0:
    shift2 = int(input("Enter Second Cypher Number: "))
    if shift2 <= 0:
        print("Secondary cypher number must be greater than 0")
    
input_path = input("Enter input file path: ") # Path the original text file is located.
encrypted_path = input("Enter output file path: ") # The location which the encrypted file is to be located.
decrypted_path = input("Enter decrypted output file path: ") # The location where the decrypted file will be saved.

"This first function encrypts the data"
# Defines the parameters of the function
def encrypt_file(shift1: int, shift2: int, input_path: str, encrypted_path: str) -> None:

    # These have been added in to simplify the character changes
    multiply = shift1 * shift2
    addition = shift1 + shift2
    square = shift2**2
    subtraction = shift1 - shift2
    
    with open(input_path, 'r') as file: # reads the input file
        content = file.read()

    encrypted = ""
    "This sequence converts the alpha / numerical character to it's ASCII code."
    "Applies the Shift but keeps it within a loop of ie a-n by using %."
    "Converts it back into it's character then inputs into the string."
    "Characters which are not in the groups below are left as they are."
    for char in content:
        if 'a' <= char <= 'n':
            encrypted += chr(ord('a') + (ord(char) - ord('a') + multiply) % 14)
        elif 'o' <= char <= 'z':
            encrypted += chr(ord('o') + (ord(char) - ord('o') - addition) % 12)
        elif 'A' <= char <= 'M':
            encrypted += chr(ord('A') + (ord(char) - ord('A') - shift1) % 13)
        elif 'N' <= char <= 'Z':
            encrypted += chr(ord('N') + (ord(char) - ord('N') + square) % 13)
        elif '0' <= char <= '9':
            encrypted += chr(ord('0') + (ord(char) - ord('0') + subtraction) % 10)
        
        else:
            encrypted += char         
    with open(encrypted_path, 'w') as file: # Writes the encrypted file to the desired location.
          file.write(encrypted)

encrypt_file(shift1, shift2, input_path, encrypted_path) # End the function.

"This function decrypts the previously encrypted file using the same method as above but in reverse."
def decrypt_file(shift1: int, shift2: int, encrypted_path: str, decrypted_path: str):
    multiply = shift1 * shift2
    addition = shift1 + shift2
    square = shift2**2
    subtraction = shift1 - shift2

    with open(encrypted_path, 'r') as file:
        encrypted = file.read()

    decrypted = ""
    
    for char in encrypted:
            if '0' <= char <= '9':
                decrypted += chr(ord('0') + (ord(char) - ord('0') - subtraction) % 10)
            elif 'N' <= char <= 'Z':
                decrypted += chr(ord('N') + (ord(char) - ord('N') - square) % 13)
            elif 'A' <= char <= 'M':
                decrypted += chr(ord('A') + (ord(char) - ord('A') + shift1) % 13)
            elif 'o' <= char <= 'z':
                decrypted += chr(ord('o') + (ord(char) - ord('o') + addition) % 12)
            elif 'a' <= char <= 'n':
                decrypted += chr(ord('a') + (ord(char) - ord('a') - multiply) % 14)
            else:
                decrypted += char
    with open(decrypted_path, 'w') as file: # Writes the decrypted file to the desired location.
        file.write(decrypted)
decrypt_file(shift1, shift2, encrypted_path, decrypted_path) # Ends the function

"""Verifies decription and verification process"""

def verify_files(input_path: str, decrypted_path: str) -> bool: # Defines both files within the function.

    with open(input_path, 'r') as original_file: # Reads original text.
        original_content = original_file.read()

    with open(decrypted_path, 'r') as decrypted_file: # Reads decrypted text.
        decrypted_content = decrypted_file.read()

    if original_content == decrypted_content: # Compares if the original text and the decrypted text are a match, if so, prints "Decryption Successful"
        print("Decryption successful")
        return True

    else:
        print("Decryption unsuccessful") # If the text are not a match, it returns "Decryption Unsuccessful"
        return False
verify_files(input_path, decrypted_path)
