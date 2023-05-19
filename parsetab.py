
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY BOOL BOOL_CONST BREAK CLASS COMMA COMMENT COMMENT_MULTI DIM DIVIDE DOUBLE DOUBLE_CONST ELSE EQUAL EQUAL_EQUAL EXTENDS FOR GREATER_EQUAL GREATER_THAN ID IDENTIFIER IF IMPLEMENTS INT INTERFACE INT_CONST LEFT_BRACE LEFT_BRACKET LEFT_PAREN LESS_EQUAL LESS_THAN MINUS MODULO NEW NEWARRAY NOT NOT_EQUAL NULL OR PERIOD PLUS PRINT READINTEGER READLINE RETURN RIGHT_BRACE RIGHT_BRACKET RIGHT_PAREN SEMICOLON STRING STRING_CONST THIS TIMES VOID WHILEprogram : decllistdecllist : decl\n                | decllist decldecl : variabledeclvariabledecl : variabletype ID SEMICOLONvariabletype : INT\n                    | DOUBLE\n                    | STRING\n                    | BOOL'
    
_lr_action_items = {'INT':([0,2,3,4,10,12,],[6,6,-2,-4,-3,-5,]),'DOUBLE':([0,2,3,4,10,12,],[7,7,-2,-4,-3,-5,]),'STRING':([0,2,3,4,10,12,],[8,8,-2,-4,-3,-5,]),'BOOL':([0,2,3,4,10,12,],[9,9,-2,-4,-3,-5,]),'$end':([1,2,3,4,10,12,],[0,-1,-2,-4,-3,-5,]),'ID':([5,6,7,8,9,],[11,-6,-7,-8,-9,]),'SEMICOLON':([11,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'decllist':([0,],[2,]),'decl':([0,2,],[3,10,]),'variabledecl':([0,2,],[4,4,]),'variabletype':([0,2,],[5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> decllist','program',1,'p_program','myparser.py',17),
  ('decllist -> decl','decllist',1,'p_decllist','myparser.py',22),
  ('decllist -> decllist decl','decllist',2,'p_decllist','myparser.py',23),
  ('decl -> variabledecl','decl',1,'p_decl','myparser.py',31),
  ('variabledecl -> variabletype ID SEMICOLON','variabledecl',3,'p_variabledecl','myparser.py',36),
  ('variabletype -> INT','variabletype',1,'p_variabletype','myparser.py',46),
  ('variabletype -> DOUBLE','variabletype',1,'p_variabletype','myparser.py',47),
  ('variabletype -> STRING','variabletype',1,'p_variabletype','myparser.py',48),
  ('variabletype -> BOOL','variabletype',1,'p_variabletype','myparser.py',49),
]
