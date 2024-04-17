import re

class LexicalAnalyzer:
    # The line number of the current token
    line_number = 1

    def tokenize(self, code):
        
        rules = [
            ('MAIN', r'main'),          # main
            ('INT', r'int'),            # int
            ('FLOAT', r'float'),        # float
            ('IF', r'if'),              # if
            ('ELSE', r'else'),          # else
            ('WHILE', r'while'),        # while
            ('READ', r'read'),          # read
            ('PRINT', r'print'),        # print
            ('LBRACKET', r'\('),        # (
            ('RBRACKET', r'\)'),        # )
            ('LBRACE', r'\{'),          # {
            ('RBRACE', r'\}'),          # }
            ('COMMA', r','),            # ,
            ('PCOMMA', r';'),           # ;
            ('EQ', r'=='),              # ==
            ('NE', r'!='),              # !=
            ('LE', r'<='),              # <=
            ('GE', r'>='),              # >=
            ('OR', r'\|\|'),            # ||
            ('AND', r'&&'),             # &&
            ('ATTR', r'\='),            # =
            ('LT', r'<'),               # <
            ('GT', r'>'),               # >
            ('PLUS', r'\+'),            # +
            ('MINUS', r'-'),            # -
            ('MULT', r'\*'),            # *
            ('DIV', r'\/'),             # /
            ('ID', r'[a-zA-Z]\w*'),     # IDENTIFIERS
            ('FLOAT_CONST', r'\d+(\.\d*)?'),   # FLOAT
            ('INTEGER_CONST', r'\d+'),          # INT
            ('NEWLINE', r'\n'),         # NEW LINE
            ('SKIP', r'[ \t]+'),        # SPACE and TABS
            ('MISMATCH', r'.'),         # ANOTHER CHARACTER
        ]

        
        tokens_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in rules)

        # The starting index of the current line
        line_start = 0

        # Initializing lists to store the output tokens, lexemes, row numbers, and column numbers
        tokens = []
        lexemes = []
        rows = []
        columns = []

        for match in re.finditer(tokens_regex, code):
            token_type = match.lastgroup
            token_lexeme = match.group(token_type)

            if token_type == 'NEWLINE':
                # Update the starting index of the current line
                line_start = match.end()
                # Increment the line number by 1
                self.line_number += 1
            elif token_type == 'SKIP':
                # Skip the following match
                continue
            elif token_type == 'MISMATCH':
                # Raise an error for an unexpected character
                raise RuntimeError(f"{token_lexeme} unexpected on line {self.line_number}")
            else:
                # Calculating the column number of the match
                column = match.start() - line_start
                # Append the token to the output lists
                tokens.append(token_type)
                lexemes.append(token_lexeme)
                rows.append(self.line_number)
                columns.append(column)
                # Print the token infos
                print(f'Token = {token_type}, Lexeme = "{token_lexeme}", Row = {self.line_number}, Column = {column}')

        # Return the output lists
        return tokens, lexemes, rows, columns