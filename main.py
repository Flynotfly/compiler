from lexer import lexer
from myparser import parser

input_code = '''
int x;
int y;
bool z;'''

parse_tree = parser.parse(input_code)


def print_tree(node, level=0):
    print('\t' * level + node.type)
    if node.value:
        print('\t' * (level + 1) + 'Value:', node.value)
    for child in node.children:
        print_tree(child, level + 1)


print_tree(parse_tree)
