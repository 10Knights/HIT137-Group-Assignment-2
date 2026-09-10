"""HIT137 Group 2 - Assignment 2 - Question 1 - Cipher Script
Member 1 – 10Knights - Joshua Sexton
Member 2 – Matt-HIT137 - Matthew Capel
Member 3 – cajohns99-a11y - Cameron Johns
Member 4 – Akai221- Dantae - Dantae Babic
This script is able to read raw_text.txt file, encrypt the text, then decrypt it ensuring the decrypted text matches the original."""

# First Shift integer is requested
shift1 = -1 # Defining shift so that it can be used in the while loop below.
while shift1 < 0: # If the integer is less than zero it will reask for a value of zero or greater
    shift1 = int(input("Enter 1st Cipher Number >= 0: ")) # Request an integer greater than or equal to zero
    if shift1 < 0: 
        print ("***Cipher number must be 0 or greater***") # The request for a value if the use inputs an integer less than zero (negative number)
        
# Second integer input which works the same as the previous input.
shift2 = -1 # Defining shift so that it can be used in the while loop below.
while shift2 < 0:
    shift2 = int(input("Enter 2nd Cypher Number >= 0: "))
    if shift2 < 0:
        print("***Cipher number must be 0 or greater***")

# Defines the files
input_path = "raw_text.txt" 
encrypted_path = "encrypted_text.txt"
decrypted_path = "decrypted_text.txt"

"This first function encrypts the data"
# Defines the parameters of the function
def encrypt_file(shift1: int, shift2: int, input_path: str, output_path: str) -> None:

    # These have been added in to simplify the character changes
    multiply = shift1 * shift2
    addition = shift1 + shift2
    square = shift2**2
    subtraction = shift1 - shift2
    
    with open(input_path, 'r') as file: # reads the input file
        content = file.read()

    encrypted = ""
    """This sequence converts the alpha / numerical character to it's ASCII code.
    Applies the Shift but keeps it within a loop of it's group ie a-n by using % 14.
    Converts it back into it's character then inputs into the string.
    Characters which are not in the groups below are left as they are."""
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
    with open(output_path, 'w') as file: # Writes the encrypted file encrypted_text.txt.
          file.write(encrypted)

encrypt_file(shift1, shift2, input_path, encrypted_path) # End of this function.

"""This function decrypts the previously encrypted file using the same method as above with the characters done in reverse order."""
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

"""This function compares the decrypted file vs raw text and verifies the encryption / decryption is correct."""
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
