"""
ANALIZADOR DEL PROYECTO 1
    RICARDO ANTONIO MENÉNDEZ TOBÍAS
    201602916
"""
reservadas = {
    'main': 'main',
    'goto': 'goto',
    'int': 'int',
    'float': 'float',
    'char': 'char',
    'print': 'print',
    'array': 'array',
    'unset': 'unset',
    'if': 'if',
    'abs': 'abs',
    'xor': 'xor'

}

tokens = [
    'SUMA',
    'RESTA',
    'MULTI',
    'DIV',
    'PORCENTAJE',


    'NOT',
    'AND',
    'OR',
    'SXOR',

    'DIGUAL',
    'IGUAL',
    'DESIGUAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'MAYOR',
    'MENOR',

    'BNOT',
    'BAND',
    'BOR',
    'BXOR',
    'BLEFT',
    'BRIGHT',

    'IZQPAR',
    'DERPAR',
    'IZQLLAVE',
    'DERLLAVE',
    'PCOMA',
    'DP',
    'ID',
    'DOUBLE',
    'INTEGER',
    'VAR'
] + list(reservadas.values())

t_RESTA = r'-'
t_SUMA = r'\+'
t_MULTI = r'\*'
t_DIV = r'\/'
t_PORCENTAJE = r'\%'

t_NOT = r'\!'
t_AND = r'\&\&'
t_OR = r'\|\|'

t_IGUAL = r'\='
t_DIGUAL = r'\=\='
t_DESIGUAL = r'\!\='
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_MAYOR = r'\>'
t_MENOR = r'\<'

t_BNOT = r'\~'
t_BAND = r'\&'
t_BOR = r'\|'
t_BXOR = r'\^'
t_BLEFT = r'\<\<'
t_BRIGHT = r'\>\>'

t_IZQPAR = r'\('
t_DERPAR = r'\)'

t_PCOMA = r'\;'
t_DP = r'\:'
t_IZQLLAVE = r'\['
t_DERLLAVE = r'\]'


def t_DOUBLE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor no es parseable a decimal %d",t.value)
        t.value = 0
    return t    

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor no es parseable a integer %d",t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
    return t

def t_VAR(t):
    r'[\$][t|v|s|a][\d]+'
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter irreconocible! '%s'"% t.value[0])
    #meter a tabla de errores!
    t.lexer.skip(1)

#Creador del analizador lexico LEX
import ply.lex as lex 
lexer = lex.lex()
from pprint import pprint

from ast import *
from ast_operacion import *
from simbolos import *

def p_lista_tag(t):
    '''
        ltag : ltag tag linst
             | tag linst
    '''
    if(len(t)==3):
        t[0] = []
        t[0].append(Tag(t[1],t[2]))
        ts.añadirMetodo(Tag(t[1],t[2]))
    if(len(t)==4):
        t[0] = t[1]
        t[0].append(Tag(t[2],t[3]))
        ts.añadirMetodo(Tag(t[2],t[3]))

def p_lista_instrucciones(t):
    ''' linst       :   linst  inst PCOMA
                    | inst PCOMA '''
    if(len(t)==3):
        t[0] = []
        t[0].append(t[1])
    if(len(t)==4):
        t[0] = t[1]
        t[0].append(t[2])

def p_instruccion(t):
    ''' inst        :   asignacion
                    |   iff
                    |   jump'''
    t[0] = t[1]


def p_asignacion(t):
    'asignacion  :   VAR IGUAL exp'
    t[0] = Asignacion(t[1],t[3])
 
def p_tag(t):
    '''tag         :   ID DP
                    |  main DP'''
    t[0] = t[1]
def p_jump(t):
    'jump        :   goto ID'
    t[0] = Salto(t[2])

def p_iff(t):
    'iff         :   if IZQPAR exp DERPAR goto ID'

def p_expresion(t):
    '''exp         : expa
                    | expl
                    | expra
                    | expb
                    | E
    '''
    t[0] = t[1]

def p_expresion_logica(t):
    '''expl        : NOT E
                    | E AND E
                    | E OR E
                    | E xor E'''

def p_expresion_relacional(t):
    '''expra        : E DIGUAL E
                    | E DESIGUAL E
                    | E MAYORIGUAL E
                    | E MENORIGUAL E
                    | E MAYOR E
                    | E MENOR E'''
    if(t[2]=='=='):
        t[0] = Igual(t[1],t[3])

def p_expresion_bit(t):
    '''expb        : BNOT E
                    | E BAND E
                    | E BOR E
                    | E BXOR E
                    | E BLEFT E
                    | E BRIGHT E'''

def p_expresion_aritmetica(t):
    '''expa        : E SUMA E
                    | E RESTA E
                    | E MULTI E
                    | E DIV E'''
    if(t[2]=='+'):
        t[0] = Suma(t[1],t[3])
    elif(t[2]=='-'):
        t[0] = Resta(t[1],t[3])
    elif(t[2]=='/'):
        t[0] = Divi(t[1],t[3])
    elif(t[2]=='*'):
        t[0] = Multi(t[1],t[3])

def p_expr(t):
    '''E           : ent
                    | dou
                    | va
    '''
    t[0] = t[1]


def p_expInt(t):
    '''
        ent : INTEGER
    '''
    t[0] = NodoEntero(t[1])

def p_expDou(t):
    '''
        dou : DOUBLE
    '''
    t[0] = NodoDouble(t[1])

def p_expVar(t):
    '''
        va : VAR
    '''

def p_error(t):
    print("Error sintáctico en: '%s'" % t.value)

#Creador del Analisis Sintactico
import ply.yacc as yacc 
parser = yacc.yacc()
ts = TablaMetodos()
arbol = parser.parse('''
main:
    $t1 = 1 == 6;
    $t4 = 5/2;
a2:
    $t3 = 4*5;
    goto ende3;
a1:
    $t1 = 3.2 / 2.4;
    $t2 = 3 + 2;
    goto a2;
ende:
    $t1 = 5 + 3;
end2:
    $t5 =  1-5;
    $t6 = 10;
''')

nodo = ts.metodos.get("main")
if(nodo!=None):
    v = 0
    for x,y in ts.metodos.items(): 
        if(x=="main"):
            flag =1
        if(flag==1):
            v = y.ejecutar(ts,ts)
            if(v==1):
                break
    
for x,y in ts.variables.items():
    print(x, " = ", y.valor.value)
print("Se termino de ejecutar")