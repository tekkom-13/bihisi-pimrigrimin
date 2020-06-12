from bihisi.lixir import BasicLexer
from bihisi.pirsir import BasicParser
from bihisi.intirpritir import BasicExecute
from sys import *

def open_file(filename):
    data = open(filename, "r").read()
    return data

if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    interpreter = basicinterpreter
    env = {}
    if len(argv) > 1:
        data = open(argv[1])
        data = data.readlines()
        for line in data:
            lex = lexer.tokenize(line)
            tree = parser.parse(lexer.tokenize(line))
            print(tree)
    else:
        while True:
            try:
                text = input('bihisi pimrigrimin » ')
            except EOFError:
                break
            if text:
                tree = parser.parse(lexer.tokenize(text))
                print(tree)