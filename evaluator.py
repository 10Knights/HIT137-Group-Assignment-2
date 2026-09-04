"""
HIT137 Assignment 2 - Question 2
Mathematical Expression Evaluator

This program:
tokenizer creates these token types:
NUM
OP
LPAREN
RPAREN
END
"""
# Josh
# Tokenisaton and formatting


def tokenize(expression: str) -> list:
    """
    Converts expressions into a list of valid tokens types only
    NUM,OP,LPAREN,RPAREN,END

    unary minus is stored as a OP- token rather than
    being included in number
    """

    tokens = []
    i = 0

    while i < len(expression):

        char = expression[i]

        # ignores spaces
        
        if char.isspace():
            i += 1
            continue

        
        if char.isdigit():

            start = i

            # read the integer portion and check for decimal points
            while i < len(expression) and expression[i].isdigit():
                i += 1

            if i < len(expression) and expression[i] == ".":

                i += 1

                # decimal points must have one digit after it
                if i >= len(expression) or not expression[i].isdigit():
                    raise ValueError("Invalid number")

                while i < len(expression) and expression[i].isdigit():
                    i += 1

            number_text = expression[start:i]

            if i < len(expression) and expression[i] == ".":
                raise ValueError("Invalid number")

            tokens.append(("NUM", number_text))
            continue
# Operators
        
        if char in "+-*/%^":

            tokens.append(("OP", char))
            i += 1
            continue

        
        # Opening and closing parenthesis
        if char == "(":

            tokens.append(("LPAREN", char))
            i += 1
            continue

        if char == ")":

            tokens.append(("RPAREN", char))
            i += 1
            continue

       
        # other characters are invalid
        
        raise ValueError("Invalid character")

    # Adding END token
    tokens.append(("END", ""))

    return tokens


def format_tokens(tokens: list) -> str:
    """
    Converts internal tokens into the required output format
    """

    formatted = []

    for token_type, value in tokens:

        if token_type == "END":
            formatted.append("[END]")

        else:
            formatted.append(f"[{token_type}:{value}]")

    return " ".join(formatted)
