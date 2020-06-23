from bihisi.lixir import BasicLexer
from bihisi.pirsir import BasicParser
from bihisi.intirpritir import BasicExecute
from sys import *

def open_file(filename):
    if (".bip" in filename):
        data = open(argv[1])
        return data
    else:
        print("Bukan file bihisi, pastikan ekstensi .bip")
        exit()

def run()
    lexer = BasicLexer()
    parser = BasicParser()
    #interpreter = basicinterpreter
    env = {}
    if len(argv) > 1:
        data = open_file(argv[1])
        text = data.readlines()
        for line in text:
            #lex = lexer.tokenize(line)
            tree = parser.parse(lexer.tokenize(line))
            BasicExecute(tree, env)
    else:
        while True:
            try:
                text = input('bihisi pimrigrimin » ')
            except EOFError:
                break
            if text:
                tree = parser.parse(lexer.tokenize(text))
                BasicExecute(tree, env)
run()