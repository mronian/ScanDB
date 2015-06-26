import ply.yacc as yacc
import Lexer

tokens=Lexer.tokens

#precedence = (
#    ('left','PLUS','MINUS'),
#    ('left','TIMES','DIVIDE'),
#    ('right','UMINUS'),
#    )

contact={}

def begin(p):
    'begin : website email sic_code naics_code'

def p_sic_code(p):
    'sic_code : SIC NUM'
    p[0]=p[2]
    contact['SIC'] = p[2]
             
def p_naics_code(p):
    'naics_code : NAICS NAICS_NUM'
    p[0]=p[2]
    contact['NAICS'] = p[2]
    
def p_email_withtok(p):
    'email : EMAIL_TOK EMAIL'
    p[0]=p[2]
    contact['EMAIL'] = p[2]
    
def p_email(p):
    'email : EMAIL '
    p[0]=p[1]
    contact['EMAIL'] = p[1]
    
def p_website(p):
    'website : WEB'
    p[0]=p[1]
    contact['WEB'] = p[1]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()

