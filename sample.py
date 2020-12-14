from pylexem.lexer import (
    Tokens,
    token_it,
    Lexer,
    Plain,
    NotPlain,
    InSet,
    NotInSet,
    Repeat,
    OR,
    AND,
    OPT,
    Any,
)

from pylexem.utils import RuleBuilder, Sanitizer

inp_text = """
int and uint numbers
-112 +110 110

float numbers
0. +0. .0 +.0 0.0 +0.1 0.0e-1 +0.0e-1 0.0e1 .0e1 -.0e1

"double quoted \t text" and 'double quoted text'

"""

tokens = RuleBuilder().add_all().build()
alltokens = Tokens().extend(tokens)

lexx = Lexer(alltokens, debug=not True, debugtime=True)

stream = lexx.tokenize(inp_text)

print("---")
print("---", "1 to 1 scanning result")
print("---")

for token in stream:
    print(token)

# remove the whitespace

stream = Sanitizer().whitespace(stream)

print("---")
print("---", "without whitespace")
print("---")

for token in stream:
    print(token)
