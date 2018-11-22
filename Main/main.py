from Lexer.lexer import Lexer
from Parser.yacc import Yacc
import codecs

f = codecs.open('Samples/test', encoding='utf-8')
data = f.read()
f.close()
temp = Lexer()
lexer = temp.build()
lexer.input(data)
yacc = Yacc()
parser = yacc.build().parse(data, lexer)


while True:
    at = "-"
    tok = lexer.token()
    if not tok:
        break  # No more input
    if tok.type == 'ID':
        print(str(tok.value)+'\t'+str(tok.type)+'\t'+str(temp.state_table.index(tok.value)))
    elif tok.type == 'BOOL_CONSTANT':
        if tok.value == 'true':
            print(str(tok.value) + '\t' + str(tok.type) + '\t' + "1")
        else:
            print(str(tok.value) + '\t' + str(tok.type) + '\t' + "0")
    elif tok.type == 'CHAR_CONSTANT':
        print(str(tok.value) + '\t' + str(tok.type) + '\t' + str(tok.value))
    elif tok.type == 'INT_CONSTANT':
        print(str(tok.value) + '\t' + str(tok.type) + '\t' + str(tok.value))
    elif tok.type == 'FLOAT_CONSTANT':
        print(str(tok.value) + '\t' + str(tok.type) + '\t' + str(tok.value))
    elif tok.type == 'STRING_CONSTANT':
        print(str(tok.value) + '\t' + str(tok.type) + '\t' + str(tok.value))
    else:
        print(str(tok.value) + '\t' + str(tok.type) + '\t' + at)


