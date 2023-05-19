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


def p_decl_variabledecl(p):
    'decl : variabledecl'
    p[0] = Node('VarDecl', [p[1]])


def p_decl_statement(p):
    'decl : statement'
    p[0] = Node('Statement', [p[1]])


def p_variabledecl(p):
    'variabledecl : variabletype ID SEMICOLON'
    p[0] = Node('Variable', [p[1], Node('ID', value=p[2])])


def p_variabletype(p):
    '''variabletype : INT
                    | DOUBLE
                    | STRING
                    | BOOL'''
    p[0] = Node('VariableType', value=p[1])



def p_statement(p):
    'statement : ID EQUAL expression SEMICOLON'
    p[0] = Node('IdEqual', [Node('ID', value=p[1]), p[3]])

def p_expression_term(p):
    'expression : term'
    p[0] = Node('Term', [p[1]])


def p_term_factor(p):
    'term : factor'
    p[0] = Node('Factor', [p[1]])


def p_factor_number(p):
    'factor : const'
    p[0] = p[1]


def p_factor_id(p):
    'factor : ID'
    p[0] = Node('ID', value=p[1])

def p_const(p):
    '''const : INT_CONST
             | DOUBLE_CONST
             | STRING_CONST
             | BOOL_CONST'''
    p[0] = Node('const', value=p[1])


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = Node('PlusExp', [p[1], p[3]])


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = Node('MinusExp', [p[1], p[3]])


def p_term_multiply(p):
    'term : term TIMES factor'
    p[0] = Node('MultiplyFactor', [p[1], p[3]])


def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = Node('DivideFactor', [p[1], p[3]])


def p_factor_paren(p):
    'factor : LEFT_PAREN expression RIGHT_PAREN'
    p[0] = Node('ParenExp', [p[2]])


def p_error(p):
    if p:
        print(f"Syntax error at token {p.value} on line {p.lineno}")
    else:
        print("Syntax error: Unexpected end of input")


parser = yacc.yacc()
