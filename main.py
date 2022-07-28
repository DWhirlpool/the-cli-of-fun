from core import amogus, dot, matrix, emojipedia, log
from os import *

commandlist = ['dot', 'amogus','matrix', 'emojipedia', 'clear', 'help', 'exit']

print('''
     / \----------------------,
     \_,|                     |  
        |    the-cli-of-fun   |
        |         v2          |
        |  ,--------------------  
        \_/___________________/ 
''')

while True:
    command = input('the-cli-of-fun> ')
    if command in commandlist:
        if command == 'amogus':
            log.log('amogus')
            amogus.amogus()
        elif command == 'dot':
            log.log('dot')
            dot.dot()
        elif command == 'matrix':
            log.log('matrix')
            matrix.matrix()
        elif command == 'emojipedia':
            log.log('emojipedia')
            emojipedia.emojipedia()
        elif command == 'clear':
            log.log('clear')
            amogus.clss()
        elif command == 'help':
            log.log('help')
            print('''amogus -> Shows a amogus walking
clear  -> Clear the screen
dot    -> Shows a cool dot moving
emojipedia -> Shows a lot of emojis
exit   -> Exit and kill the-cli-of-fun
help   -> Display commands and information
matrix -> Shows a matrix effect''')
        elif command == 'exit':
            log.log('exit')
            exit()
    else:
        print('Unknown command: ', command)