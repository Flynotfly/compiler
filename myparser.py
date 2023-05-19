import ply.yacc as yacc
from lexer import tokens


class Node:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children or []
        self.value = value

    def __str__(self):
        if self.type == "variabletype":
            return self.value


def p_program(p):
    '''program : decllist'''
    p[0] = p[1]


def p_decllist(p):
    '''decllist : decl
                | decllist decl'''
    if len(p) == 2:
        p[0] = Node('decllist', [p[1]])
    else:
        p[0] = Node('decllist', p[1].children + [p[2]])


def p_decl(p):
    'decl : variabletype ID SEMICOLON'
    p[0] = Node('decl', [Node('variabletype', value=p[1]), Node('identifier', value=p[2])])


def p_variabletype(p):
    '''variabletype : INT
                    | DOUBLE
                    | STRING
                    | BOOL'''
    p[0] = Node('variabletype', value=p[1])


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()
