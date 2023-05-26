from anytree import Node, RenderTree
from myparser import parser
import myparser

input_code = '''
int x;
bool y;
y = true;
y = 3;
string x;
double z;
z = 23.2 + 4.3 * 2.0 / 2.3 + 4.0 * (3.4 + 2.4);
Print(x - false);
'''

parse_tree = parser.parse(input_code)

for pre, _, node in RenderTree(parse_tree):
    print(f'{pre}{node}')

print(f'\nSemantic errors: {myparser.semantic_errors}')  # Счётчик семантических ошибок
print(f'SYMBOL TABLE:\n{myparser.symbol_table}')  # Таблица символов
