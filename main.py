from core import amogus, dot, matrix
from os import *

commandlist = ['dot', 'amogus','matrix', 'clear', 'help', 'exit']

while True:
    command = input('the-cli-of-fun> ')
    if command in commandlist:
        if command == 'amogus':
            amogus.amogus()
        elif command == 'dot':
            dot.dot()
        elif command == 'matrix':
            matrix.matrix()
        elif command == 'clear':
            amogus.clss()
        elif command == 'help':
            print('''amogus -> Shows a amogus walking
clear  -> Clear the screen
dot    -> Shows a cool dot moving
exit   -> Exit and kill the-cli-of-fun
help   -> Display commands and information
matrix -> Shows a matrix effect''')
        elif command == 'exit':
            exit()
    else:
        print('Unknown command: ', command)