#!/usr/bin/python

#This program finds the biggest sequence of zeroes, ONLY those surrounded by ones

import os

decimal = 0

while type(decimal) is int:
    try:
        decimal = int(raw_input('Type a decimal number (or any non-number to quit): '))
        
        os.system('clear')

        first_one_found = False

        sequence = 0
        biggest = 0

        while decimal > 0:
            remainder = decimal % 2

            if not first_one_found and remainder == 0:
                decimal //= 2
            elif remainder == 1:
                first_one_found = True
                sequence = 0
                decimal //= 2
            else:
                sequence += 1
                decimal //= 2

            biggest = max(sequence, biggest)

        print '''
        Decimal number: {}
        The biggest zeroes sequence surrounded by ones is: {}
        '''.format(decimal, biggest)
    except ValueError:
        break