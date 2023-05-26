from anytree import Node, RenderTree
from myparser import parser
import myparser
import csv

input_code = '''
int x;
bool y;
int z;

y = false;
Print(y);

z = 34;
x = 95 + 23 - z * 2;

double w;
w = 23.2 + 4.3 * 2.0 / 2.3 + 4.0 * (3.4 + 2.4);
Print(x - 56);
'''

parse_tree = parser.parse(input_code)

for pre, _, node in RenderTree(parse_tree):
    print(f'{pre}{node}')

print(f'\nSemantic errors: {myparser.semantic_errors}')  # Счётчик семантических ошибок


# Таблица символов
with open('C:/Git/Compiler/symbolTable.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Var', 'Type'])

    writer.writerows(myparser.symbol_table.items())


# Трехадресный код
with open('C:/Git/Compiler/three.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Operator", "Operand1", "Operand2", "Result"])

    for sequence in myparser.quadruples:
        writer.writerow(sequence)
