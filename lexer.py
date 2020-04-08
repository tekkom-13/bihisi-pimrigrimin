from sly import lex
#import dari library sly

tokens = [
    'PLUS',         #+
    'MINUS',        #-     
    'MULTIPLY',     #*
    'DIVIDE',       #/
    'MODULO',       #%

    'EQUALS',       #=

    'LPAREN',       #(
    'RPAREN',       #)
    "LBRACE",       #[
    "RBRACE",       #]
    'BLOCKSTART',   #{
    'BLOCKEND',     #}

    'INTEGER',
    'FLOAT',

    'COMMENT',      #--    
]

#mendefinisikan token
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE  = r'/'
t_MODULO = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_BLOCKSTART = r'\{'
t_BLOCKEND = r'\}'
t_EQUALS = r'\='
t_COMMENT = r'\#.*'            
t_ignore  = ' \t' #mengabaikan tab dan spasi

#peran untuk int dan float

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

if __name__ == '__main__':
    lexer = lex.lex()
    