import lexer

# Give the lexer some input
#lexer.input(data)

# Tokenize
for tok in lexer:
   print(tok)

data = '''
[25/(3*40) + {300-20} -16.5]
{(300-250)<(400-500)}
20 & 30 | 50
# This is a comment
'''

