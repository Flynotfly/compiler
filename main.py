from anytree import Node, RenderTree
from myparser import parser
import myparser

input_code = '''
int x;
bool y;
y = true;

Print(x);
'''

parse_tree = parser.parse(input_code)

for pre, _, node in RenderTree(parse_tree):
    print(f'{pre}{node}')

print(f'\nSemantic errors: {myparser.semantic_errors}')  # Счётчик семантических ошибок
print(f'SYMBOL TABLE:\n{myparser.symbol_table}')  # Таблица символов
