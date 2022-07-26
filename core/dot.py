from math import *
from time import *

def dot():
    def dot_string(x):
        return ' ' * int(20 * cos(radians(x)) + 20) + 'o'

    for i in range(0, 1800, 12):
        s = dot_string(i)
        print(s)
        sleep(0.1)