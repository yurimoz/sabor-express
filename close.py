import os
from time import sleep


def close_app(msg = 'Thanks for using our system! Bye!'):

    print(msg)
    sleep(2)
    os.system('cls')
    