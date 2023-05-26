import ply.yacc as yacc
from lexer import tokens


symbol_table = {}
semantic_errors = 0

quadruples = []
next_temp = 0


def new_temp():
    global next_temp
    temp = f"t{next_temp}"
    next_temp += 1
    return temp


def add_sem_error():
    global semantic_errors
    semantic_errors += 1


def new_quadruple(operator, operand1, operand2, result):
    quadruple = (operator, operand1, operand2, result)
    quadruples.append(quadruple)


class Node:
    def __init__(self, name, children=None, value=None, type=None):
        if children is None:
            children = []
        self.name = name
        self.children = children
        self.value = value
        self.type = type

    def __repr__(self):
        if self.value is None and self.type is None:
            return f'{self.name}'
        elif self.value and self.type is None:
            return f'{self.name} = {self.value}'
        elif self.value is None and self.type:
            return f'{self.name} [{self.type}]'
        else:
            return f'{self.name} = {self.value} [{self.type}]'


def p_program(p):
    'program : decllist'
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


def p_decl_prntstmnt(p):
    'decl : printstatement'
    p[0] = Node('PrintStmnt', [p[1]])


def p_variabledecl(p):
    'variabledecl : variabletype ID SEMICOLON'
    p[0] = Node('Variable', [p[1], Node('ID', value=p[2], type=p[1].value.lower())])

    variable_name = p[2]
    if variable_name in symbol_table:
        print(f"Semantic error: Variable '{variable_name}' already declared.")
        add_sem_error()
    else:
        symbol_table[variable_name] = p[1].value

    new_quadruple("Declare", p[1].value, None, p[2])


def p_variabletype(p):
    '''variabletype : INT
                    | DOUBLE
                    | STRING
                    | BOOL'''
    p[0] = Node('VariableType', value=p[1])


def p_statement(p):
    'statement : ID EQUAL expression SEMICOLON'

    variable_name = p[1]

    if variable_name not in symbol_table:
        print(f"Semantic error: Variable '{variable_name}' is not declared.")
        add_sem_error()
        p[0] = Node('IdEqual', [Node('ID', value=p[1]), p[3]])
    else:
        p[0] = Node('IdEqual', [Node('ID', value=p[1], type=symbol_table[variable_name]), p[3]])
        assigned_type = symbol_table[variable_name]
        expression_type = p[3].type

        if assigned_type != expression_type:
            print(f"Semantic error: Type mismatch in assignment of variable '{variable_name}'.")
            add_sem_error()

    new_quadruple("=", p[3].value, None, p[1])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_number(p):
    'factor : const'
    p[0] = p[1]


def p_factor_id(p):
    'factor : ID'

    variable_name = p[1]
    if variable_name not in symbol_table:
        print(f"Semantic error: Variable '{variable_name}' is not declared.")
        add_sem_error()
        p[0] = Node('ID', value=p[1])
    else:
        p[0] = Node('ID', value=p[1], type=symbol_table[variable_name])


def p_const_int(p):
    'const : INT_CONST'
    p[0] = Node('const', value=p[1], type='int')


def p_const_double(p):
    'const : DOUBLE_CONST'
    p[0] = Node('const', value=p[1], type='double')


def p_const_string(p):
    'const : STRING_CONST'
    p[0] = Node('const', value=p[1], type='string')


def p_const_bool(p):
    'const : BOOL_CONST'
    p[0] = Node('const', value=p[1], type='bool')


def p_expression_plus(p):
    'expression : expression PLUS term'

    if p[1].type == p[3].type and (p[1].type == "int" or p[1].type == "double" or p[1].type == "string"):
        p[0] = Node('Plus', [p[1], p[3]], type=p[1].type)
    else:
        print("Semantic error: Unexpected expression type")
        add_sem_error()
        p[0] = Node('Plus', [p[1], p[3]])

    result = new_temp()
    p[0].value = result
    new_quadruple("+", p[1].value, p[3].value, result)


def p_expression_minus(p):
    'expression : expression MINUS term'

    if p[1].type == p[3].type and (p[1].type == "int" or p[1].type == "double"):
        p[0] = Node('Minus', [p[1], p[3]], type=p[1].type)
    else:
        print("Semantic error: Unexpected expression type")
        add_sem_error()
        p[0] = Node('Minus', [p[1], p[3]])

    result = new_temp()
    p[0].value = result
    new_quadruple("-", p[1].value, p[3].value, result)


def p_term_multiply(p):
    'term : term TIMES factor'

    if p[1].type == p[3].type and (p[1].type == "int" or p[1].type == "double"):
        p[0] = Node('Multiply', [p[1], p[3]], type=p[1].type)
    else:
        print("Semantic error: Unexpected expression type")
        add_sem_error()
        p[0] = Node('Multiply', [p[1], p[3]])

    result = new_temp()
    p[0].value = result
    new_quadruple("*", p[1].value, p[3].value, result)


def p_term_divide(p):
    'term : term DIVIDE factor'

    if p[1].type == p[3].type and (p[1].type == "int" or p[1].type == "double"):
        p[0] = Node('Divide', [p[1], p[3]], type=p[1].type)
    else:
        print("Semantic error: Unexpected expression type")
        add_sem_error()
        p[0] = Node('Divide', [p[1], p[3]])

    result = new_temp()
    p[0].value = result
    new_quadruple("/", p[1].value, p[3].value, result)


def p_factor_paren(p):
    'factor : LEFT_PAREN expression RIGHT_PAREN'
    p[0] = p[2]


def p_printstatement(p):
    'printstatement : PRINT LEFT_PAREN expression RIGHT_PAREN SEMICOLON'
    p[0] = Node('Print', [p[3]], type=p[3].type)
    if p[3].type is None:
        print('Semantic error: Unexpected expression type in print statement')
        add_sem_error()

    new_quadruple("Print", p[3].value, None, None)


def p_error(p):
    if p:
        print(f"Syntax error at token {p.value} on line {p.lineno}")
    else:
        print("Syntax error: Unexpected end of input")


parser = yacc.yacc()
