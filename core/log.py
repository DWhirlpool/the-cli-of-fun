from datetime import datetime

def log(command):
    f = open(file = 'the-cli-of-fun.log', mode = 'a')
    if command == 'exit':
        f.write('Exited on {} \n'.format(datetime.now()))
    else:
        f.write("command: {} \n".format(command))
    f.close()

def get_log():
    fle = open('the-cli-of-fun.log', mode = 'rt')
    cont = fle.read()
    fle.close()
    return cont