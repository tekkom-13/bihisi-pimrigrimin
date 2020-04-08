import lexer

from sys import *


def main ():
 #baca flow source di test
 content = ""
 with open('test.py', 'r') as file:
 	content = file.read()

 	#lexer

 	lexer = lex.lex()
 	#panggil tokenize
 	tokens = Lex.tokenize()