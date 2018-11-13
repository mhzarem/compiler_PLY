import ply.lex as lex
import codecs


class Lexer:
    # List of token names.
    tokens = (
        'PROGRAM_KW',
        'WHILE_KW',
        'IF_KW',
        'FOR_KW',
        'SWITCH_KW',
        'CASE_KW',
        'DEFAULT_KW',
        'RETURN_KW',
        'BREAK_KW',
        'CONTINUE_KW',
        'READ_KW',
        'WRITE_KW',
        'ELSE_KW',
        'THEN_KW',
        'INT_KW',
        'FLOAT_KW',
        'CHAR_KW',
        'BOOL_KW',
        'VOID_KW',
        'CALLOUT_KW',
        'BOOL_CONSTANT',
        'EQ',
        'NE',
        'LT',
        'LE',
        'GT',
        'GE',
        'NOT',
        'PLUS',
        'MINUS',
        'MULT',
        'DIV',
        'REM',
        'AND_THEN',
        'AND',
        'OR_ELSE',
        'OR',
        'SHR',
        'SHL',
        'ID',
        'CHAR_CONSTANT',
        'INT_CONSTANT',
        'FLOAT_CONSTANT',
        'STRING_CONSTANT',
        'OPENING_BRACE',
        'CLOSING_BRACE',
        'OPENING_BRACKET',
        'CLOSING_BRACKET',
        'OPENING_PARENTHESES',
        'CLOSING_PARENTHESES',
        'COLON',
        'EXP',
        'SEMICOLON',
        'COMMA',
        'ERROR'

    )
    reserved = {
        'program': 'PROGRAM_KW',
        'while': 'WHILE_KW',
        'if': 'IF_KW',
        'for': 'FOR_KW',
        'switch': 'SWITCH_KW',
        'case': 'CASE_KW',
        'default': 'DEFAULT_KW',
        'return': 'RETURN_KW',
        'break': 'BREAK_KW',
        'continue': 'CONTINUE_KW',
        'read': 'READ_KW',
        'write': 'WRITE_KW',
        'else': 'ELSE_KW',
        'then': 'THEN_KW',
        'integer': 'INT_KW',
        'float': 'FLOAT_KW',
        'character': 'CHAR_KW',
        'bool': 'BOOL_KW',
        'void': 'VOID_KW',
        'callout': 'CALLOUT_KW',
        'true': 'BOOL_CONSTANT',
        'false': 'BOOL_CONSTANT',

        }

    t_OPENING_BRACE = r'{'
    t_CLOSING_BRACE = r'}'
    t_OPENING_BRACKET = r'\['
    t_CLOSING_BRACKET = r'\]'
    t_OPENING_PARENTHESES = r'\('
    t_CLOSING_PARENTHESES = r'\)'
    t_COLON = r':'
    t_EXP = r'='
    t_NE = r'!='
    t_SEMICOLON = r';'
    t_COMMA = r','
    t_LT = r'<'
    t_LE = r'<='
    t_EQ = r'=='
    t_GE = r'>='
    t_GT = r'>'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_MULT = r'\*'
    t_DIV = r'\/'
    t_REM = r'\%'
    t_NOT = r'!'
    t_AND_THEN = r'\&&'
    t_AND = r'&'
    t_OR_ELSE = '\|\|'
    t_OR = r'\|'
    t_SHR = r'>>'
    t_SHL = r'<<'

    # stat table
    state_table = []

    def t_COMMENT(self, t):
        r'(//.*)|%%%.*[\r\n]*.*%%%'
        pass


    def t_FLOAT_CONSTANT(self, t):
        r'[1-9][0-9]*[eE][+|-][1-9][0-9]*|'\
          '[1-9][0-9]*[eE][1-9][0-9]*|'\
          '[1-9][0-9]*\.[0-9]*[1-9][eE][+|-][1-9][0-9]*|'\
          '[1-9][0-9]*\.[0-9]*[1-9][eE][1-9][0-9]*|'\
          '[1-9][0-9]*\.[0-9]*[1-9]|'\
          '[1-9][0-9]*\.[0][eE][+|-][1-9][0-9]*|'\
          '[1-9][0-9]*\.[0]'
        return t

    def t_INT_CONSTANT(self, t):
        r'(([0-9|a-f]+x)|'\
         '[0-1]+b)|'\
         '([0-9]+)'

        return t

    def t_ID(self, t):
        r'([a-zA-Z]{1,5}[0-9])+[a-zA-Z]*[_][a-zA-Z][a-zA-Z0-9]*|'\
         '[a-zA-Z]+[_][a-zA-Z][a-zA-Z0-9]*|'\
         '[a-zA-Z][a-zA-Z0-9]*'
        t.type = self.reserved.get(t.value, 'ID')  # Check for reserved words

        if str(t.value).find('_') != -1:
            temp = str(t.value).split('_')
            if len(temp[0]) % 2 == 0:
                self.t_error(t)
                t.type = 'ERROR'

        if t.type == 'ID':
            if t.value not in self.state_table:
                self.state_table.append(t.value)
        return t


    def t_CHAR_CONSTANT(self, t):
        r'\'.*\''
        t.value = str(t.value).split('\'')[1]
        return t


    def t_STRING_CONSTANT(self, t):
        # you can you [\r\n] as new line or [ ] as space even you can't find star in it
        r'\".*\"(([\r\n]|[ ])*\+([\r\n]|[ ])*\".*\")*'
        temp = str(t.value).split("\"")
        concat = ""
        for string in temp:
            if temp.index(string) % 2 == 1:
                concat = concat + string
        t.value = concat
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t\r'

    # Error handling rule
    def t_error(self, t):
        print("Illegal type '%s'" % t.value)
        t.lexer.skip(1)

    def build(self, **kwargs):
        '''
        build the lexer
        '''
        self.lexer = lex.lex(module=self, **kwargs)

        return self.lexer


f = codecs.open('test', encoding='utf-8')
data = f.read()
f.close()
temp = Lexer()
lexer = temp.build()
lexer.input(data)

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





