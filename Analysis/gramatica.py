reservadas = {
    'let' : 'LET',
    'fn' : 'FN',
    'main' : 'MAIN',
    'nothing' : 'NULO',
    'i64' : 'INT',
    'f64' : 'FLOAT64',
    'bool' : 'BOOL',
    'char': 'CHAR',
    'true': 'TRUE',
    'false': 'FALSE',
    'String' : 'STRING',
    'Struct': 'STRUCT',
    'mutable': 'MUTABLE',
    'log10': 'LOG10',
    'log': 'LOG',
    'sin': 'SIN',
    'cos': 'COS',
    'tan': 'TAN',
    'sqrt': 'SQRT',
    'print': 'PRINT',
    'println': 'PRINTLN',
    'function': 'FUNCTION',
    'end'     : 'END',
    'parse'   : 'PARSE',
    'trunc'   : 'TRUNC',
    'float'   : 'FLOAT',
    'abs'     : 'ABS',  
    'to_string'  : 'FSTRING',
    'uppercase': 'UPPERCASE',
    'lowercase': 'LOWERCASE',
    'typeof'  : 'TYPEOF',
    'push' :  'PUSH',
    'pop' : 'POP',
    'length': 'LENGTH',
    'if'   : 'IF',
    'elseif' : 'ELSEIF',
    'else': 'ELSE',
#Ciclos  
    'while': 'WHILE',
    'for' : 'FOR',
    'in'  : 'IN',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return' : 'RETURN',


}



tokens  = [
    'PUNTO',
    'LLAVEIZQ',
    'LLAVEDER',
    'PTCOMA',
    'PARIZQ',
    'PARDER',
    'BRAIZQ',
    'BRADER',
    'COMA',
    'DOSPTS',
    'DOSP',
    'ASIGN',
    'CADENA',
    'CHARVALOR',
    'ID',
#OPERATORS     
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'POTENCIA',
    'MODULO',
#RELACIONALES
    'MAYOR',
    'MENOR',
    'MAIGUAL',
    'MEIGUAL',
    'IGUAL',
    'NOIGUAL',
#BINARIAS 
    'OR',
    'AND',
    'NOT',        
#DATOS    
    'DECIMAL',
    'ENTERO',
    'CONST'
    #'RANGO'
]+ list(reservadas.values())

# Tokens
t_PUNTO     = r'.'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_PTCOMA    = r';'
t_DOSP      = r':'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_BRAIZQ    = r'\['
t_BRADER    = r'\]'
t_COMA      = r','
t_DOSPTS    = r'::'
t_ASIGN     = r'='    
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_POTENCIA  = r'\^' 
t_MODULO    = r'%'
t_MAYOR     = r'>'
t_MENOR     = r'<'
t_MAIGUAL   = r'>='
t_MEIGUAL   = r'<='
t_IGUAL     = r'=='
t_NOIGUAL   = r'!='
t_OR        = r'\|\|'
t_AND       = r'&&'
t_NOT       = r'!'

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

'''
def t_RANGO(t):
    r'(\d+:\d+)'
    print(t.value) 
    t.type =  'RANGO'
    return t
'''

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CHARVALOR(t):
    r'\'.?\''
    t.value = t.value[1:-1] #Remueve las comillas simples
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value,'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t  

