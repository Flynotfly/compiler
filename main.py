from anytree import Node, RenderTree
from myparser import parser

input_code = '''
int x;
int y;
y = 5 + 4;
query = 93 * 63 - 2;
pork = "pig";
cake = true;
Print("2");
l = 93 * 34 / 24 - 43 + 2 * 4;
'''

parse_tree = parser.parse(input_code)


for pre, _, node in RenderTree(parse_tree):
    print(f'{pre}{node}')

