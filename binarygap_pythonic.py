#!/usr/bin/python

#This program finds the biggest sequence of zeroes, ONLY those surrounded by ones

import os

decimal = 0

while type(decimal) is int:
    try:
        decimal = int(raw_input('Type a decimal number (or any non-number to quit): '))
        
        os.system('clear')
        
        binary = bin(decimal)[2:]
        binary_sequences = binary.rstrip('0').split('1')
        biggest_zeroes_sequence = len(max(binary_sequences))

        print '''
        Decimal number: {}
        Binary number: {}
        The biggest zeroes sequence surrounded by ones is: {}
        '''.format(decimal, binary, biggest_zeroes_sequence)
    except ValueError:
        break