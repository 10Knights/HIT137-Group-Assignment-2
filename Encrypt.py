

shift1 = int(input("Enter First Cypher Number: ")) 
# If the integer is less than or equal to zero it will reask for a value higher than zero
if shift1 <=0:
    print ("First cypher number must be greater than 0") 
    shift1 = int(input("Enter Cypher Number Greater than Zero: "))

# Second integer value which works with the same input ideal.
shift2 = int(input("Enter Second Cypher Number: "))
if shift2 <=0:
    print("Secondary cypher number must be greater than 0")
    shift2 = int(input("Enter Second Cypher Number Greater than Zero: "))

input_path = r'C:\Users\Matt\OneDrive\Documents\HIT137\Python Files\raw_text.txt'
output_path = r'C:\Users\Matt\OneDrive\Documents\HIT137\Python Files\encrypt_text.txt'

# Defines the parameters of the function
def encrypt_file(shift1: int, shift2: int, input_path: str, output_path: str):

    # These have been added in to simplify the character changes
    multiply = shift1 * shift2
    addition = shift1 + shift2
    square = shift2**2
    subtraction = shift1 - shift2

    with open(input_path, 'r') as file: # reads the input file
        content = file.read()

    output = ""
    
    for char in content:
        if 'a' <= char <= 'n':
            output += chr(ord('a') + (ord(char) - ord('a') + multiply) % 14)
        elif 'o' <= char <= 'z':
            output += chr(ord('o') + (ord(char) - ord('o') - addition) % 12)
        elif 'A' <= char <= 'M':
            output += chr(ord('A') + (ord(char) - ord('A') - shift1) % 13)
        elif 'N' <= char <= 'Z':
            output += chr(ord('N') + (ord(char) - ord('N') + square) % 13)
        elif '0' <= char <= '9':
            output += chr(ord('0') + (ord(char) - ord('0') + subtraction) % 10)
        
        else:
            output += char         
    with open(output_path, 'w') as file:
          file.write(output)
    return output
result = encrypt_file(shift1, shift2, input_path, output_path)

print (result)          