# Comentario de múltiples líneas #= .. =#
def t_COMENTARIO_MULTILINEA(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')
          

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1
    


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

     
def t_error(t):
    print("Illegal character '%s'" % t.value[0] ,  t.lexer.lineno)
    listaErrores.append({"tipo":"Error Lexico", "descripcion" : "Caracter invalido:  "+ str(t.value[0]), "fila":  t.lexer.lineno , "columna": find_column(t.lexer.lexdata,t.lexer) })
    t.lexer.skip(1)

# Construyendo el analizador léxico
from typing import Type
from Expresion.natives.Typeof import Typeof
from Expresion.natives.Lowercase import Lowercase
from Expresion.natives.Uppercase import Uppercase
from Instruction.transferencia.Return import Return
from Expresion.Unaria.call_function import CallFunction
from Expresion.Id import Id
from Instruction.Asignacion import Asignacion
from Instruction.Print import Print
from Expresion.natives.String import String
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Environment.Primitive import Primitive
from Environment.Rango import Rango
from Enum.typeOperation import typeOperation
from Enum.typeExpression import typeExpression
from Expresion.Arithmetic.Add import Add
from Expresion.Arithmetic.Mult import Mult
from Expresion.Relational.Relational import Relational
from Expresion.Logical.Logical import Logical
from Expresion.Logical.Not import Not
from Expresion.Unaria.Negativo import Negativo
from Expresion.natives.Logaritmo import Logaritmo
from Expresion.natives.Trigonometry import Trignometry
from  Expresion.natives.Parse import Parse
from Expresion.natives.Trunc import Trunc
from Expresion.natives.Float import Float
from Expresion.natives.String import String
from Instruction.Print import Print
from Instruction.control.condicionIf import CondicionIf
from Instruction.control.If import If
from Instruction.ciclos.While import While
from Instruction.ciclos.For import IFor
from Instruction.transferencia.Break import Break
from Instruction.transferencia.Continue import Continue
from Instruction.bloque import Bloque
from Funcion.Funcion import Funcion
from Funcion.parametro import Parametro
from Environment.Contexto import listaErrores



import ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','OR','AND'),
    ('left','MAS','MENOS'),
    ('left','DIVIDIDO','POR'),
    ('left','MODULO','POTENCIA' ),
    ('left','NOIGUAL','IGUAL'),
    ('left','MEIGUAL', 'MENOR'),
    ('left','MAIGUAL','MAYOR'),
   
    ('right','NOT'),
    ('right','UMENOS'),
    )

def p_main(t):
    '''f1 : FN MAIN PARIZQ PARDER LLAVEIZQ inicio LLAVEDER '''
    parent =  Environment(None)
    for ins in t[6]:
        ins.execute(parent)


# Definición de la gramática=====================================================
def p_inicio(t):
    '''inicio : l_instruccion '''
    t[0] = t[1]    

