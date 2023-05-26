from anytree import Node, RenderTree
from myparser import parser
import myparser

input_code = '''
int x;
Print(x);
'''

parse_tree = parser.parse(input_code)


for pre, _, node in RenderTree(parse_tree):
    print(f'{pre}{node}')

print(f'\nSYMBOL TABLE:\n{myparser.symbol_table}')