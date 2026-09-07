# Recursive descent parser for Question 2
# Takes a token list from the tokeniser and builds a parse tree.
# Token format expected: list of (TYPE, VALUE) tuples, ending with ('END', None)
# TYPE is one of: NUM, OP, LPAREN, RPAREN, END
#
# Tree node format (nested tuples):
#   ('num', value)              - number literal
#   ('neg', operand)            - unary negation
#   ('bin', op, left, right)    - binary operation, op is '+','-','*','/','%','^'
#
# Grammar (lowest to highest precedence):
#   expr   -> term (('+'|'-') term)*
#   term   -> unary (('*'|'/'|'%'|implicit) unary)*
#   unary  -> '-' unary | power
#   power  -> primary ('^' unary)?
#   primary-> NUM | '(' expr ')'
#
# Implicit multiplication: allowed when a ')' is followed directly by a NUM
# or '(', or a NUM/')' is followed directly by '('. Plain NUM NUM adjacency
# is not implicit multiplication and is left as a parse error.

def parse(tokens):
    if not tokens:
        return None
    try:
        node, pos = parse_expression(tokens, 0)
    except (ValueError, IndexError):
        return None
    if tokens[pos][0] != 'END':
        return None
    return node


def parse_expression(tokens, pos):
    node, pos = parse_term(tokens, pos)
    while tokens[pos][0] == 'OP' and tokens[pos][1] in ('+', '-'):
        op = tokens[pos][1]
        pos += 1
        right, pos = parse_term(tokens, pos)
        node = ('bin', op, node, right)
    return node, pos


def parse_term(tokens, pos):
    node, pos = parse_unary(tokens, pos)
    while True:
        tok_type, tok_val = tokens[pos]
        if tok_type == 'OP' and tok_val in ('*', '/', '%'):
            pos += 1
            right, pos = parse_unary(tokens, pos)
            node = ('bin', tok_val, node, right)
        elif tok_type == 'LPAREN':
            right, pos = parse_unary(tokens, pos)
            node = ('bin', '*', node, right)
        elif tok_type == 'NUM' and tokens[pos - 1][0] == 'RPAREN':
            right, pos = parse_unary(tokens, pos)
            node = ('bin', '*', node, right)
        else:
            break
    return node, pos


def parse_unary(tokens, pos):
    tok_type, tok_val = tokens[pos]
    if tok_type == 'OP' and tok_val == '-':
        operand, pos = parse_unary(tokens, pos + 1)
        return ('neg', operand), pos
    return parse_power(tokens, pos)


def parse_power(tokens, pos):
    node, pos = parse_primary(tokens, pos)
    tok_type, tok_val = tokens[pos]
    if tok_type == 'OP' and tok_val == '^':
        right, pos = parse_unary(tokens, pos + 1)
        node = ('bin', '^', node, right)
    return node, pos


def parse_primary(tokens, pos):
    tok_type, tok_val = tokens[pos]
    if tok_type == 'NUM':
        return ('num', float(tok_val)), pos + 1
    if tok_type == 'LPAREN':
        node, pos = parse_expression(tokens, pos + 1)
        if tokens[pos][0] != 'RPAREN':
            raise ValueError('expected )')
        return node, pos + 1
    raise ValueError('unexpected token')


def tree_to_string(node):
    if node is None:
        return "ERROR"
    kind = node[0]
    if kind == 'num':
        val = node[1]
        if val == int(val):
            return str(int(val))
        return str(val)
    if kind == 'neg':
        return "(neg " + tree_to_string(node[1]) + ")"
    op, left, right = node[1], node[2], node[3]
    return "(" + op + " " + tree_to_string(left) + " " + tree_to_string(right) + ")"
