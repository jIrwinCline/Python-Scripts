import sys
import logging
from os import path
import os
# from .classmodule import MyClass
# from .funcmodule import my_function


def main():
    if(len(sys.argv) != 2):
        logging.warning('takes one argument: "trim"')
        print(sys.argv[1])
        return None

    print('Trimming your Create React app project!...')
    args = sys.argv[1]
    # inCorrectDirectory = sys.argv[0] + 'App.js'
    print(os.getcwd() + '\App.js')
    print(path.isfile(os.getcwd() + '\App.js'))

    if(path.islink(sys.argv[0] + '\App.js')):
        length = len(args)

        print(f'count of args :: {length}')
        for arg in args:
            print(f'passed argument :: {arg}')
    else:
        print('incorrect directory')


    # my_function('hello world')
    # my_object = MyClass('Thomas')
    # my_object.say_name()
if __name__ == '__main__':
    main()
