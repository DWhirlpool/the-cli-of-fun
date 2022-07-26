import os
import time
import random

def matrix():
    print('\x1b[32m')

    nums = [1,0]
    tm = 0

    while tm < 30:
        print(random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),)

        tm = tm + 0.1

        time.sleep(0.1)
    print('\x1b[0m')