reserved = {
    'void': 'VOID',
    'int': 'INT',
    'double': 'DOUBLE',
    'bool': 'BOOL',
    'string': 'STRING',
    'class': 'CLASS',
    'interface': 'INTERFACE',
    'null': 'NULL',
    'this': 'THIS',
    'extends': 'EXTENDS',
    'implements': 'IMPLEMENTS',
    'for': 'FOR',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'break': 'BREAK',
    'new': 'NEW',
    'NewArray': 'NEWARRAY',
    'Print': 'PRINT',
    'ReadInteger': 'READINTEGER',
    'ReadLine': 'READLINE'
}

tokens = ['PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'LESS_THAN', 'LESS_EQUAL',
          'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'EQUAL_EQUAL', 'NOT_EQUAL',
          'AND', 'OR', 'NOT', 'SEMICOLON', 'COMMA', 'PERIOD', 'LEFT_BRACKET',
          'RIGHT_BRACKET', 'LEFT_PAREN', 'RIGHT_PAREN', 'LEFT_BRACE', 'RIGHT_BRACE',
          'IDENTIFIER', 'COMMENT', 'COMMENT_MULTI', 'ARRAY',
          'DIM', 'ID', 'INT_CONST', 'DOUBLE_CONST', 'BOOL_CONST', 'STRING_CONST'] + list(reserved.values())

# Tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_LESS_THAN = r'<'
t_LESS_EQUAL = r'<='
t_GREATER_THAN = r'>'
t_GREATER_EQUAL = r'>='
t_EQUAL = r'='
t_EQUAL_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_SEMICOLON = r';'
t_COMMA = r','
t_PERIOD = r'\.'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_ARRAY = r'\[]'

# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_NUMBER(t):
    r'(?:0[xX][0-9a-fA-F]+|\d+\.\d+(?:[eE][-+]?\d+)?|\d+(?:\.\d*)?(?:[eE][-+]?\d+)?)'

    if 'x' in t.value or 'X' in t.value:
        t.value = int(t.value, 16)
        t.type = 'INT_CONST'
    elif '.' in t.value or 'e' in t.value or 'E' in t.value:
        t.value = float(t.value)
        t.type = 'DOUBLE_CONST'
    else:
        t.value = int(t.value)
        t.type = 'INT_CONST'
    return t

def t_BOOL_CONST(t):
    r'(true|false)'
    t.value = 'true' if t.value == 'true' else 'false'
    t.type = 'BOOL_CONST'
    return t

def t_STRING_CONST(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = str(t.value[1:-1])
    t.type = 'STRING_CONST'
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if len(t.value) > 31:
        print(f"ERROR: Identifier '{t.value}' is too long (max 31 characters)")
        t.lexer.skip(1)
    else:
        t.type = reserved.get(t.value, 'ID')
        return t


def t_comment(t):
    r'\/\/.*'
    pass  # ignore the comment


def t_comment_multi(t):
    r'\/\*[\s\S]*?\*\/'
    pass  # ignore the comment


def t_eof_COMMENT_MULTI(token):
    r'\/\*[\s\S]*$'
    # If the file ends with an unclosed multi-line comment, raise an exception
    raise Exception("Unclosed multi-line comment at end of file")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Build the lexer
import ply.lex as lex

lexer = lex.lex()

# TESTPATH = 'C:/Users/alter/Downloads/lexer_tests'
#
# import os
#
# def pair_files(folder_path):
#     file_pairs = []
#     file_names = os.listdir(folder_path)
#     for name in file_names:
#         if name.endswith('.frag'):
#             pair_name = name[:-5] + '.out'
#             if pair_name in file_names:
#                 file_pairs.append((name, pair_name))
#     return file_pairs
#
# FILEPATHS = pair_files(TESTPATH)
#
# for FILES in FILEPATHS:
#     testFile = open(f'{TESTPATH}/{FILES[0]}')
#     data = testFile.read()
#     testFileResult = open(f'{TESTPATH}/{FILES[1]}')
#     lexer.input(data)
#
#     print(f'                                       ----------{FILES[0]}----------\n')
#     while True:
#         tok = lexer.token()
#         if not tok: break
#         print ('%50s %10s' % (tok, f' |   {testFileResult.readline()[:-1]}'))
#     print('\n                                       ----------test----------')
#     print(data)