#======================== instruction =================================
def p_lista_instruccion(t):
    '''l_instruccion :  l_instruccion instruccion 
                     |  instruccion '''
    if(len(t) == 3):
        t[1].append(t[2])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion : print PTCOMA
                   | println  PTCOMA
                   | asignacion PTCOMA
                   | if
                   | while
                   | break
                   | continue
                   | para
                   | funcion
                   | return 
                   '''
    t[0] = t[1]

def p_asignacion(t):
    '''asignacion : LET ID ASIGN expresion
                  | LET ID DOSP type ASIGN expresion    '''
    if len(t) == 5:
        t[0] = Asignacion(t[2], t[4] , None ,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif len(t) == 7 :
        t[0] = Asignacion(t[2], t[6], t[4] ,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)                  
                  

def p_type(t):
    '''type : INT
            | FLOAT64
            | STRING
            | CHAR
            | BOOL
    '''
    if t[1] == 'i64':  t[0] = Primitive(typeExpression.INT, typeExpression.ERROR)
    elif t[1] == 'f64': t[0] = Primitive(typeExpression.FLOAT, typeExpression.ERROR)
    elif t[1] == 'String' : t[0] = Primitive(typeExpression.STRING,typeExpression.ERROR)
    elif t[1] == 'char'   : t[0] = Primitive(typeExpression.CHAR, typeExpression.ERROR)
    elif t[1] == 'bool'   : t[0] = Primitive(typeExpression.BOOL, typeExpression.ERROR)  




def p_print(t):
    '''print : PRINT PARIZQ l_expresion PARDER'''
    t[0] = Print(t[3], False,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)

def p_printl(t):
    '''println : PRINTLN NOT PARIZQ l_expresion PARDER'''
    t[0] = Print(t[4], True,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)

def p_if(t):
    '''if : l_if  ELSE  bloque END PTCOMA 
          | l_if  END PTCOMA 
    '''
    if(len(t) == 4):
        t[0] = If(t[1], t[2],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno) 
    elif(len(t) == 2):
        t[0] = If(t[1], None,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)

def p_lIf(t):
    ''' l_if : l_if   ELSEIF expresion bloque
             | IF expresion bloque 
    '''
    if(len(t) == 5):
        t[1].append(CondicionIf(t[3],t[4], False, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno))
        t[0] = t[1]
    elif(len(t) == 4):
        t[0] = [CondicionIf(t[2], t[3], False, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)]

def p_while(t):
    ''' while : WHILE expresion bloque END PTCOMA 
    '''
    t[0] = While(t[2], t[3] ,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)

def p_For(t):
    '''para : FOR ID IN rango bloque END PTCOMA
    '''
    t[0] = IFor(t[2], t[4],t[5],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)  # Tipo de for con un rango 
    #Tipo de for con cadena 
    #Tipo de for con un arreglo 

def p_break(t):
    ''' break : BREAK PTCOMA
    '''
    t[0] = Break(find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno) 

def p_continue(t):
    ''' continue : CONTINUE PTCOMA'''
    t[0] = Continue(find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)

def p_return(t):
    ''' return : RETURN  PTCOMA
               | RETURN  expresion PTCOMA 
    '''
    if len(t) == 3:
        t[0] = Return(None,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno) 
    elif len(t) == 4:
        t[0] = Return(t[2],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)        


def p_rango(t):
    ''' rango : ENTERO DOSP ENTERO
              | expresion  
    '''
    if(len(t) == 4):
        t[0] = Rango(t[1], t[3])
    elif(len(t) == 2):
        t[0] = t[1] 

def p_dfuncion(t):
    ''' funcion : FUNCTION ID PARIZQ PARDER bloque END PTCOMA 
                | FUNCTION ID PARIZQ l_parametro PARDER bloque END PTCOMA 
    '''
    if len(t) == 8:
        t[0] = Funcion(t[2], None, t[5] ,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif len(t) == 9:
        t[0] = Funcion(t[2], t[4], t[6] ,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)

def p_bloque(t):
    ''' bloque : 
               |  l_instruccion 
    '''
    if len(t) == 1:
        t[0] = Bloque(None,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif len(t) == 2:
        t[0] = Bloque(t[1],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno) 




#====================================================
def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion
                  | expresion MODULO   expresion
                  | expresion POTENCIA  expresion
                  | expresion MAYOR    expresion
                  | expresion MENOR    expresion
                  | expresion MAIGUAL  expresion
                  | expresion MEIGUAL  expresion
                  | expresion IGUAL    expresion
                  | expresion NOIGUAL  expresion
                  | expresion AND      expresion
                  | expresion OR       expresion  
                  '''
    if t[2] == '+'  : t[0] = Add(t[1], t[3], typeOperation.SUMA, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '-': t[0] = Add(t[1], t[3], typeOperation.RESTA, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '*': t[0] = Mult(t[1], t[3], typeOperation.MULT, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '/': t[0] = Add(t[1], t[3], typeOperation.DIVISION, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '%': t[0] = Add(t[1], t[3], typeOperation.MODULO, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno) 
    elif t[2] == '^': t[0] = Mult(t[1], t[3], typeOperation.POTENCIA, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '>': t[0] = Relational(t[1],t[3],typeOperation.MAYOR,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '<': t[0] = Relational(t[1],t[3],typeOperation.MENOR,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '>=': t[0] = Relational(t[1],t[3],typeOperation.GMAYOR,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '<=': t[0] = Relational(t[1],t[3],typeOperation.GMENOR,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '==': t[0] = Relational(t[1],t[3],typeOperation.IGUAL,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '!=': t[0] = Relational(t[1],t[3],typeOperation.NIGUAL,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '&&': t[0] = Logical(t[1],t[3],typeOperation.AND,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[2] == '||' : t[0] = Logical(t[1],t[3],typeOperation.OR,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)  

#====================================================
def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                 | NOT expresion   
    '''
    if t[1] == '-' : t[0] = Negativo(t[2],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[1] == '!':t[0] = Not(t[2],typeOperation.NOT,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno) 
    

#====================================================
def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]


#====================================================
def p_expresion_number(t):
    'expresion    : ENTERO'
    t[0] =  Primitive(t[1],typeExpression.INT)

def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = Primitive(t[1],typeExpression.FLOAT)

def p_expresion_nulo(t):
    'expresion : NULO'
    t[0] = Primitive(t[1], typeExpression.NOTHING)   

def p_expresion_id(t):
    'expresion : ID'
    t[0] = Id(t[1],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)     

def p_expresion_bool(t):
    '''expresion : FALSE
                 | TRUE'''
    if(t[1] == 'false') :  t[0] =Primitive(False , typeExpression.BOOL)
    else :   t[0] = Primitive(True, typeExpression.BOOL)           

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = Primitive(t[1],typeExpression.STRING)

def p_expresion_char(t):
    'expresion : CHARVALOR'
    t[0] = Primitive(t[1], typeExpression.CHAR)

def p_expresion_int64(t):
    'expresion : INT'
    t[0] = Primitive(typeExpression.INT,typeExpression.ERROR)

def p_expresion_float64(t):
    'expresion : FLOAT64'
    t[0] = Primitive(typeExpression.FLOAT,typeExpression.ERROR) 

#==================== Lista de expresiones ========================

def p_expresion_list(t):
    '''l_expresion :  l_expresion COMA expresion 
                   | expresion '''
    if(len(t) == 4):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

def p_parametros(t):
    ''' l_parametro : l_parametro COMA parametro 
                    | parametro
    '''                      
    if len(t) == 4 :
        t[1].append(t[3])
        t[0] = t[1]
    elif len(t) == 2 :
        t[0] = [t[1]]   

def p_param(t):
    ''' parametro :  ID DOSPTS type 
                  |  ID
    '''
    if len(t) == 4 :
        t[0] = Parametro(t[1], t[3])
    elif len(t) == 2:
        t[0] = Parametro(t[1],Primitive(typeExpression.OBJECT, typeExpression.ERROR))    

#==============================================

def p_expresion_natives(t):
    '''expresion : expresion PUNTO SQRT PARIZQ  PARDER
                | expresion PUNTO FSTRING PARIZQ  PARDER 
                | ID PARIZQ  PARDER 
                | ID PARIZQ l_expresion PARDER                 
                '''
   # if t[1] == 'log'     : t[0] = Logaritmo(t[3],t[5],True,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
   # elif t[1] == 'log10' : t[0] = Logaritmo(t[3],None,False, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
   # elif t[1] == 'sin'   : t[0] = Trignometry(t[3],typeOperation.SIN, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
   # elif t[1] == 'cos'   : t[0] = Trignometry(t[3],typeOperation.COS, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
   # elif t[1] == 'tan'   : t[0] = Trignometry(t[3],typeOperation.TAN, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    if t[3] == 'sqrt'   : t[0] = Trignometry(t[1],typeOperation.SQR, find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
   # elif t[1] == 'parse'  : t[0] = Parse(t[3],t[5],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
   # elif t[1] == 'trunc'  : t[0] = Trunc(t[3],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
   # elif t[1] == 'float'  : t[0] = Float(t[3],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif t[3] == 'to_string' : t[0] = String(t[1],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
   # elif t[1] == 'uppercase' : t[0] = Uppercase(t[3],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
   # elif t[1] == 'lowercase' : t[0] = Lowercase(t[3],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
   # elif t[1] == 'typeof'    : t[0] = Typeof(t[3],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif len(t) == 4  : t[0]=     CallFunction(t[1], None,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    else : t[0] = CallFunction(t[1], t[3],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)   
#====================================================

'''
def p_callFunction(t):
     expresion : ID PARIZQ  PARDER 
                  | ID PARIZQ l_expresion PARDER
   
    if len(t) == 4:
        t[0] = CallFunction(t[1], None,find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)
    elif len(t) == 5:
        t[0] = CallFunction(t[1], t[3],find_column(t.lexer.lexdata,t.lexer), t.lexer.lineno)   
  '''      

#===================================================
def p_error(t):
    if not t:
        print("End of File!")
        return

    # Read ahead looking for a closing '}'
    while True:
        tok = parser.token()             # Get the next token
        listaErrores.append({"tipo":"Error Sintactico", "descripcion" : "No se esperaba "+ str(t.value), "fila":  t.lexer.lineno , "columna": find_column(t.lexer.lexdata,t.lexer) })
        if not tok or tok.type == 'PTCOMA':
            break
    parser.restart()    
    print("Error sintáctico en '%s'" % t.value)
    #print("Error tipo en '%s" % t.type)

#====================================================
#====================================================
#====================================================

import ply.yacc as yacc
parser = yacc.yacc()