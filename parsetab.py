
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BAND BLEFT BNOT BOR BRIGHT BXOR DERLLAVE DERPAR DESIGUAL DIGUAL DIV DOUBLE DP ID IGUAL INTEGER IZQLLAVE IZQPAR MAYOR MAYORIGUAL MENOR MENORIGUAL MULTI NOT OR PCOMA PORCENTAJE RESTA STR SUMA SXOR VAR abs array char exit float goto if int main print unset xor\n        ltag : ltag tag linst\n             | tag linst\n     linst       :   linst  inst PCOMA\n                    | inst PCOMA  inst        :   asignacion\n                    |   iff\n                    |   jump\n                    |   printt\n                    |   extasignacion  :   VAR IGUAL exptag         :   ID DP\n                    |  main DPjump        :   goto IDiff         :   if IZQPAR exp DERPAR goto IDprintt     :   print IZQPAR va DERPARext     :   exitexp         : expa\n                    | expl\n                    | expra\n                    | expb\n                    | E\n    expl        : NOT E\n                    | E AND E\n                    | E OR E\n                    | E xor Eexpra        : E DIGUAL E\n                    | E DESIGUAL E\n                    | E MAYORIGUAL E\n                    | E MENORIGUAL E\n                    | E MAYOR E\n                    | E MENOR Eexpb        : BNOT E\n                    | E BAND E\n                    | E BOR E\n                    | E BXOR E\n                    | E BLEFT E\n                    | E BRIGHT Eexpa        : E SUMA E\n                    | E RESTA E\n                    | E MULTI E\n                    | E DIV EE           : ent\n                    | dou\n                    | va\n                    | str\n    \n        ent : INTEGER\n    \n        dou : DOUBLE\n    \n        str : STR\n    \n        va : VAR\n    '
    
