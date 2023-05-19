
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY BOOL BOOL_CONST BREAK CLASS COMMA COMMENT COMMENT_MULTI DIM DIVIDE DOUBLE DOUBLE_CONST ELSE EQUAL EQUAL_EQUAL EXTENDS FOR GREATER_EQUAL GREATER_THAN ID IDENTIFIER IF IMPLEMENTS INT INTERFACE INT_CONST LEFT_BRACE LEFT_BRACKET LEFT_PAREN LESS_EQUAL LESS_THAN MINUS MODULO NEW NEWARRAY NOT NOT_EQUAL NULL OR PERIOD PLUS PRINT READINTEGER READLINE RETURN RIGHT_BRACE RIGHT_BRACKET RIGHT_PAREN SEMICOLON STRING STRING_CONST THIS TIMES VOID WHILEprogram : decllistdecllist : decl\n                | decllist decldecl : variabletype ID SEMICOLONvariabletype : INT\n                    | DOUBLE\n                    | STRING\n                    | BOOL'
    
_lr_action_items = {'INT':([0,2,3,9,11,],[5,5,-2,-3,-4,]),'DOUBLE':([0,2,3,9,11,],[6,6,-2,-3,-4,]),'STRING':([0,2,3,9,11,],[7,7,-2,-3,-4,]),'BOOL':([0,2,3,9,11,],[8,8,-2,-3,-4,]),'$end':([1,2,3,9,11,],[0,-1,-2,-3,-4,]),'ID':([4,5,6,7,8,],[10,-5,-6,-7,-8,]),'SEMICOLON':([10,],[11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'decllist':([0,],[2,]),'decl':([0,2,],[3,9,]),'variabletype':([0,2,],[4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> decllist','program',1,'p_program','myparser.py',19),
  ('decllist -> decl','decllist',1,'p_decllist','myparser.py',24),
  ('decllist -> decllist decl','decllist',2,'p_decllist','myparser.py',25),
  ('decl -> variabletype ID SEMICOLON','decl',3,'p_decl','myparser.py',33),
  ('variabletype -> INT','variabletype',1,'p_variabletype','myparser.py',38),
  ('variabletype -> DOUBLE','variabletype',1,'p_variabletype','myparser.py',39),
  ('variabletype -> STRING','variabletype',1,'p_variabletype','myparser.py',40),
  ('variabletype -> BOOL','variabletype',1,'p_variabletype','myparser.py',41),
]
