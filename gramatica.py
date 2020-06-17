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
    'xor': 'xor',
    'exit': 'exit',
    'read': 'read'

}

tokens = [
    'SUMA',
    'RESTA',
    'MULTI',
    'DIV',
    'PORCENTAJE',
    'PUNTERO',


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
    'VAR',
    'STR'
] + list(reservadas.values())

t_RESTA = r'-'
t_SUMA = r'\+'
t_MULTI = r'\*'
t_DIV = r'\/'
t_PORCENTAJE = r'\%'

t_PUNTERO = r'\&'

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

def t_STR(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
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
    t.type = reservadas.get(t.value.lower(),'ID') 
    return t

def t_VAR(t):
    r'[\$](([t|v|s|a][\d]+)|sp|ra)'
    return t

def t_COMENTARIO(t):
    r'\#.*\n'
    t.lexer.lineno += 1

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter irreconocible! '%s'"% t.value[0])
    #meter a tabla de errores!
    erroresLexicos.append("Error Lexico: "+t.value[0]+"  en linea:  "+ str(int(t.lexer.lineno)))
    t.lexer.skip(1)

#Creador del analizador lexico LEX
import ply.lex as lex 
lexer = lex.lex()
from pprint import pprint

from ast import *
from ast_operacion import *
from simbolos import *

def p_s_tag(t):
    '''s    : ltag'''
    t[0] = Root(t[1])

def p_lista_tag(t):
    '''
        ltag : ltag tag linst
             | tag linst
    '''
    if(len(t)==3):
        t[0] = {}
        t[0][t[1]] = (Tag(t[1],t[2],t.lineno(1)))
    if(len(t)==4):
        t[0] = t[1]
        t[0][t[2]] = (Tag(t[2],t[3],t.lineno(1)))
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
                    |   jump
                    |   printt
                    |   ext
                    |   uns'''
    t[0] = t[1]

def p_unset(t):
    '''
        uns     :   unset IZQPAR va DERPAR
    '''
    t[0] = Unset(t[3],t.lineno(1))

def p_asignacion(t):
    'asignacion  :   var2 IGUAL exp'
    t[0] = Asignacion(t[1],t[3],t.lineno(1))
 
def p_var2(t):
    '''var2        :   VAR arr
                 |   VAR'''
    if(len(t)==3):
        t[0] = NodoVariable(t[1],t[2])
    else:
        t[0] = NodoVariable(t[1],None)

def p_tag(t):
    '''tag         :   ID DP
                    |  main DP'''
    t[0] = t[1]

def p_jump(t):
    'jump        :   goto ID'
    t[0] = Salto(t[2],t.lineno(1))

def p_iff(t):
    'iff         :   if IZQPAR exp DERPAR goto ID'
    t[0] = Si(t[3],t[6],t.lineno(1))

def p_printt(t):
    'printt     :   print IZQPAR E DERPAR'
    t[0] = Print(t[3],t.lineno(1))


def p_exxit(t):
    'ext     :   exit'
    t[0] = Exit()

def p_expresion(t):
    '''exp         : expa
                    | expl
                    | expra
                    | expb
                    | casteo
                    | E
                    | calls
    '''
    t[0] = t[1]

def p_casteo(t):
    '''
        casteo      : IZQPAR int DERPAR E
                    | IZQPAR float DERPAR E
                    | IZQPAR char DERPAR E
    '''
    if(t[2]=="int"):
        t[0] = Cast2Int(t[4])
    elif(t[2]=="float"):
        t[0] = Cast2Double(t[4])
    elif(t[2]=="char"):
        t[0] = Cast2Char(t[4])

def p_calls(t):
    '''
        calls       :  read IZQPAR DERPAR
                    |  array IZQPAR DERPAR
                    | PUNTERO VAR
    '''
    if(t[1]=="read"):
        t[0] = Leer()
    elif(t[1]=="array"):
        t[0] = Array()
    else:
        t[0] = NodoPuntero(t[2])

def p_expresion_logica(t):
    '''expl        : NOT E
                    | E AND E
                    | E OR E
                    | E xor E'''
    if(t[2]=='&&'):
        t[0] = And(t[1],t[3])
    if(t[2]=='||'):
        t[0] = Or(t[1],t[3])
    if(t[2]=='xor'):
        t[0] = Xor(t[1],t[3])

def p_expresion_relacional(t):
    '''expra        : E DIGUAL E
                    | E DESIGUAL E
                    | E MAYORIGUAL E
                    | E MENORIGUAL E
                    | E MAYOR E
                    | E MENOR E'''
    if(t[2]=='=='):
        t[0] = Igual(t[1],t[3])
    if(t[2]=='!='):
        t[0] = DesIgual(t[1],t[3])
    if(t[2]=='>'):
        t[0] = Mayor(t[1],t[3])
    if(t[2]=='<'):
        t[0] = Menor(t[1],t[3])
    if(t[2]=='>='):
        t[0] = MayorI(t[1],t[3])
    if(t[2]=='<='):
        t[0] = MenorI(t[1],t[3])

def p_expresion_bit(t):
    '''expb        : BNOT E
                    | E BAND E
                    | E BOR E
                    | E BXOR E
                    | E BLEFT E
                    | E BRIGHT E'''
    if(len(t)==3):
        t[0] = BNot(t[2])
    elif(t[2]=='&'):
        t[0] = BAnd(t[1],t[3])
    elif(t[2]=='|'):
        t[0] = BOr(t[1],t[3])
    elif(t[2]=='^'):
        t[0] = BXor(t[1],t[3])
    elif(t[2]=='<<'):
        t[0] = BLeft(t[1],t[3])
    elif(t[2]=='>>'):
        t[0] = BRight(t[1],t[3])

def p_expresion_aritmetica(t):
    '''expa        : E SUMA E
                    | E RESTA E
                    | E MULTI E
                    | abs IZQPAR E DERPAR
                    | E DIV E'''
    if(len(t)==5):
        t[0] = Absoluto(t[3])
    elif(t[2]=='+'):
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
                    | str
                    | RESTA E
    '''
    if(len(t)==3):
        t[0] = Rest(t[2])
    else:    
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

def p_expStr(t):
    '''
        str : STR
    '''
    t[0] = NodoCadena(t[1])

def p_expVar(t):
    '''
        va : VAR arr
            | VAR 
    '''
    if(len(t)==3):
        t[0] = NodoVariable(t[1],t[2])
    else:
        t[0] = NodoVariable(t[1],None)

def p_arrayL(t):
    '''
        arr : arr IZQLLAVE E DERLLAVE
            | IZQLLAVE E DERLLAVE
    '''
    if(len(t)==5):
        lar = t[1]
        lar.append(t[3])
        t[0] = lar 
    else:
        lar = []
        lar.append(t[2])
        t[0] = lar

def p_error(t):
    if(t!=None):
        print("Error sintáctico en: '%s'" % t.value)
        erroresSintacticos.append("Error Sintactico:  Token: "+t.value + "   En Linea : " +str(t.lineno))
        
        while(True):
            tok = parser.token()
            if(tok==None):
                break
            elif(tok.type=="PCOMA"):
                break
        parser.errok()
        return tok
    else:
        print("Error Irrecuperable")
        erroresSintacticos.append("Error Sintactico: No hay un token!")

#Creador del Analisis Sintactico
import ply.yacc as yacc 

from reportes import *
from tkinter import *

erroresLexicos = []
erroresSintacticos = []
parser = yacc.yacc()

def ejecutar(v):
    global parser
    parser = yacc.yacc()
    ts = TablaMetodos()
    global erroresLexicos 
    erroresLexicos = []
    global erroresSintacticos
    erroresSintacticos = []

    arbol = parser.parse(v,tracking=True)

    try:
        arbol.ejecutar(ts,ts)
    except Exception as e:
        print("Error de compilación!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   "+str(e))
    print("HTML DE REPORTE GRAMATICAL.-----------------------")
    gramaticalASC(ts.metodos)    
    print("VARIBALES--------------------------")
    reporteTS(ts.variables,ts.metodos)
    reporteAST(arbol)
    reporteErrores(erroresLexicos, erroresSintacticos, ts.errores)
    print("METODOS--------------------------")
    for x,y in ts.metodos.items():
        print(x, " = ", y)

    tk = tkinter.Tk() # Create the object
    tk.geometry('1280x200')
    text = tkinter.Text(tk,height=200, width=1280)
    text.pack()

    print("MENSAJES --------------------------")
    for x in ts.mensajes:
        x = str(x).replace('\\n','\n')
        text.insert(END,x)

    tk.mainloop()
    tk.destroy()