_lr_action_items = {'ID':([0,1,6,15,20,22,27,86,],[3,3,-2,25,-1,-4,-3,87,]),'main':([0,1,6,20,22,27,],[4,4,-2,-1,-4,-3,]),'$end':([1,6,20,22,27,],[0,-2,-1,-4,-3,]),'VAR':([2,5,6,18,19,20,22,23,24,26,27,35,36,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[13,13,13,-11,-12,13,-4,28,28,28,-3,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'if':([2,5,6,18,19,20,22,27,],[14,14,14,-11,-12,14,-4,-3,]),'goto':([2,5,6,18,19,20,22,27,66,],[15,15,15,-11,-12,15,-4,-3,86,]),'print':([2,5,6,18,19,20,22,27,],[16,16,16,-11,-12,16,-4,-3,]),'exit':([2,5,6,18,19,20,22,27,],[17,17,17,-11,-12,17,-4,-3,]),'DP':([3,4,],[18,19,]),'PCOMA':([7,8,9,10,11,12,17,21,25,28,29,30,31,32,33,34,37,38,39,40,41,42,43,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,],[22,-5,-6,-7,-8,-9,-16,27,-13,-49,-10,-17,-18,-19,-20,-21,-42,-43,-44,-45,-46,-47,-48,-22,-32,-15,-38,-39,-40,-41,-23,-24,-25,-26,-27,-28,-29,-30,-31,-33,-34,-35,-36,-37,-14,]),'IGUAL':([13,],[23,]),'IZQPAR':([14,16,],[24,26,]),'NOT':([23,24,],[35,35,]),'BNOT':([23,24,],[36,36,]),'INTEGER':([23,24,35,36,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'DOUBLE':([23,24,35,36,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'STR':([23,24,35,36,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'SUMA':([28,34,37,38,39,40,41,42,43,],[-49,46,-42,-43,-44,-45,-46,-47,-48,]),'RESTA':([28,34,37,38,39,40,41,42,43,],[-49,47,-42,-43,-44,-45,-46,-47,-48,]),'MULTI':([28,34,37,38,39,40,41,42,43,],[-49,48,-42,-43,-44,-45,-46,-47,-48,]),'DIV':([28,34,37,38,39,40,41,42,43,],[-49,49,-42,-43,-44,-45,-46,-47,-48,]),'AND':([28,34,37,38,39,40,41,42,43,],[-49,50,-42,-43,-44,-45,-46,-47,-48,]),'OR':([28,34,37,38,39,40,41,42,43,],[-49,51,-42,-43,-44,-45,-46,-47,-48,]),'xor':([28,34,37,38,39,40,41,42,43,],[-49,52,-42,-43,-44,-45,-46,-47,-48,]),'DIGUAL':([28,34,37,38,39,40,41,42,43,],[-49,53,-42,-43,-44,-45,-46,-47,-48,]),'DESIGUAL':([28,34,37,38,39,40,41,42,43,],[-49,54,-42,-43,-44,-45,-46,-47,-48,]),'MAYORIGUAL':([28,34,37,38,39,40,41,42,43,],[-49,55,-42,-43,-44,-45,-46,-47,-48,]),'MENORIGUAL':([28,34,37,38,39,40,41,42,43,],[-49,56,-42,-43,-44,-45,-46,-47,-48,]),'MAYOR':([28,34,37,38,39,40,41,42,43,],[-49,57,-42,-43,-44,-45,-46,-47,-48,]),'MENOR':([28,34,37,38,39,40,41,42,43,],[-49,58,-42,-43,-44,-45,-46,-47,-48,]),'BAND':([28,34,37,38,39,40,41,42,43,],[-49,59,-42,-43,-44,-45,-46,-47,-48,]),'BOR':([28,34,37,38,39,40,41,42,43,],[-49,60,-42,-43,-44,-45,-46,-47,-48,]),'BXOR':([28,34,37,38,39,40,41,42,43,],[-49,61,-42,-43,-44,-45,-46,-47,-48,]),'BLEFT':([28,34,37,38,39,40,41,42,43,],[-49,62,-42,-43,-44,-45,-46,-47,-48,]),'BRIGHT':([28,34,37,38,39,40,41,42,43,],[-49,63,-42,-43,-44,-45,-46,-47,-48,]),'DERPAR':([28,30,31,32,33,34,37,38,39,40,41,42,43,44,45,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-49,-17,-18,-19,-20,-21,-42,-43,-44,-45,-46,-47,-48,66,67,-22,-32,-38,-39,-40,-41,-23,-24,-25,-26,-27,-28,-29,-30,-31,-33,-34,-35,-36,-37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ltag':([0,],[1,]),'tag':([0,1,],[2,5,]),'linst':([2,5,],[6,20,]),'inst':([2,5,6,20,],[7,7,21,21,]),'asignacion':([2,5,6,20,],[8,8,8,8,]),'iff':([2,5,6,20,],[9,9,9,9,]),'jump':([2,5,6,20,],[10,10,10,10,]),'printt':([2,5,6,20,],[11,11,11,11,]),'ext':([2,5,6,20,],[12,12,12,12,]),'exp':([23,24,],[29,44,]),'expa':([23,24,],[30,30,]),'expl':([23,24,],[31,31,]),'expra':([23,24,],[32,32,]),'expb':([23,24,],[33,33,]),'E':([23,24,35,36,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[34,34,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,]),'ent':([23,24,35,36,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'dou':([23,24,35,36,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'va':([23,24,26,35,36,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[39,39,45,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'str':([23,24,35,36,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ltag","S'",1,None,None,None),
  ('ltag -> ltag tag linst','ltag',3,'p_lista_tag','gramatica.py',153),
  ('ltag -> tag linst','ltag',2,'p_lista_tag','gramatica.py',154),
  ('linst -> linst inst PCOMA','linst',3,'p_lista_instrucciones','gramatica.py',166),
  ('linst -> inst PCOMA','linst',2,'p_lista_instrucciones','gramatica.py',167),
  ('inst -> asignacion','inst',1,'p_instruccion','gramatica.py',176),
  ('inst -> iff','inst',1,'p_instruccion','gramatica.py',177),
  ('inst -> jump','inst',1,'p_instruccion','gramatica.py',178),
  ('inst -> printt','inst',1,'p_instruccion','gramatica.py',179),
  ('inst -> ext','inst',1,'p_instruccion','gramatica.py',180),
  ('asignacion -> VAR IGUAL exp','asignacion',3,'p_asignacion','gramatica.py',185),
  ('tag -> ID DP','tag',2,'p_tag','gramatica.py',189),
  ('tag -> main DP','tag',2,'p_tag','gramatica.py',190),
  ('jump -> goto ID','jump',2,'p_jump','gramatica.py',193),
  ('iff -> if IZQPAR exp DERPAR goto ID','iff',6,'p_iff','gramatica.py',197),
  ('printt -> print IZQPAR va DERPAR','printt',4,'p_printt','gramatica.py',201),
  ('ext -> exit','ext',1,'p_exxit','gramatica.py',206),
  ('exp -> expa','exp',1,'p_expresion','gramatica.py',210),
  ('exp -> expl','exp',1,'p_expresion','gramatica.py',211),
  ('exp -> expra','exp',1,'p_expresion','gramatica.py',212),
  ('exp -> expb','exp',1,'p_expresion','gramatica.py',213),
  ('exp -> E','exp',1,'p_expresion','gramatica.py',214),
  ('expl -> NOT E','expl',2,'p_expresion_logica','gramatica.py',219),
  ('expl -> E AND E','expl',3,'p_expresion_logica','gramatica.py',220),
  ('expl -> E OR E','expl',3,'p_expresion_logica','gramatica.py',221),
  ('expl -> E xor E','expl',3,'p_expresion_logica','gramatica.py',222),
  ('expra -> E DIGUAL E','expra',3,'p_expresion_relacional','gramatica.py',225),
  ('expra -> E DESIGUAL E','expra',3,'p_expresion_relacional','gramatica.py',226),
  ('expra -> E MAYORIGUAL E','expra',3,'p_expresion_relacional','gramatica.py',227),
  ('expra -> E MENORIGUAL E','expra',3,'p_expresion_relacional','gramatica.py',228),
  ('expra -> E MAYOR E','expra',3,'p_expresion_relacional','gramatica.py',229),
  ('expra -> E MENOR E','expra',3,'p_expresion_relacional','gramatica.py',230),
  ('expb -> BNOT E','expb',2,'p_expresion_bit','gramatica.py',235),
  ('expb -> E BAND E','expb',3,'p_expresion_bit','gramatica.py',236),
  ('expb -> E BOR E','expb',3,'p_expresion_bit','gramatica.py',237),
  ('expb -> E BXOR E','expb',3,'p_expresion_bit','gramatica.py',238),
  ('expb -> E BLEFT E','expb',3,'p_expresion_bit','gramatica.py',239),
  ('expb -> E BRIGHT E','expb',3,'p_expresion_bit','gramatica.py',240),
  ('expa -> E SUMA E','expa',3,'p_expresion_aritmetica','gramatica.py',243),
  ('expa -> E RESTA E','expa',3,'p_expresion_aritmetica','gramatica.py',244),
  ('expa -> E MULTI E','expa',3,'p_expresion_aritmetica','gramatica.py',245),
  ('expa -> E DIV E','expa',3,'p_expresion_aritmetica','gramatica.py',246),
  ('E -> ent','E',1,'p_expr','gramatica.py',257),
  ('E -> dou','E',1,'p_expr','gramatica.py',258),
  ('E -> va','E',1,'p_expr','gramatica.py',259),
  ('E -> str','E',1,'p_expr','gramatica.py',260),
  ('ent -> INTEGER','ent',1,'p_expInt','gramatica.py',267),
  ('dou -> DOUBLE','dou',1,'p_expDou','gramatica.py',273),
  ('str -> STR','str',1,'p_expStr','gramatica.py',279),
  ('va -> VAR','va',1,'p_expVar','gramatica.py',285),
]
