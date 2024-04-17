#!/usr/bin/env python
# -*- coding: utf-8 -*-

from LexicalAnalyzer import LexicalAnalyzer

class Buffer:
    def load_buffer(self):
        with open('program.c', 'r') as file:
            lines = file.readlines()

        buffer_size = 10
        buffer = []

        for i in range(0, len(lines), buffer_size):
            buffer = lines[i:i + buffer_size]
            yield ''.join(buffer)



if __name__ == '__main__':
    buffer = Buffer()
    analyzer = LexicalAnalyzer()

    # Initializing lists for token, lexeme, row, and column
    token_list = []
    lexeme_list = []
    row_list = []
    column_list = []

    for buffer_content in buffer.load_buffer():
        t, lex, lin, col = analyzer.tokenize(buffer_content)
        token_list.extend(t)
        lexeme_list.extend(lex)
        row_list.extend(lin)
        column_list.extend(col)

    print('\nRecognized Tokens:')
    print(f'Token: {token_list}')

