import ply.yacc as yacc
from lexer import tokens


class Node:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children or []
        self.value = value

    def __str__(self):
        if self.type == "VariableType":
            return self.value


def p_program(p):
    '''program : decllist'''
    p[0] = p[1]


def p_decllist(p):
    '''decllist : decl
                | decllist decl'''
    if len(p) == 2:
        p[0] = Node('DeclList', [p[1]])
    else:
        p[0] = Node('DeclList', p[1].children + [p[2]])


def p_decl(p):
    'decl : variabledecl'
    p[0] = Node('VarDecl', [p[1]])


def p_variabledecl(p):
    'variabledecl : variabletype ID SEMICOLON'
    p[0] = Node('Variable', [Node('VariableType', value=p[1]), Node('ID', value=p[2])])


def p_variabletype(p):
    '''variabletype : INT
                    | DOUBLE
                    | STRING
                    | BOOL'''
    p[0] = Node('VariableType', value=p[1])




def p_error(p):
    print("Syntax error")


parser = yacc.yacc()
