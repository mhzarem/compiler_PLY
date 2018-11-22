from ply import yacc
from lexer import Lexer


class Yacc:
    tokens = Lexer.tokens
    precedence = (
        ('left', 'OR', 'OR_ELSE'),
        ('left', 'AND', 'AND_THEN'),
        ('left', 'EQ'),
        ('left', 'LT', 'GT', 'LE', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'REM'),
        ('left', 'MULT', 'DIV'),
        ('right', 'NOT'),
        ('nonassoc', 'ELSE_KW'),
        ('nonassoc', 'ID')
    )

    def p_start_program(self, p):
        """program : PROGRAM_KW ID OPENING_BRACE field_decl_list method_decl_list CLOSING_BRACE """
        print(" RULE1 --> tarif field and method")

    def p_decl_list(self, p):
        """field_decl_list : field_decl field_decl_list
                            |
        """
        if len(p) == 3:
            print(" RULE2.1 --> list fieldha")
        elif len(p) == 2:
            print(" RULE2.2 --> bedune field!")

    def p_decl(self, p):
        """ field_decl : type field_name_list SEMICOLON"""
        print(" RULE3 --> tarif field")

    def p_field_name_list(self, p):
        """field_name_list : field_name COMMA field_name_list
                            | field_name
        """
        if len(p) == 3:
            print(" RULE4.1 --> tarif name fieldha")
        elif len(p) == 2:
            print(" RULE4.2 --> tarif name field")

    def p_field_name(self, p):
        """field_name : ID OPENING_BRACKET INT_CONSTANT CLOSING_BRACKET
                        | ID
        """
        if len(p) == 3:
            print(" RULE5.1 --> name arraye")
        elif len(p) == 2:
            print(" RULE5.2 --> name moteghayer")

    def p_method_decl_list(self, p):
        """method_decl_list : method_decl method_decl_list
                            |
        """
        if len(p) == 3:
            print(" RULE6.1 --> list method ha!")
        elif len(p) == 2:
            print(" RULE6.2 --> bedune method!")

    def p_method_decl(self, p):
        """method_decl : return_type ID OPENING_PARENTHESES formal_parameter_list CLOSING_PARENTHESES block"""
        print(" RULE7 --> tarif method!")

    def p_method_call(self, p):
        """method_call : ID OPENING_PARENTHESES actual_parameters CLOSING_PARENTHESES
                        | CALLOUT_KW OPENING_PARENTHESES STRING_CONSTANT callout_parameters CLOSING_PARENTHESES """
        print(" RULE8 --> seda zadane method!")

    def p_actual_parameters(self, p):
        """actual_parameters : actual_parameter_list
                            |
         """
        if len(p) == 2:
            print(" RULE9.1 --> actual parameter")
        elif len(p) == 1:
            print(" RULE9.2 --> bedune actual parameter ")

    def p_actual_parameter_list(self,p):
        """actual_parameter_list : expr COMMA actual_parameter_list
                                | expr
        """
        if len(p) == 4:
            print(" RULE10.1 --> actual parameter list")
        elif len(p) == 2:
            print(" RULE10.2 --> actual parameter list just expr")

    def p_callout_parameters(self, p):
        """callout_parameters : COMMA callout_parameter_list
                                | expr
        """
        if len(p) == 3:
            print(" RULE11.1 --> callout parameters")
        elif len(p) == 2:
            print(" RULE11.2 --> callout parameters just expr")

    def p_callout_parameter_list(self, p):
        """callout_parameter_list : expr COMMA callout_parameter_list
                                | expr
        """
        if len(p) == 4:
            print(" RULE12.1 --> callout parameter list")
        elif len(p) == 2:
            print(" RULE12.2 --> callout parameter list just expr")

    def p_formal_parameter_list(self, p):
        """formal_parameter_list : argumant_list
                                |
        """
        if len(p) == 2:
            print(" RULE13.1 --> formal parameter list")
        elif len(p) == 1:
            print(" RULE13.2 --> no formal parameter list")

    def p_argumant_list(self, p):
        """argumant_list : type ID COMMA argumant_list
                        | type ID
        """
        if len(p) == 4:
            print(" RULE14.1 --> argument list ")
        elif len(p) == 1:
            print(" RULE14.2 --> argument list just type ID")

    def p_type(self, p):
        """type : INT_KW
                | FLOAT_KW
                | CHAR_KW
                | BOOL_KW
        """
        if p[1] == 'INT_KW':
            print(" RULE15.1 --> type INT ")
        elif p[1] == 'FLOAT_KW':
            print(" RULE15.2 --> type FLOAT ")
        elif p[1] == 'CHAR_KW':
            print(" RULE15.3 --> type CHAR ")
        elif p[1] == 'BOOL_KW':
            print(" RULE15.4 --> type BOOL ")

    def p_constant(self, p):
        """constant : INT_CONSTANT
        | FLOAT_CONSTANT
        | CHAR_CONSTANT
        | BOOL_CONSTANT
        """

    def p_return_type(self, p):
        """return_type : type
                    | VOID_KW
        """
        print(" RULE16 --> return type")

    def p_return_expr(self, p):
        """return_expr : expr
                        |
        """
        print(" RULE17 --> return expr")

    def p_block(self, p):
        """block : OPENING_BRACE var_decl_list statement_list CLOSING_BRACE """
        print(" RULE18 --> block")

    def p_var_decl_list(self, p):
        """var_decl_list : var_decl var_decl_list
                        |
        """
        if len(p) == 2:
            print(" RULE19.1 --> var_decl_list ")
        elif len(p) == 1:
            print(" RULE19.2 --> no var_decl_list")

    def p_var_decl(self, p):
        """var_decl : type id_list SEMICOLON"""
        print(" RULE20 --> var_decl ")

    def p_id_list(self, p):
        """id_list : ID COMMA id_list
                    | ID
        """
        if len(p) == 4:
            print(" RULE21.1 --> id_list ")
        elif len(p) == 1:
            print(" RULE21.2 --> id_list just ID")

    def p_statement_list(self, p):
        """statement_list : statement statement_list
                            |
        """
        if len(p) == 3:
            print(" RULE22.1 --> statement_list ")
        elif len(p) == 1:
            print(" RULE22.2 --> no statement_list")

    def p_statement(self, p):
        """statement : assignment SEMICOLON
        | method_call SEMICOLON
        | IF_KW OPENING_PARENTHESES expr CLOSING_PARENTHESES THEN_KW block SEMICOLON
        | IF_KW OPENING_PARENTHESES expr CLOSING_PARENTHESES THEN_KW block ELSE_KW block SEMICOLON
        | WHILE_KW OPENING_PARENTHESES expr CLOSING_PARENTHESES block SEMICOLON
        | FOR_KW OPENING_PARENTHESES for_initialize SEMICOLON expr SEMICOLON assignment CLOSING_PARENTHESES block SEMICOLON
        | SWITCH_KW OPENING_PARENTHESES ID CLOSING_PARENTHESES OPENING_BRACE case_statements CLOSING_BRACE SEMICOLON
        | RETURN_KW return_expr SEMICOLON
        | BREAK_KW SEMICOLON
        | CONTINUE_KW SEMICOLON
        | block
        | READ_KW OPENING_PARENTHESES ID CLOSING_PARENTHESES SEMICOLON
        | WRITE_KW OPENING_PARENTHESES write_parameter CLOSING_PARENTHESES SEMICOLON
        | SEMICOLON
        """
        print(" RULE23 --> statements")

    def p_case_statement(self, p):
        """case_statements : CASE_KW constant COLON statement case_statements
                        | DEFAULT_KW COLON statement
                        |
        """
        print(" RULE24 --> case statements")

    def p_write_parameter(self, p):
        """write_parameter : expr
                        | STRING_CONSTANT
        """
        print(" RULE25 --> write statements")

    def p_assignment(self, p):
        """assignment : location EXP expr
                        | location
        """
        print(" RULE26 --> assignment")

    def p_for_initialize(self, p):
        """for_initialize : assignment
                        |
        """
        print(" RULE27 --> for_init")

    def p_location(self, p):
        """location : ID
                    | ID OPENING_BRACKET expr CLOSING_BRACKET"""
        print(" RULE27 --> location")

    def p_expr(self, p):
        """expr : location
                | constant
                | OPENING_PARENTHESES expr CLOSING_PARENTHESES
                | method_call
                | operational_expr
        """
        print(" RULE28 --> expr")

    def p_operational_expr(self, p):
        """operational_expr : expr LT expr
        | expr LE expr
        | expr GT expr
        | expr GE expr
        | expr EQ expr
        | expr NE expr
        | expr AND expr
        | expr OR expr
        | expr AND_THEN expr
        | expr OR_ELSE expr
        | expr PLUS expr
        | expr MINUS expr
        | expr DIV expr
        | expr REM expr
        | SHR expr
        | SHL expr
        | MINUS expr
        | NOT expr
        """

    def p_error(self, p):
        print('syntax error! @ ' + str(p.value))

    def build(self, **kwargs):
        """
        build the parser
        """
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
